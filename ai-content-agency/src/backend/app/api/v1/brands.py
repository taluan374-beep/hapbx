"""
Brand Management Endpoints
"""
from typing import Any, List
from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from ...database import get_db
from ...models import Brand, User
from ...schemas.brand import BrandCreate, BrandUpdate, BrandResponse
from ..deps import get_current_user

router = APIRouter()


@router.post("/", response_model=BrandResponse, status_code=status.HTTP_201_CREATED)
async def create_brand(
    brand_data: BrandCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
) -> Any:
    """Create a new brand"""
    
    brand = Brand(
        user_id=current_user.id,
        name=brand_data.name,
        industry=brand_data.industry,
        description=brand_data.description,
        slogan=brand_data.slogan,
        tone_of_voice=brand_data.tone_of_voice,
        language_style=brand_data.language_style,
        core_values=brand_data.core_values,
        usp=brand_data.usp,
        target_audience=brand_data.target_audience.model_dump() if brand_data.target_audience else None,
        brand_colors=brand_data.brand_colors.model_dump() if brand_data.brand_colors else None,
        logo_url=brand_data.logo_url,
        competitors=brand_data.competitors,
        banned_words=brand_data.banned_words,
        must_mention=brand_data.must_mention,
        hashtags=brand_data.hashtags,
        products=[p.model_dump() for p in brand_data.products] if brand_data.products else None
    )
    
    db.add(brand)
    await db.commit()
    await db.refresh(brand)
    
    return brand


@router.get("/", response_model=List[BrandResponse])
async def list_brands(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
) -> Any:
    """List all brands for current user"""
    
    result = await db.execute(
        select(Brand).where(Brand.user_id == current_user.id).order_by(Brand.created_at.desc())
    )
    brands = result.scalars().all()
    
    return brands


@router.get("/{brand_id}", response_model=BrandResponse)
async def get_brand(
    brand_id: UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
) -> Any:
    """Get a specific brand"""
    
    result = await db.execute(
        select(Brand).where(Brand.id == brand_id, Brand.user_id == current_user.id)
    )
    brand = result.scalar_one_or_none()
    
    if not brand:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Brand not found"
        )
    
    return brand


@router.put("/{brand_id}", response_model=BrandResponse)
async def update_brand(
    brand_id: UUID,
    brand_data: BrandUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
) -> Any:
    """Update a brand"""
    
    result = await db.execute(
        select(Brand).where(Brand.id == brand_id, Brand.user_id == current_user.id)
    )
    brand = result.scalar_one_or_none()
    
    if not brand:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Brand not found"
        )
    
    # Update fields
    update_data = brand_data.model_dump(exclude_unset=True)
    
    for field, value in update_data.items():
        if value is not None:
            if field == "target_audience" and hasattr(value, "model_dump"):
                value = value.model_dump()
            elif field == "brand_colors" and hasattr(value, "model_dump"):
                value = value.model_dump()
            elif field == "products" and isinstance(value, list):
                value = [p.model_dump() if hasattr(p, "model_dump") else p for p in value]
            setattr(brand, field, value)
    
    await db.commit()
    await db.refresh(brand)
    
    return brand


@router.delete("/{brand_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_brand(
    brand_id: UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
) -> None:
    """Delete a brand"""
    
    result = await db.execute(
        select(Brand).where(Brand.id == brand_id, Brand.user_id == current_user.id)
    )
    brand = result.scalar_one_or_none()
    
    if not brand:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Brand not found"
        )
    
    await db.delete(brand)
    await db.commit()


@router.get("/{brand_id}/context", response_model=dict)
async def get_brand_context(
    brand_id: UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
) -> Any:
    """Get brand context string for AI prompts"""
    
    result = await db.execute(
        select(Brand).where(Brand.id == brand_id, Brand.user_id == current_user.id)
    )
    brand = result.scalar_one_or_none()
    
    if not brand:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Brand not found"
        )
    
    return {
        "brand_id": str(brand.id),
        "brand_name": brand.name,
        "context": brand.to_context_string()
    }
