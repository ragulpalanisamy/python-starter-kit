from fastapi import HTTPException
from typing import List, Optional
from .service import BoardRepository
from app.utils.logger import get_logger
from pydantic import BaseModel, Field
from datetime import datetime

logger = get_logger(__name__)

# Request/Response models moved from routes to controller (or can stay in routes, but common practice in this repo seems to be routes or common schema file)
# In movies, they are in app.validations.movie_schema.
# For boards, they were in routes.py. I'll move them to controller for now or keep them in routes.
# Actually, movies controller imports from app.validations.movie_schema.
# I will check if there is a board_schema in app.validations.

class BoardController:
    """Controller for Board endpoints."""
    
    def __init__(self, board_repository: BoardRepository):
        self.board_repository = board_repository

    async def create_board(self, board_data: dict) -> int:
        """Create a new board."""
        # Check if board_id already exists
        existing = await self.board_repository.get_board(board_data["board_id"])
        if existing:
            raise HTTPException(status_code=400, detail="Board ID already exists")
        
        try:
            return await self.board_repository.create_board(board_data)
        except Exception as e:
            logger.error(f"Failed to create board: {e}")
            raise HTTPException(status_code=500, detail="Internal server error")

    async def list_boards(self, skip: int, limit: int, status: Optional[str] = None) -> List[dict]:
        """List boards with pagination."""
        try:
            return await self.board_repository.list_boards(skip=skip, limit=limit, status=status)
        except Exception as e:
            logger.error(f"Failed to list boards: {e}")
            raise HTTPException(status_code=500, detail="Internal server error")

    async def get_board(self, board_id: int) -> dict:
        """Get board by ID."""
        board = await self.board_repository.get_board(board_id)
        if not board:
            raise HTTPException(status_code=404, detail="Board not found")
        return board

    async def update_board(self, board_id: int, board_update: dict) -> dict:
        """Update a board."""
        updated = await self.board_repository.update_board(board_id, board_update)
        if not updated:
            raise HTTPException(status_code=404, detail="Board not found or no changes made")
        return {"message": "Board updated successfully"}

    async def delete_board(self, board_id: int) -> dict:
        """Delete a board."""
        deleted = await self.board_repository.delete_board(board_id)
        if not deleted:
            raise HTTPException(status_code=404, detail="Board not found")
        return {"message": "Board deleted successfully"}
