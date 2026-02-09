import math
from fastapi import HTTPException
from app.modules.api.v1.comments.service import CommentService
from app.validations.pagination import PaginatedResponse
from app.validations.comment_schema import CommentCreate, CommentUpdate
from app.Models.domain_models import CommentModel
from app.utils.logger import get_logger

logger = get_logger(__name__)

class CommentController:
    """Controller for Comment endpoints."""
    
    def __init__(self, comment_service: CommentService):
        self.comment_service = comment_service

    async def list_comments(self, page: int, page_size: int) -> PaginatedResponse[CommentModel]:
        """List comments with pagination."""
        try:
            comments, total = await self.comment_service.get_comments(page, page_size)
            total_pages = math.ceil(total / page_size) if total > 0 else 0
            return PaginatedResponse(
                items=comments,
                total=total,
                page=page,
                page_size=page_size,
                total_pages=total_pages,
                has_next=page < total_pages,
                has_prev=page > 1
            )
        except Exception as e:
            logger.error(f"Error listing comments: {e}")
            raise HTTPException(status_code=500, detail="Failed to fetch comments")

    async def get_comment(self, comment_id: str) -> CommentModel:
        """Get a comment by ID."""
        comment = await self.comment_service.get_comment(comment_id)
        if not comment:
            raise HTTPException(status_code=404, detail="Comment not found")
        return comment

    async def create_comment(self, comment_data: CommentCreate) -> CommentModel:
        """Create a new comment."""
        try:
            # Convert schema to domain model
            # Note: comment_data.movie_id is a string, CommentModel expects PyObjectId
            db_comment = CommentModel(**comment_data.dict())
            return await self.comment_service.create_comment(db_comment)
        except Exception as e:
            logger.error(f"Error creating comment: {e}")
            raise HTTPException(status_code=500, detail="Failed to create comment")

    async def update_comment(self, comment_id: str, comment_data: CommentUpdate) -> CommentModel:
        """Update a comment."""
        try:
            update_dict = {k: v for k, v in comment_data.dict().items() if v is not None}
            comment = await self.comment_service.update_comment(comment_id, update_dict)
            if not comment:
                raise HTTPException(status_code=404, detail="Comment not found")
            return comment
        except HTTPException:
            raise
        except Exception as e:
            logger.error(f"Error updating comment: {e}")
            raise HTTPException(status_code=500, detail="Failed to update comment")

    async def delete_comment(self, comment_id: str) -> dict:
        """Delete a comment."""
        try:
            success = await self.comment_service.delete_comment(comment_id)
            if not success:
                raise HTTPException(status_code=404, detail="Comment not found")
            return {"message": "Comment deleted successfully"}
        except HTTPException:
            raise
        except Exception as e:
            logger.error(f"Error deleting comment: {e}")
            raise HTTPException(status_code=500, detail="Failed to delete comment")
