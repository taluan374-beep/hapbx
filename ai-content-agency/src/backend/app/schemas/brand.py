"""
Brand Schemas
"""
from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any
from uuid import UUID
from datetime import datetime


class TargetAudience(BaseModel):
    age_range: Optional[str] = "25-45"
    gender: Optional[str] = "all"
    location: Optional[str] = "Vietnam"
    income_level: Optional[str] = None
    interests: Optional[List[str]] = []
    pain_points: Optional[List[str]] = []
    desires: Optional[List[str]] = []


class Product(BaseModel):
    name: str
    description: Optional[str] = None
    price: Optional[float] = None
    features: Optional[List[str]] = []
    benefits: Optional[List[str]] = []
    images: Optional[List[str]] = []


class BrandColors(BaseModel):
    primary: Optional[str] = "#000000"
    secondary: Optional[str] = "#ffffff"
    accent: Optional[str] = None


class BrandCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=255)
    industry: str = Field(..., min_length=1, max_length=100)
    description: Optional[str] = None
    slogan: Optional[str] = None
    
    tone_of_voice: str = Field(default="professional")  # professional, friendly, playful, luxury
    language_style: str = Field(default="formal")  # formal, casual, trendy
    core_values: Optional[List[str]] = []
    usp: Optional[str] = None
    
    target_audience: Optional[TargetAudience] = None
    brand_colors: Optional[BrandColors] = None
    logo_url: Optional[str] = None
    
    competitors: Optional[List[str]] = []
    banned_words: Optional[List[str]] = []
    must_mention: Optional[List[str]] = []
    hashtags: Optional[List[str]] = []
    
    products: Optional[List[Product]] = []

    class Config:
        json_schema_extra = {
            "example": {
                "name": "Beauty Lab",
                "industry": "beauty",
                "description": "Thương hiệu skincare cao cấp cho phụ nữ hiện đại",
                "slogan": "Vẻ đẹp từ bên trong",
                "tone_of_voice": "professional",
                "language_style": "formal",
                "core_values": ["innovation", "quality", "natural"],
                "usp": "Công nghệ peptide độc quyền giúp trẻ hóa da sau 14 ngày",
                "target_audience": {
                    "age_range": "25-40",
                    "gender": "female",
                    "location": "Vietnam",
                    "pain_points": ["da nhăn", "thiếu độ ẩm"],
                    "desires": ["da căng mịn", "trẻ trung"]
                },
                "products": [
                    {
                        "name": "Peptide Serum",
                        "description": "Serum chống lão hóa với 5% peptide",
                        "price": 890000,
                        "features": ["5% peptide", "Vitamin C"],
                        "benefits": ["Giảm nếp nhăn", "Sáng da"]
                    }
                ]
            }
        }


class BrandUpdate(BaseModel):
    name: Optional[str] = None
    industry: Optional[str] = None
    description: Optional[str] = None
    slogan: Optional[str] = None
    tone_of_voice: Optional[str] = None
    language_style: Optional[str] = None
    core_values: Optional[List[str]] = None
    usp: Optional[str] = None
    target_audience: Optional[TargetAudience] = None
    brand_colors: Optional[BrandColors] = None
    logo_url: Optional[str] = None
    competitors: Optional[List[str]] = None
    banned_words: Optional[List[str]] = None
    must_mention: Optional[List[str]] = None
    hashtags: Optional[List[str]] = None
    products: Optional[List[Product]] = None


class BrandResponse(BaseModel):
    id: UUID
    user_id: UUID
    name: str
    industry: Optional[str]
    description: Optional[str]
    slogan: Optional[str]
    tone_of_voice: Optional[str]
    language_style: Optional[str]
    core_values: Optional[List[str]]
    usp: Optional[str]
    target_audience: Optional[Dict[str, Any]]
    brand_colors: Optional[Dict[str, Any]]
    logo_url: Optional[str]
    products: Optional[List[Dict[str, Any]]]
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        from_attributes = True
