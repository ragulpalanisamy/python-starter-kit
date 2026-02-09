"""Board API endpoints."""

from fastapi import APIRouter, HTTPException, Depends, Query
from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
from app.db.mongodb import get_mongodb
from .service import BoardRepository
from .controller import BoardController
from app.utils.logger import get_logger

logger = get_logger(__name__)
router = APIRouter()

# Dependency to get board controller
async def get_board_controller(mongodb = Depends(get_mongodb)):
    repo = BoardRepository(mongodb)
    return BoardController(repo)

from app.validations.board_schema import BoardCreate, BoardUpdate, BoardResponse

@router.post("", response_model=int)
async def create_board(
    board: BoardCreate,
    controller: BoardController = Depends(get_board_controller)
):
    """Create a new board."""
    return await controller.create_board(board.model_dump())

@router.get("", response_model=List[BoardResponse])
async def list_boards(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    status: Optional[str] = None,
    controller: BoardController = Depends(get_board_controller)
):
    """List boards with pagination."""
    return await controller.list_boards(skip=skip, limit=limit, status=status)

@router.get("/{board_id}", response_model=BoardResponse)
async def get_board(
    board_id: int,
    controller: BoardController = Depends(get_board_controller)
):
    """Get board by ID."""
    return await controller.get_board(board_id)

@router.put("/{board_id}")
async def update_board(
    board_id: int,
    board_update: BoardUpdate,
    controller: BoardController = Depends(get_board_controller)
):
    """Update a board."""
    return await controller.update_board(board_id, board_update.model_dump(exclude_unset=True))

@router.delete("/{board_id}")
async def delete_board(
    board_id: int,
    controller: BoardController = Depends(get_board_controller)
):
    """Delete a board."""
    return await controller.delete_board(board_id)
