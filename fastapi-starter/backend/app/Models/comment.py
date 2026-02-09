from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field
from app.Models.base import PyObjectId, MongoBaseModel

class CommentModel(BaseModel):
    """Model for MFlix Comment documents."""
    
    id: Optional[PyObjectId] = Field(default_factory=PyObjectId, alias="_id")
    name: str = Field(..., description="Name of the commenter")
    email: str = Field(..., description="Email of the commenter")
    movie_id: PyObjectId = Field(..., description="Reference to the Movie ID")
    text: str = Field(..., description="The comment text")
    date: datetime = Field(default_factory=datetime.utcnow)

    class Config(MongoBaseModel):
        pass
