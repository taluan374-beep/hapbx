"""
User Schemas
"""
from pydantic import BaseModel, EmailStr, Field
from typing import Optional, Dict, Any
from uuid import UUID
from datetime import datetime


class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=8)
    full_name: Optional[str] = None
    company_name: Optional[str] = None


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: UUID
    email: str
    full_name: Optional[str]
    company_name: Optional[str]
    subscription_tier: str
    usage_this_month: Optional[Dict[str, Any]]
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True


class UserUpdate(BaseModel):
    full_name: Optional[str] = None
    company_name: Optional[str] = None
    phone: Optional[str] = None


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
    expires_in: int
    user: UserResponse


class UsageStats(BaseModel):
    social_posts: int = 0
    ads_copies: int = 0
    landing_pages: int = 0
    video_scripts: int = 0
    images: int = 0
    
    social_posts_limit: int = 10
    ads_copies_limit: int = 5
    landing_pages_limit: int = 1
    video_scripts_limit: int = 2
    images_limit: int = 5
