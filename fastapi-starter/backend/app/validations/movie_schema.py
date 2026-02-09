from typing import Optional, List, Dict, Any
from datetime import datetime
from pydantic import BaseModel, Field

class MovieCreate(BaseModel):
    """Schema for creating a movie."""
    title: str = Field(..., min_length=1, description="The title of the movie")
    year: int = Field(..., ge=1800, le=2100, description="Release year")
    plot: Optional[str] = None
    fullplot: Optional[str] = None
    genres: List[str] = Field(default_factory=list)
    runtime: Optional[int] = Field(None, ge=1)
    rated: Optional[str] = None
    cast: List[str] = Field(default_factory=list)
    poster: Optional[str] = None
    languages: List[str] = Field(default_factory=list)
    released: Optional[datetime] = None
    directors: List[str] = Field(default_factory=list)
    writers: List[str] = Field(default_factory=list)
    countries: List[str] = Field(default_factory=list)
    awards: Dict[str, Any] = Field(default_factory=dict)
    imdb: Dict[str, Any] = Field(default_factory=dict)
    type: str = "movie"

class MovieUpdate(BaseModel):
    """Schema for updating a movie."""
    title: Optional[str] = None
    year: Optional[int] = None
    plot: Optional[str] = None
    fullplot: Optional[str] = None
    genres: Optional[List[str]] = None
    runtime: Optional[int] = None
    rated: Optional[str] = None
    cast: Optional[List[str]] = None
    poster: Optional[str] = None
    languages: Optional[List[str]] = None
    released: Optional[datetime] = None
    directors: Optional[List[str]] = None
    writers: Optional[List[str]] = None
    countries: Optional[List[str]] = None
    awards: Optional[Dict[str, Any]] = None
    imdb: Optional[Dict[str, Any]] = None
    type: Optional[str] = None
