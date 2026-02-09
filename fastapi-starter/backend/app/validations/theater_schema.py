from typing import Optional, Dict, Any
from pydantic import BaseModel, Field

class TheaterLocationSchema(BaseModel):
    """Theater location validation."""
    address: Dict[str, str]
    geo: Dict[str, Any]

class TheaterCreate(BaseModel):
    """Schema for creating a theater."""
    theaterId: int = Field(..., ge=1)
    location: TheaterLocationSchema

class TheaterUpdate(BaseModel):
    """Schema for updating a theater."""
    theaterId: Optional[int] = None
    location: Optional[TheaterLocationSchema] = None
