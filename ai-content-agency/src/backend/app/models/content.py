"""
Content Model - Nội dung được tạo
"""
from sqlalchemy import Column, String, Text, JSON, DateTime, ForeignKey, Enum, ARRAY
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import uuid
import enum

from ..database import Base


class ContentType(str, enum.Enum):
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


class ContentStatus(str, enum.Enum):
    DRAFT = "draft"
    PENDING_REVIEW = "pending_review"
    APPROVED = "approved"
    SCHEDULED = "scheduled"
    PUBLISHED = "published"
    ARCHIVED = "archived"


class Content(Base):
    __tablename__ = "contents"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    brand_id = Column(UUID(as_uuid=True), ForeignKey("brands.id"), nullable=False)
    
    # Content Type & Platform
    content_type = Column(Enum(ContentType), nullable=False)
    platform = Column(String(50))  # facebook, instagram, tiktok, google, website
    
    # Content Data
    title = Column(String(500))
    hook = Column(Text)  # First line / attention grabber
    body = Column(Text)
    cta = Column(String(500))  # Call to action
    
    # Media
    media_urls = Column(JSON)  # ["url1", "url2"]
    image_prompts = Column(JSON)  # AI image generation prompts used
    
    # Social specific
    hashtags = Column(ARRAY(String))
    
    # Ads specific
    headlines = Column(JSON)  # Multiple headline variations
    descriptions = Column(JSON)  # Multiple description variations
    
    # Video specific
    script_segments = Column(JSON)
    # [
    #   {"timestamp": "0-3s", "type": "hook", "text": "...", "visual": "..."},
    #   ...
    # ]
    
    # Status & Scheduling
    status = Column(Enum(ContentStatus), default=ContentStatus.DRAFT)
    scheduled_at = Column(DateTime(timezone=True))
    published_at = Column(DateTime(timezone=True))
    
    # Performance (populated after publishing)
    performance_metrics = Column(JSON)
    # {
    #   "impressions": 1000,
    #   "engagement": 50,
    #   "clicks": 30,
    #   "conversions": 5
    # }
    
    # AI Generation metadata
    generation_params = Column(JSON)  # Parameters used for generation
    ai_model_used = Column(String(100))  # gpt-4o, claude-3-5-sonnet, etc.
    tokens_used = Column(JSON)  # {"input": 500, "output": 1000}
    
    # Metadata
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relationships
    brand = relationship("Brand", back_populates="contents")
    versions = relationship("ContentVersion", back_populates="content", cascade="all, delete-orphan")


class ContentVersion(Base):
    """Store multiple versions for A/B testing"""
    __tablename__ = "content_versions"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    content_id = Column(UUID(as_uuid=True), ForeignKey("contents.id"), nullable=False)
    
    version_name = Column(String(50))  # "Version A", "Version B"
    body = Column(Text)
    hook = Column(Text)
    cta = Column(String(500))
    
    # Performance for this version
    performance_score = Column(JSON)
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Relationships
    content = relationship("Content", back_populates="versions")
