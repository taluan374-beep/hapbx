"""
Content Management Endpoints
"""
from typing import Any, List, Optional
from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func

from ...database import get_db
from ...models import Content, Brand, User
from ...models.content import ContentStatus
from ...schemas.content import ContentCreate, ContentResponse, ContentListResponse
from ..deps import get_current_user

router = APIRouter()


@router.post("/", response_model=ContentResponse, status_code=status.HTTP_201_CREATED)
async def create_content(
    content_data: ContentCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
) -> Any:
    """Save generated content to database"""
    
    # Verify brand ownership
    result = await db.execute(
        select(Brand).where(
            Brand.id == content_data.brand_id,
            Brand.user_id == current_user.id
        )
    )
    brand = result.scalar_one_or_none()
    
    if not brand:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Brand not found"
        )
    
    content = Content(
        brand_id=content_data.brand_id,
        content_type=content_data.content_type,
        platform=content_data.platform,
        title=content_data.title,
        hook=content_data.hook,
        body=content_data.body,
        cta=content_data.cta,
        hashtags=content_data.hashtags,
        headlines=content_data.headlines,
        descriptions=content_data.descriptions,
        script_segments=content_data.script_segments,
        status=content_data.status
    )
    
    db.add(content)
    await db.commit()
    await db.refresh(content)
    
    return content


@router.get("/", response_model=ContentListResponse)
async def list_contents(
    brand_id: Optional[UUID] = None,
    content_type: Optional[str] = None,
    status: Optional[str] = None,
    page: int = Query(default=1, ge=1),
    page_size: int = Query(default=20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
) -> Any:
    """List contents with filtering and pagination"""
    
    # Build query
    query = select(Content).join(Brand).where(Brand.user_id == current_user.id)
    
    if brand_id:
        query = query.where(Content.brand_id == brand_id)
    if content_type:
        query = query.where(Content.content_type == content_type)
    if status:
        query = query.where(Content.status == status)
    
    # Get total count
    count_query = select(func.count()).select_from(query.subquery())
    total_result = await db.execute(count_query)
    total = total_result.scalar()
    
    # Apply pagination
    query = query.order_by(Content.created_at.desc())
    query = query.offset((page - 1) * page_size).limit(page_size)
    
    result = await db.execute(query)
    contents = result.scalars().all()
    
    return ContentListResponse(
        items=contents,
        total=total,
        page=page,
        page_size=page_size
    )


@router.get("/{content_id}", response_model=ContentResponse)
async def get_content(
    content_id: UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
) -> Any:
    """Get a specific content"""
    
    result = await db.execute(
        select(Content)
        .join(Brand)
        .where(Content.id == content_id, Brand.user_id == current_user.id)
    )
    content = result.scalar_one_or_none()
    
    if not content:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Content not found"
        )
    
    return content


@router.put("/{content_id}", response_model=ContentResponse)
async def update_content(
    content_id: UUID,
    content_data: ContentCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
) -> Any:
    """Update content"""
    
    result = await db.execute(
        select(Content)
        .join(Brand)
        .where(Content.id == content_id, Brand.user_id == current_user.id)
    )
    content = result.scalar_one_or_none()
    
    if not content:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Content not found"
        )
    
    # Update fields
    for field, value in content_data.model_dump(exclude_unset=True).items():
        setattr(content, field, value)
    
    await db.commit()
    await db.refresh(content)
    
    return content


@router.delete("/{content_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_content(
    content_id: UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
) -> None:
    """Delete content"""
    
    result = await db.execute(
        select(Content)
        .join(Brand)
        .where(Content.id == content_id, Brand.user_id == current_user.id)
    )
    content = result.scalar_one_or_none()
    
    if not content:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Content not found"
        )
    
    await db.delete(content)
    await db.commit()


@router.patch("/{content_id}/status")
async def update_content_status(
    content_id: UUID,
    new_status: str,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
) -> Any:
    """Update content status"""
    
    # Validate status
    valid_statuses = [s.value for s in ContentStatus]
    if new_status not in valid_statuses:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Invalid status. Must be one of: {valid_statuses}"
        )
    
    result = await db.execute(
        select(Content)
        .join(Brand)
        .where(Content.id == content_id, Brand.user_id == current_user.id)
    )
    content = result.scalar_one_or_none()
    
    if not content:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Content not found"
        )
    
    content.status = new_status
    await db.commit()
    
    return {"id": str(content_id), "status": new_status}


@router.post("/{content_id}/duplicate", response_model=ContentResponse)
async def duplicate_content(
    content_id: UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
) -> Any:
    """Duplicate content"""
    
    result = await db.execute(
        select(Content)
        .join(Brand)
        .where(Content.id == content_id, Brand.user_id == current_user.id)
    )
    original = result.scalar_one_or_none()
    
    if not original:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Content not found"
        )
    
    # Create duplicate
    duplicate = Content(
        brand_id=original.brand_id,
        content_type=original.content_type,
        platform=original.platform,
        title=f"{original.title} (Copy)" if original.title else None,
        hook=original.hook,
        body=original.body,
        cta=original.cta,
        hashtags=original.hashtags,
        headlines=original.headlines,
        descriptions=original.descriptions,
        script_segments=original.script_segments,
        status=ContentStatus.DRAFT
    )
    
    db.add(duplicate)
    await db.commit()
    await db.refresh(duplicate)
    
    return duplicate
