"""
Content Generation Endpoints
"""
from typing import Any
from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, status, BackgroundTasks
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from ...database import get_db
from ...models import Brand, Content, User
from ...models.content import ContentType, ContentStatus
from ...schemas.content import GenerateRequest, GenerateResponse, GenerateImageRequest
from ...services.ai.text_generator import TextGenerator
from ...services.ai.image_generator import ImageGenerator, ContentImageGenerator
from ..deps import get_current_user

router = APIRouter()


def get_content_type_key(content_type: str) -> str:
    """Map content type to usage tracking key"""
    mapping = {
        "social_facebook": "social_posts",
        "social_instagram": "social_posts",
        "social_tiktok": "social_posts",
        "social_linkedin": "social_posts",
        "ads_facebook": "ads_copies",
        "ads_google": "ads_copies",
        "ads_tiktok": "ads_copies",
        "landing_page": "landing_pages",
        "video_script": "video_scripts",
    }
    return mapping.get(content_type, "social_posts")


async def increment_usage(user: User, content_type: str, db: AsyncSession):
    """Increment user's usage count"""
    usage_key = get_content_type_key(content_type)
    if user.usage_this_month is None:
        user.usage_this_month = {}
    
    current = user.usage_this_month.get(usage_key, 0)
    user.usage_this_month[usage_key] = current + 1
    await db.commit()


@router.post("/content", response_model=GenerateResponse)
async def generate_content(
    request: GenerateRequest,
    background_tasks: BackgroundTasks,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
) -> Any:
    """
    Generate content based on brand and parameters
    
    Supported content types:
    - social_facebook, social_instagram, social_tiktok, social_linkedin
    - ads_facebook, ads_google, ads_tiktok
    - landing_page
    - video_script
    """
    
    # Check usage limit
    usage_key = get_content_type_key(request.content_type.value)
    if not current_user.can_generate(usage_key):
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail=f"Monthly limit reached for {usage_key}. Please upgrade your plan."
        )
    
    # Get brand
    result = await db.execute(
        select(Brand).where(
            Brand.id == request.brand_id,
            Brand.user_id == current_user.id
        )
    )
    brand = result.scalar_one_or_none()
    
    if not brand:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Brand not found"
        )
    
    # Initialize generator
    try:
        generator = TextGenerator(provider=request.ai_provider)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
    
    # Get brand context
    brand_context = brand.to_context_string()
    
    # Generate based on content type
    content_type = request.content_type.value
    
    try:
        if content_type.startswith("social_"):
            platform = content_type.replace("social_", "")
            result = generator.generate_social_content(
                brand_context=brand_context,
                platform=platform,
                objective=request.objective or "engagement",
                topic=request.topic or "",
                product_name=request.product_name,
                key_message=request.key_message,
                promotion=request.promotion,
                body_length=request.body_length or "medium",
                num_variations=request.num_variations,
                industry=brand.industry,
                temperature=request.temperature
            )
        
        elif content_type.startswith("ads_"):
            platform = content_type.replace("ads_", "")
            if not request.product_name:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="product_name is required for ads generation"
                )
            result = generator.generate_ads_copy(
                brand_context=brand_context,
                platform=platform,
                product_name=request.product_name,
                offer=request.offer,
                landing_url=request.landing_url,
                objective=request.objective or "conversion",
                num_variations=request.num_variations,
                temperature=request.temperature
            )
        
        elif content_type == "landing_page":
            if not request.product_name:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="product_name is required for landing page generation"
                )
            result = generator.generate_landing_page(
                brand_context=brand_context,
                product_name=request.product_name,
                price=None,  # Could be added to request
                offer=request.offer,
                temperature=request.temperature
            )
            # Wrap landing page in variations format for consistency
            result["variations"] = [result.get("landing_page", {})]
        
        elif content_type == "video_script":
            result = generator.generate_video_script(
                brand_context=brand_context,
                platform="tiktok",  # Default, could be parameterized
                duration=request.duration or 30,
                topic=request.topic or "",
                product_name=request.product_name,
                video_style=request.video_style or "talking_head",
                temperature=request.temperature
            )
            # Wrap script in variations format
            result["variations"] = [result.get("script", {})]
        
        else:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Unsupported content type: {content_type}"
            )
        
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Generation failed: {str(e)}"
        )
    
    # Increment usage in background
    background_tasks.add_task(increment_usage, current_user, content_type, db)
    
    # Build response
    return GenerateResponse(
        success=result.get("success", True),
        content_type=content_type,
        brand_name=brand.name,
        variations=result.get("variations", []),
        ai_model_used=result.get("ai_model_used", "unknown"),
        tokens_used=result.get("tokens_used", {}),
        generation_time_seconds=result.get("generation_time_seconds", 0)
    )


@router.post("/image")
async def generate_image(
    request: GenerateImageRequest,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
) -> Any:
    """
    Generate marketing images
    
    Providers:
    - dalle: DALL-E 3 (best for product, clean designs)
    - flux: Flux 1.1 Pro (best for photorealistic)
    - flux_schnell: Faster, cheaper alternative
    """
    
    # Check usage limit
    if not current_user.can_generate("images"):
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail="Monthly limit reached for images. Please upgrade your plan."
        )
    
    # Get brand for context
    result = await db.execute(
        select(Brand).where(
            Brand.id == request.brand_id,
            Brand.user_id == current_user.id
        )
    )
    brand = result.scalar_one_or_none()
    
    if not brand:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Brand not found"
        )
    
    # Generate prompt if auto_generate_prompt is True
    if request.auto_generate_prompt and not request.prompt:
        from ...services.ai.image_generator import MarketingImagePrompts
        prompts = MarketingImagePrompts()
        
        brand_colors = []
        if brand.brand_colors:
            brand_colors = [
                brand.brand_colors.get("primary", "#000000"),
                brand.brand_colors.get("secondary", "#ffffff")
            ]
        
        if request.image_type == "product":
            # Use first product if available
            product_name = "product"
            product_desc = ""
            if brand.products and len(brand.products) > 0:
                product_name = brand.products[0].get("name", "product")
                product_desc = brand.products[0].get("description", "")
            
            prompt = prompts.product_showcase(
                product_name=product_name,
                product_description=product_desc,
                style=request.style
            )
        
        elif request.image_type == "social":
            prompt = prompts.social_media_post(
                theme=f"{brand.name} marketing",
                brand_colors=brand_colors,
                mood=request.style
            )
        
        elif request.image_type == "ads":
            product_name = brand.products[0].get("name", brand.name) if brand.products else brand.name
            prompt = prompts.ads_banner(
                product=product_name,
                style=request.style
            )
        
        else:
            prompt = f"Marketing image for {brand.name}, {brand.industry} industry, {request.style} style"
    else:
        prompt = request.prompt
    
    if not prompt:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Either prompt or auto_generate_prompt=True is required"
        )
    
    # Generate image
    try:
        generator = ImageGenerator()
        
        # Map aspect_ratio to size for DALL-E
        size_map = {
            "1:1": "1024x1024",
            "16:9": "1792x1024",
            "9:16": "1024x1792",
        }
        
        if request.provider == "dalle":
            result = generator.generate_dalle(
                prompt=prompt,
                size=size_map.get(request.aspect_ratio, "1024x1024")
            )
        elif request.provider == "flux":
            result = generator.generate_flux(
                prompt=prompt,
                aspect_ratio=request.aspect_ratio
            )
        elif request.provider == "flux_schnell":
            result = generator.generate_flux_schnell(
                prompt=prompt,
                aspect_ratio=request.aspect_ratio
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Unknown provider: {request.provider}"
            )
        
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Image generation failed: {str(e)}"
        )
    
    return {
        "success": True,
        "prompt_used": prompt,
        **result
    }


@router.post("/quick/{content_type}")
async def quick_generate(
    content_type: str,
    brand_id: UUID,
    topic: str = "",
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
) -> Any:
    """
    Quick generation with minimal parameters
    Just provide brand_id and topic, get content back
    """
    
    # Get brand
    result = await db.execute(
        select(Brand).where(
            Brand.id == brand_id,
            Brand.user_id == current_user.id
        )
    )
    brand = result.scalar_one_or_none()
    
    if not brand:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Brand not found"
        )
    
    # Use default product if available
    product_name = None
    if brand.products and len(brand.products) > 0:
        product_name = brand.products[0].get("name")
    
    # Create request with defaults
    request = GenerateRequest(
        brand_id=brand_id,
        content_type=content_type,
        topic=topic,
        product_name=product_name,
        num_variations=3
    )
    
    # Delegate to main generate endpoint
    from fastapi import BackgroundTasks
    return await generate_content(
        request=request,
        background_tasks=BackgroundTasks(),
        db=db,
        current_user=current_user
    )
