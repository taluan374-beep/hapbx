"""
Brand Model - Thông tin thương hiệu của khách hàng
"""
from sqlalchemy import Column, String, Text, JSON, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import uuid

from ..database import Base


class Brand(Base):
    __tablename__ = "brands"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    
    # Basic Info
    name = Column(String(255), nullable=False)
    industry = Column(String(100))  # fnb, beauty, education, realestate, etc.
    description = Column(Text)
    slogan = Column(String(500))
    
    # Brand Identity
    tone_of_voice = Column(String(50))  # professional, friendly, playful, luxury
    language_style = Column(String(50))  # formal, casual, trendy
    core_values = Column(JSON)  # ["innovation", "quality", "trust"]
    usp = Column(Text)  # Unique Selling Proposition
    
    # Target Audience
    target_audience = Column(JSON)
    # {
    #   "age_range": "25-40",
    #   "gender": "all",
    #   "location": "Vietnam",
    #   "income_level": "middle-high",
    #   "interests": ["beauty", "skincare"],
    #   "pain_points": ["da nhạy cảm", "thiếu thời gian"],
    #   "desires": ["da đẹp", "tự tin"]
    # }
    
    # Visual Identity
    brand_colors = Column(JSON)  # {"primary": "#FF5733", "secondary": "#333"}
    logo_url = Column(String(500))
    brand_assets = Column(JSON)  # URLs to brand assets
    
    # Competitors
    competitors = Column(JSON)  # ["competitor1", "competitor2"]
    
    # Content Guidelines
    banned_words = Column(JSON)  # Words to avoid
    must_mention = Column(JSON)  # Must include phrases
    hashtags = Column(JSON)  # Branded hashtags
    
    # Products/Services
    products = Column(JSON)
    # [
    #   {
    #     "name": "Product A",
    #     "description": "...",
    #     "price": 500000,
    #     "features": ["feature1", "feature2"],
    #     "benefits": ["benefit1", "benefit2"]
    #   }
    # ]
    
    # Metadata
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relationships
    user = relationship("User", back_populates="brands")
    contents = relationship("Content", back_populates="brand", cascade="all, delete-orphan")
    
    def to_context_string(self) -> str:
        """Convert brand to context string for AI prompts"""
        context = f"""
## BRAND CONTEXT
- Tên thương hiệu: {self.name}
- Ngành: {self.industry}
- Slogan: {self.slogan or 'N/A'}
- USP: {self.usp or 'N/A'}
- Giá trị cốt lõi: {', '.join(self.core_values or [])}

## TONE OF VOICE
- Style: {self.tone_of_voice}
- Ngôn ngữ: {self.language_style}

## TARGET AUDIENCE
"""
        if self.target_audience:
            ta = self.target_audience
            context += f"""- Độ tuổi: {ta.get('age_range', 'N/A')}
- Giới tính: {ta.get('gender', 'N/A')}
- Vị trí: {ta.get('location', 'N/A')}
- Pain points: {', '.join(ta.get('pain_points', []))}
- Mong muốn: {', '.join(ta.get('desires', []))}
"""
        
        if self.products:
            context += "\n## SẢN PHẨM/DỊCH VỤ\n"
            for p in self.products[:5]:  # Limit to 5 products
                context += f"- {p.get('name')}: {p.get('description', '')}\n"
        
        if self.banned_words:
            context += f"\n## KHÔNG DÙNG CÁC TỪ: {', '.join(self.banned_words)}\n"
        
        return context
