from typing import Optional
from pydantic import BaseModel, Field
from app.Models.base import PyObjectId, MongoBaseModel

class UserModel(BaseModel):
    """Model for MFlix User documents."""
    
    id: Optional[PyObjectId] = Field(default_factory=PyObjectId, alias="_id")
    name: str = Field(..., description="User's full name")
    email: str = Field(..., description="User's email address")
    password: str = Field(..., description="Hashed password")

    class Config(MongoBaseModel):
        pass
