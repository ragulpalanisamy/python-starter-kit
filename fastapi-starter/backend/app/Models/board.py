from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field
from app.Models.base import PyObjectId, MongoBaseModel

class BoardModel(BaseModel):
    """Model for Board documents."""
    
    id: Optional[PyObjectId] = Field(default_factory=PyObjectId, alias="_id")
    board_id: int = Field(..., description="Unique board identifier")
    sanityId: Optional[str] = None
    name: str = Field(..., description="Board name")
    status: str = Field(default="ACTIVE", description="Board status")
    createdBy: Optional[int] = None
    updatedBy: Optional[int] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    class Config(MongoBaseModel):
        pass
