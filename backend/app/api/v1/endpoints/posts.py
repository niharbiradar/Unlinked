from fastapi import APIRouter, HTTPException, Depends, Query
from typing import List, Optional
from datetime import datetime, UTC
from bson import ObjectId
import logging

from ....models.post import PostCreate, PostResponse
from ....database import database
from ....config import settings

logger = logging.getLogger(__name__)
router = APIRouter()

@router.post("/", response_model=PostResponse)
async def create_post(post: PostCreate):
    """Create a new anonymous post."""
    collection = database.get_collection("posts")
    
    # Validate content length
    if len(post.content) > settings.MAX_CONTENT_LENGTH:
        raise HTTPException(
            status_code=400, 
            detail=f"Content too long. Maximum {settings.MAX_CONTENT_LENGTH} characters allowed."
        )
    
    # Validate number of tags
    if len(post.tags) > settings.MAX_TAGS_PER_POST:
        raise HTTPException(
            status_code=400,
            detail=f"Too many tags. Maximum {settings.MAX_TAGS_PER_POST} tags allowed."
        )
    
    post_data = post.model_dump()
    post_data["created_at"] = datetime.now(UTC)
    post_data["is_flagged"] = False
    post_data["reaction_counts"] = {"same": 0, "helpful": 0, "upvote": 0}
    
    try:
        result = await collection.insert_one(post_data)
        post_data["_id"] = str(result.inserted_id)
        return PostResponse(**post_data)
    except Exception as e:
        logger.error(f"Error creating post: {e}")
        raise HTTPException(status_code=500, detail="Failed to create post")

@router.get("/", response_model=List[PostResponse])
async def get_posts(
    skip: int = Query(0, ge=0, description="Number of posts to skip"),
    limit: int = Query(settings.DEFAULT_PAGE_SIZE, ge=1, le=settings.MAX_PAGE_SIZE, description="Number of posts to return"),
    tag: Optional[str] = Query(None, description="Filter by tag")
):
    """Get posts (chronological order, excluding private posts)."""
    try:
        collection = database.get_collection("posts")
        
        # Build query
        query = {"is_private": False}
        if tag:
            # Sanitize tag input
            tag = tag.strip().lower()
            if len(tag) > 50:  # Reasonable tag length limit
                raise HTTPException(status_code=400, detail="Tag too long")
            query["tags"] = tag
        
        cursor = collection.find(query).sort("created_at", -1).skip(skip).limit(limit)
        posts = await cursor.to_list(length=limit)
        
        # Convert ObjectIds to strings for Pydantic
        for post in posts:
            post["_id"] = str(post["_id"])
        
        return [PostResponse(**post) for post in posts]
    except Exception as e:
        logger.error(f"Error retrieving posts: {e}")
        raise HTTPException(status_code=500, detail=f"Failed to retrieve posts: {str(e)}")

@router.get("/{post_id}", response_model=PostResponse)
async def get_post(post_id: str):
    """Get a specific post by ID."""
    collection = database.get_collection("posts")
    
    # Validate post_id format
    if not post_id or len(post_id) != 24:
        raise HTTPException(status_code=400, detail="Invalid post ID format")
    
    try:
        post = await collection.find_one({"_id": ObjectId(post_id)})
        if not post:
            raise HTTPException(status_code=404, detail="Post not found")
        
        # Convert ObjectId to string for Pydantic
        post["_id"] = str(post["_id"])
        return PostResponse(**post)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid post ID")
    except Exception as e:
        logger.error(f"Error retrieving post {post_id}: {e}")
        raise HTTPException(status_code=500, detail="Failed to retrieve post") 