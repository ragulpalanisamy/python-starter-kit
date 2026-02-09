from typing import List, Tuple, Optional
from app.db.mongodb import MongoDB
from app.Models.comment import CommentModel
from app.utils.logger import get_logger
from bson import ObjectId

logger = get_logger(__name__)

class CommentService:
    """Service for Comment operations."""
    
    def __init__(self, mongodb: MongoDB):
        self.mongodb = mongodb
        self.collection_name = "comments"

    async def get_comments(self, page: int, page_size: int) -> Tuple[List[CommentModel], int]:
        """Get paginated comments."""
        skip = (page - 1) * page_size
        collection = self.mongodb.get_collection(self.collection_name)
        total = await collection.count_documents({})
        cursor = collection.find({}).skip(skip).limit(page_size)
        comments = [CommentModel(**doc) async for doc in cursor]
        return comments, total

    async def get_comment(self, comment_id: str) -> Optional[CommentModel]:
        """Get a single comment by ID."""
        collection = self.mongodb.get_collection(self.collection_name)
        doc = await collection.find_one({"_id": ObjectId(comment_id)})
        return CommentModel(**doc) if doc else None

    async def create_comment(self, comment_data: CommentModel) -> CommentModel:
        """Create a new comment."""
        collection = self.mongodb.get_collection(self.collection_name)
        doc = comment_data.dict(by_alias=True, exclude={"id"})
        result = await collection.insert_one(doc)
        comment_data.id = result.inserted_id
        return comment_data

    async def update_comment(self, comment_id: str, comment_data: dict) -> Optional[CommentModel]:
        """Update an existing comment."""
        collection = self.mongodb.get_collection(self.collection_name)
        await collection.update_one(
            {"_id": ObjectId(comment_id)},
            {"$set": comment_data}
        )
        return await self.get_comment(comment_id)

    async def delete_comment(self, comment_id: str) -> bool:
        """Delete a comment."""
        collection = self.mongodb.get_collection(self.collection_name)
        result = await collection.delete_one({"_id": ObjectId(comment_id)})
        return result.deleted_count > 0
