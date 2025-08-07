from pydantic import BaseModel, Field, ConfigDict, field_validator
from typing import Literal
from bson import ObjectId

class ReactionBase(BaseModel):
    """Base reaction model."""
    post_id: str
    reaction_type: Literal["same", "helpful", "upvote"]
    
    @field_validator('post_id', mode='before')
    @classmethod
    def validate_object_id(cls, v):
        if isinstance(v, ObjectId):
            return str(v)
        if isinstance(v, str) and ObjectId.is_valid(v):
            return v
        raise ValueError("Invalid ObjectId")
    
    model_config = ConfigDict(
        json_encoders={ObjectId: str}
    )

class ReactionCreate(ReactionBase):
    """Model for creating a new reaction."""
    pass

class ReactionResponse(ReactionBase):
    """Model for reaction responses."""
    id: str = Field(alias="_id")
    
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