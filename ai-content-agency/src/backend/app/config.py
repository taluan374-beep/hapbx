"""
Application Configuration
"""
from pydantic_settings import BaseSettings
from functools import lru_cache
from typing import Optional


class Settings(BaseSettings):
    # App
    APP_NAME: str = "AI Content Agency"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = False
    
    # Database
    DATABASE_URL: str = "postgresql://postgres:postgres@localhost:5432/ai_agency"
    
    # Redis
    REDIS_URL: str = "redis://localhost:6379/0"
    
    # AI Services
    OPENAI_API_KEY: str = ""
    ANTHROPIC_API_KEY: str = ""
    REPLICATE_API_TOKEN: str = ""
    
    # HeyGen (Video)
    HEYGEN_API_KEY: str = ""
    
    # ElevenLabs (Voice)
    ELEVENLABS_API_KEY: str = ""
    
    # Storage (S3/R2)
    AWS_ACCESS_KEY_ID: str = ""
    AWS_SECRET_ACCESS_KEY: str = ""
    S3_BUCKET_NAME: str = "ai-agency-assets"
    S3_REGION: str = "ap-southeast-1"
    
    # Supabase Auth
    SUPABASE_URL: str = ""
    SUPABASE_ANON_KEY: str = ""
    SUPABASE_SERVICE_KEY: str = ""
    
    # JWT
    JWT_SECRET_KEY: str = "your-secret-key-change-in-production"
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    class Config:
        env_file = ".env"
        case_sensitive = True


@lru_cache()
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
