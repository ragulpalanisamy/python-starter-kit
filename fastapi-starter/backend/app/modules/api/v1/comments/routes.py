from fastapi import APIRouter, Depends, Query
from app.db.mongodb import get_mongodb
from app.modules.api.v1.comments.service import CommentService
from app.modules.api.v1.comments.controller import CommentController
from app.validations.pagination import PaginatedResponse
from app.Models.domain_models import CommentModel
from app.validations.comment_schema import CommentCreate, CommentUpdate

router = APIRouter()

async def get_comment_controller(mongodb = Depends(get_mongodb)):
    service = CommentService(mongodb)
    return CommentController(service)

@router.get("/", response_model=PaginatedResponse[CommentModel])
async def get_comments(
    page: int = Query(1, ge=1),
    page_size: int = Query(10, ge=1, le=100),
    controller: CommentController = Depends(get_comment_controller)
):
    """Get paginated comments."""
    return await controller.list_comments(page, page_size)

@router.get("/{comment_id}", response_model=CommentModel)
async def get_comment(
    comment_id: str,
    controller: CommentController = Depends(get_comment_controller)
):
    """Get a single comment by ID."""
    return await controller.get_comment(comment_id)

@router.post("/", response_model=CommentModel)
async def create_comment(
    comment_data: CommentCreate,
    controller: CommentController = Depends(get_comment_controller)
):
    """Create a new comment."""
    return await controller.create_comment(comment_data)

@router.put("/{comment_id}", response_model=CommentModel)
async def update_comment(
    comment_id: str,
    comment_data: CommentUpdate,
    controller: CommentController = Depends(get_comment_controller)
):
    """Update a comment."""
    return await controller.update_comment(comment_id, comment_data)

@router.delete("/{comment_id}")
async def delete_comment(
    comment_id: str,
    controller: CommentController = Depends(get_comment_controller)
):
    """Delete a comment."""
    return await controller.delete_comment(comment_id)
