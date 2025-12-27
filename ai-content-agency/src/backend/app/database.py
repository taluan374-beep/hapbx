"""
Database Configuration
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

from .config import settings

# Sync engine (for Alembic migrations)
SYNC_DATABASE_URL = settings.DATABASE_URL.replace("postgresql://", "postgresql+psycopg2://")
sync_engine = create_engine(SYNC_DATABASE_URL)

# Async engine (for FastAPI)
ASYNC_DATABASE_URL = settings.DATABASE_URL.replace("postgresql://", "postgresql+asyncpg://")
async_engine = create_async_engine(ASYNC_DATABASE_URL, echo=settings.DEBUG)

# Session
AsyncSessionLocal = sessionmaker(
    async_engine, 
    class_=AsyncSession, 
    expire_on_commit=False
)

# Base for models
Base = declarative_base()


async def get_db():
    """Dependency to get database session"""
    async with AsyncSessionLocal() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()


async def init_db():
    """Initialize database tables"""
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
