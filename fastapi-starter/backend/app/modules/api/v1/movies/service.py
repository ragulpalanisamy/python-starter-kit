from typing import List, Tuple
from app.db.mongodb import MongoDB
from app.Models.domain_models import MovieModel
from app.utils.logger import get_logger
from typing import Optional

logger = get_logger(__name__)

class MovieService:
    """Service for Movie operations."""
    
    def __init__(self, mongodb: MongoDB):
        self.mongodb = mongodb
        self.collection_name = "movies"

    async def get_movies(self, page: int, page_size: int) -> Tuple[List[MovieModel], int]:
        """Get paginated movies."""
        skip = (page - 1) * page_size
        collection = self.mongodb.get_collection(self.collection_name)
        total = await collection.count_documents({})
        cursor = collection.find({}).skip(skip).limit(page_size)
        movies = [MovieModel(**doc) async for doc in cursor]
        return movies, total

    async def get_movie(self, movie_id: str) -> Optional[MovieModel]:
        """Get a single movie by ID."""
        from bson import ObjectId
        collection = self.mongodb.get_collection(self.collection_name)
        doc = await collection.find_one({"_id": ObjectId(movie_id)})
        return MovieModel(**doc) if doc else None

    async def create_movie(self, movie_data: MovieModel) -> MovieModel:
        """Create a new movie."""
        collection = self.mongodb.get_collection(self.collection_name)
        doc = movie_data.dict(by_alias=True, exclude={"id"})
        result = await collection.insert_one(doc)
        movie_data.id = result.inserted_id
        return movie_data

    async def update_movie(self, movie_id: str, movie_data: dict) -> Optional[MovieModel]:
        """Update an existing movie."""
        from bson import ObjectId
        collection = self.mongodb.get_collection(self.collection_name)
        await collection.update_one(
            {"_id": ObjectId(movie_id)},
            {"$set": movie_data}
        )
        return await self.get_movie(movie_id)

    async def delete_movie(self, movie_id: str) -> bool:
        """Delete a movie."""
        from bson import ObjectId
        collection = self.mongodb.get_collection(self.collection_name)
        result = await collection.delete_one({"_id": ObjectId(movie_id)})
        return result.deleted_count > 0
