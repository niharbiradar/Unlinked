from pydantic import BaseModel, Field, ConfigDict, field_validator
from typing import List, Optional, Any
from datetime import datetime
from bson import ObjectId

class PostBase(BaseModel):
    """Base post model."""
    content: str = Field(..., min_length=1, max_length=2000)
    tags: List[str] = Field(default_factory=list)
    is_private: bool = Field(default=False)
    
    model_config = ConfigDict(
        json_encoders={ObjectId: str},
        populate_by_name=True
    )

class PostCreate(PostBase):
    """Model for creating a new post."""
    pass

class PostResponse(PostBase):
    """Model for post responses."""
    id: str = Field(alias="_id")
    created_at: datetime
    is_flagged: bool = False
    reaction_counts: dict = Field(default_factory=dict)
    
    @field_validator('id', mode='before')
    @classmethod
    def validate_object_id(cls, v):
        if isinstance(v, ObjectId):
            return str(v)
        if isinstance(v, str) and ObjectId.is_valid(v):
            return v
        raise ValueError("Invalid ObjectId")
    
    model_config = ConfigDict(
        json_encoders={ObjectId: str},
        populate_by_name=True
    ) 