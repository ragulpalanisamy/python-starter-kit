from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class BoardCreate(BaseModel):
    board_id: int = Field(..., description="Unique board identifier")
    sanityId: Optional[str] = None
    name: str = Field(..., min_length=1, max_length=100)
    status: str = Field(default="ACTIVE")
    createdBy: Optional[int] = None

class BoardUpdate(BaseModel):
    name: Optional[str] = None
    status: Optional[str] = None
    updatedBy: Optional[int] = None

class BoardResponse(BaseModel):
    board_id: int
    sanityId: Optional[str]
    name: str
    status: str
    createdBy: Optional[int]
    updatedBy: Optional[int]
    created_at: datetime
    updated_at: datetime
