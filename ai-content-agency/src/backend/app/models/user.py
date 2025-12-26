"""
User Model
"""
from sqlalchemy import Column, String, Boolean, DateTime, JSON
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import uuid

from ..database import Base


class User(Base):
    __tablename__ = "users"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    
    # Auth
    email = Column(String(255), unique=True, nullable=False, index=True)
    hashed_password = Column(String(255))
    
    # Profile
    full_name = Column(String(255))
    company_name = Column(String(255))
    phone = Column(String(50))
    
    # Subscription
    subscription_tier = Column(String(50), default="free")  # free, starter, growth, scale
    subscription_status = Column(String(50), default="active")  # active, cancelled, expired
    subscription_end_date = Column(DateTime(timezone=True))
    
    # Usage tracking
    usage_this_month = Column(JSON, default={
        "social_posts": 0,
        "ads_copies": 0,
        "landing_pages": 0,
        "video_scripts": 0,
        "images": 0
    })
    
    # Settings
    settings = Column(JSON, default={})
    
    # Status
    is_active = Column(Boolean, default=True)
    is_verified = Column(Boolean, default=False)
    
    # Metadata
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    last_login = Column(DateTime(timezone=True))
    
    # Relationships
    brands = relationship("Brand", back_populates="user", cascade="all, delete-orphan")
    
    @property
    def usage_limits(self) -> dict:
        """Get usage limits based on subscription tier"""
        limits = {
            "free": {
                "social_posts": 10,
                "ads_copies": 5,
                "landing_pages": 1,
                "video_scripts": 2,
                "images": 5
            },
            "starter": {
                "social_posts": 30,
                "ads_copies": 10,
                "landing_pages": 2,
                "video_scripts": 5,
                "images": 10
            },
            "growth": {
                "social_posts": 60,
                "ads_copies": 30,
                "landing_pages": 5,
                "video_scripts": 10,
                "images": 20
            },
            "scale": {
                "social_posts": -1,  # unlimited
                "ads_copies": -1,
                "landing_pages": 10,
                "video_scripts": 20,
                "images": 50
            }
        }
        return limits.get(self.subscription_tier, limits["free"])
    
    def can_generate(self, content_type: str) -> bool:
        """Check if user can generate more content"""
        limits = self.usage_limits
        usage = self.usage_this_month or {}
        
        limit = limits.get(content_type, 0)
        current = usage.get(content_type, 0)
        
        if limit == -1:  # unlimited
            return True
        return current < limit
