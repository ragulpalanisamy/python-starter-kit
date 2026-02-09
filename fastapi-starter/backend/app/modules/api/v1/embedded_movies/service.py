from typing import List, Tuple, Optional
from app.db.mongodb import MongoDB
from app.Models.embedded_movie import EmbeddedMovieModel
from app.utils.logger import get_logger
from bson import ObjectId

logger = get_logger(__name__)

class EmbeddedMovieService:
    """Service for Embedded Movie operations."""
    
    def __init__(self, mongodb: MongoDB):
        self.mongodb = mongodb
        self.collection_name = "embedded_movies"

    async def get_movies(self, page: int, page_size: int) -> Tuple[List[EmbeddedMovieModel], int]:
        """Get paginated embedded movies."""
        skip = (page - 1) * page_size
        collection = self.mongodb.get_collection(self.collection_name)
        total = await collection.count_documents({})
        cursor = collection.find({}).skip(skip).limit(page_size)
        movies = [EmbeddedMovieModel(**doc) async for doc in cursor]
        return movies, total

    async def get_movie(self, movie_id: str) -> Optional[EmbeddedMovieModel]:
        """Get a single embedded movie by ID."""
        collection = self.mongodb.get_collection(self.collection_name)
        doc = await collection.find_one({"_id": ObjectId(movie_id)})
        return EmbeddedMovieModel(**doc) if doc else None

    async def create_movie(self, movie_data: EmbeddedMovieModel) -> EmbeddedMovieModel:
        """Create a new embedded movie."""
        collection = self.mongodb.get_collection(self.collection_name)
        doc = movie_data.dict(by_alias=True, exclude={"id"})
        result = await collection.insert_one(doc)
        movie_data.id = result.inserted_id
        return movie_data

    async def update_movie(self, movie_id: str, movie_data: dict) -> Optional[EmbeddedMovieModel]:
        """Update an existing embedded movie."""
        collection = self.mongodb.get_collection(self.collection_name)
        await collection.update_one(
            {"_id": ObjectId(movie_id)},
            {"$set": movie_data}
        )
        return await self.get_movie(movie_id)

    async def delete_movie(self, movie_id: str) -> bool:
        """Delete an embedded movie."""
        collection = self.mongodb.get_collection(self.collection_name)
        result = await collection.delete_one({"_id": ObjectId(movie_id)})
        return result.deleted_count > 0
