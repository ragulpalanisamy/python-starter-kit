from typing import List, Tuple, Optional
from app.db.mongodb import MongoDB
from app.Models.theater import TheaterModel
from app.utils.logger import get_logger
from bson import ObjectId

logger = get_logger(__name__)

class TheaterService:
    """Service for Theater operations."""
    
    def __init__(self, mongodb: MongoDB):
        self.mongodb = mongodb
        self.collection_name = "theaters"

    async def get_theaters(self, page: int, page_size: int) -> Tuple[List[TheaterModel], int]:
        """Get paginated theaters."""
        skip = (page - 1) * page_size
        collection = self.mongodb.get_collection(self.collection_name)
        total = await collection.count_documents({})
        cursor = collection.find({}).skip(skip).limit(page_size)
        theaters = [TheaterModel(**doc) async for doc in cursor]
        return theaters, total

    async def get_theater(self, theater_id: str) -> Optional[TheaterModel]:
        """Get a single theater by ID."""
        collection = self.mongodb.get_collection(self.collection_name)
        doc = await collection.find_one({"_id": ObjectId(theater_id)})
        return TheaterModel(**doc) if doc else None

    async def create_theater(self, theater_data: TheaterModel) -> TheaterModel:
        """Create a new theater."""
        collection = self.mongodb.get_collection(self.collection_name)
        doc = theater_data.dict(by_alias=True, exclude={"id"})
        result = await collection.insert_one(doc)
        theater_data.id = result.inserted_id
        return theater_data

    async def update_theater(self, theater_id: str, theater_data: dict) -> Optional[TheaterModel]:
        """Update an existing theater."""
        collection = self.mongodb.get_collection(self.collection_name)
        await collection.update_one(
            {"_id": ObjectId(theater_id)},
            {"$set": theater_data}
        )
        return await self.get_theater(theater_id)

    async def delete_theater(self, theater_id: str) -> bool:
        """Delete a theater."""
        collection = self.mongodb.get_collection(self.collection_name)
        result = await collection.delete_one({"_id": ObjectId(theater_id)})
        return result.deleted_count > 0
