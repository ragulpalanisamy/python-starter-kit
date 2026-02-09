"""Repository for Board operations."""

from typing import List, Optional
from datetime import datetime
from app.db.mongodb import MongoDB
from app.Models.domain_models import BoardModel
from app.utils.logger import get_logger

logger = get_logger(__name__)

class BoardRepository:
    """Repository for managing Boards in MongoDB."""
    
    def __init__(self, mongodb: MongoDB):
        """
        Initialize repository.
        
        Args:
            mongodb: MongoDB instance
        """
        self.mongodb = mongodb
        self.collection = mongodb.get_collection("boards")
    
    async def create_board(self, board_data: dict) -> int:
        """
        Create a new board record.
        
        Args:
            board_data: Board data
            
        Returns:
            board_id of the created record
        """
        try:
            board_model = BoardModel(**board_data)
            await self.collection.insert_one(
                board_model.model_dump(by_alias=True, exclude={"id"})
            )
            logger.info(f"Created board record: {board_data['board_id']}")
            return board_data['board_id']
        except Exception as e:
            logger.error(f"Error creating board: {e}")
            raise
    
    async def get_board(self, board_id: int) -> Optional[dict]:
        """
        Get board by ID.
        
        Args:
            board_id: Board identifier
            
        Returns:
            Board document or None
        """
        try:
            board = await self.collection.find_one({"board_id": board_id})
            if board:
                board["_id"] = str(board["_id"])
            return board
        except Exception as e:
            logger.error(f"Error getting board {board_id}: {e}")
            raise
    
    async def list_boards(
        self,
        skip: int = 0,
        limit: int = 10,
        status: Optional[str] = None
    ) -> List[dict]:
        """
        List boards with pagination.
        
        Args:
            skip: Number of records to skip
            limit: Maximum number of records to return
            status: Optional status filter
            
        Returns:
            List of board documents
        """
        try:
            query = {}
            if status:
                query["status"] = status
            
            cursor = self.collection.find(query).sort("created_at", -1).skip(skip).limit(limit)
            boards = await cursor.to_list(length=limit)
            
            # Convert ObjectId to string
            for board in boards:
                board["_id"] = str(board["_id"])
            
            return boards
        except Exception as e:
            logger.error(f"Error listing boards: {e}")
            raise
    
    async def update_board(self, board_id: int, board_data: dict) -> bool:
        """
        Update a board record.
        
        Args:
            board_id: Board identifier
            board_data: Board data to update
            
        Returns:
            True if updated successfully
        """
        try:
            board_data["updated_at"] = datetime.utcnow()
            result = await self.collection.update_one(
                {"board_id": board_id},
                {"$set": board_data}
            )
            if result.modified_count > 0:
                logger.info(f"Updated board: {board_id}")
                return True
            return False
        except Exception as e:
            logger.error(f"Error updating board {board_id}: {e}")
            raise

    async def delete_board(self, board_id: int) -> bool:
        """
        Delete a board record.
        
        Args:
            board_id: Board identifier
            
        Returns:
            True if deleted successfully
        """
        try:
            result = await self.collection.delete_one({"board_id": board_id})
            if result.deleted_count > 0:
                logger.info(f"Deleted board: {board_id}")
                return True
            return False
        except Exception as e:
            logger.error(f"Error deleting board: {e}")
            raise
