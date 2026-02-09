from typing import Optional
from pydantic import BaseModel, Field

class CommentCreate(BaseModel):
    """Schema for creating a comment."""
    name: str = Field(..., min_length=1)
    email: str = Field(..., pattern=r"^\S+@\S+\.\S+$")
    movie_id: str = Field(..., description="The ID of the movie this comment belongs to")
    text: str = Field(..., min_length=1)

class CommentUpdate(BaseModel):
    """Schema for updating a comment."""
    text: Optional[str] = Field(None, min_length=1)
