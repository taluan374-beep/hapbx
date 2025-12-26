"""
Content Schemas
"""
from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any, Literal
from uuid import UUID
from datetime import datetime
from enum import Enum


class ContentTypeEnum(str, Enum):
    SOCIAL_FACEBOOK = "social_facebook"
    SOCIAL_INSTAGRAM = "social_instagram"
    SOCIAL_TIKTOK = "social_tiktok"
    SOCIAL_LINKEDIN = "social_linkedin"
    ADS_FACEBOOK = "ads_facebook"
    ADS_GOOGLE = "ads_google"
    ADS_TIKTOK = "ads_tiktok"
    LANDING_PAGE = "landing_page"
    VIDEO_SCRIPT = "video_script"
    EMAIL = "email"


class ContentStatusEnum(str, Enum):
    DRAFT = "draft"
    PENDING_REVIEW = "pending_review"
    APPROVED = "approved"
    SCHEDULED = "scheduled"
    PUBLISHED = "published"


# Request Schemas
class GenerateRequest(BaseModel):
    """Request to generate content"""
    brand_id: UUID
    content_type: ContentTypeEnum
    
    # Common params
    topic: Optional[str] = None
    product_name: Optional[str] = None
    objective: Optional[str] = "engagement"  # awareness, engagement, conversion
    key_message: Optional[str] = None
    promotion: Optional[str] = None
    
    # Quantity
    num_variations: int = Field(default=3, ge=1, le=10)
    
    # Social specific
    body_length: Optional[str] = "medium"  # short, medium, long
    include_hashtags: bool = True
    
    # Ads specific
    landing_url: Optional[str] = None
    offer: Optional[str] = None
    
    # Video specific
    duration: Optional[int] = 30  # seconds
    video_style: Optional[str] = "talking_head"  # talking_head, voiceover, text_overlay
    
    # AI settings
    ai_provider: str = Field(default="openai")  # openai, anthropic
    temperature: float = Field(default=0.7, ge=0, le=1)
    
    class Config:
        json_schema_extra = {
            "example": {
                "brand_id": "123e4567-e89b-12d3-a456-426614174000",
                "content_type": "social_facebook",
                "topic": "Ra mắt sản phẩm mới",
                "product_name": "Peptide Serum",
                "objective": "conversion",
                "key_message": "Giảm nếp nhăn sau 14 ngày",
                "promotion": "Giảm 30% tuần này",
                "num_variations": 3,
                "body_length": "medium",
                "include_hashtags": True
            }
        }


class GenerateImageRequest(BaseModel):
    """Request to generate image"""
    brand_id: UUID
    prompt: Optional[str] = None
    auto_generate_prompt: bool = True  # Auto create prompt from brand context
    
    image_type: str = "product"  # product, social, ads, banner
    style: str = "modern"  # modern, minimal, luxury, playful
    aspect_ratio: str = "1:1"  # 1:1, 16:9, 9:16, 4:5
    
    provider: str = "dalle"  # dalle, flux, midjourney


# Response Schemas
class GeneratedContent(BaseModel):
    """A single generated content piece"""
    hook: Optional[str] = None
    body: str
    cta: Optional[str] = None
    hashtags: Optional[List[str]] = []
    
    # For ads
    headlines: Optional[List[str]] = []
    descriptions: Optional[List[str]] = []
    
    # For video
    script_segments: Optional[List[Dict[str, Any]]] = []
    
    # Suggestions
    image_suggestion: Optional[str] = None
    best_posting_time: Optional[str] = None


class GenerateResponse(BaseModel):
    """Response from content generation"""
    success: bool
    content_type: str
    brand_name: str
    variations: List[GeneratedContent]
    
    # Metadata
    ai_model_used: str
    tokens_used: Dict[str, int]
    generation_time_seconds: float
    
    # Saved content IDs (if auto-saved)
    saved_content_ids: Optional[List[UUID]] = []


class ContentCreate(BaseModel):
    brand_id: UUID
    content_type: ContentTypeEnum
    platform: Optional[str] = None
    title: Optional[str] = None
    hook: Optional[str] = None
    body: str
    cta: Optional[str] = None
    hashtags: Optional[List[str]] = []
    headlines: Optional[List[str]] = []
    descriptions: Optional[List[str]] = []
    script_segments: Optional[List[Dict[str, Any]]] = []
    status: ContentStatusEnum = ContentStatusEnum.DRAFT


class ContentResponse(BaseModel):
    id: UUID
    brand_id: UUID
    content_type: str
    platform: Optional[str]
    title: Optional[str]
    hook: Optional[str]
    body: Optional[str]
    cta: Optional[str]
    hashtags: Optional[List[str]]
    status: str
    scheduled_at: Optional[datetime]
    created_at: datetime
    
    class Config:
        from_attributes = True


class ContentListResponse(BaseModel):
    items: List[ContentResponse]
    total: int
    page: int
    page_size: int
