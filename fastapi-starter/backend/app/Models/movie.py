from typing import Optional, List, Dict, Any
from datetime import datetime
from pydantic import BaseModel, Field
from app.Models.base import PyObjectId, MongoBaseModel

class MovieModel(BaseModel):
    """Model for MFlix Movie documents."""
    
    id: Optional[PyObjectId] = Field(default_factory=PyObjectId, alias="_id")
    title: str = Field(..., description="The title of the movie")
    year: int = Field(..., description="Release year")
    plot: Optional[str] = Field(None, description="Short summary of the plot")
    fullplot: Optional[str] = Field(None, description="Detailed plot description")
    genres: List[str] = Field(default_factory=list)
    runtime: Optional[int] = Field(None, description="Runtime in minutes")
    rated: Optional[str] = Field(None, description="Rating (R, PG, etc)")
    cast: List[str] = Field(default_factory=list)
    poster: Optional[str] = Field(None, description="URL to the poster image")
    languages: List[str] = Field(default_factory=list)
    released: Optional[datetime] = None
    directors: List[str] = Field(default_factory=list)
    writers: List[str] = Field(default_factory=list)
    countries: List[str] = Field(default_factory=list)
    awards: Dict[str, Any] = Field(default_factory=dict)
    imdb: Dict[str, Any] = Field(default_factory=dict)
    tomatoes: Optional[Dict[str, Any]] = None
    type: str = Field(default="movie")
    num_mflix_comments: int = Field(default=0)
    lastupdated: Optional[str] = None

    class Config(MongoBaseModel):
        pass
