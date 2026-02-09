from fastapi import APIRouter
from app.modules.api.v1.health import routes as health
from app.modules.api.v1.external_api import routes as external_api
from app.modules.api.v1.ml import routes as ml_predictions
from app.modules.api.v1.boards import routes as boards
from app.modules.api.v1.movies import routes as movies
from app.modules.api.v1.comments import routes as comments
from app.modules.api.v1.theaters import routes as theaters
from app.modules.api.v1.embedded_movies import routes as embedded_movies

api_router = APIRouter()

api_router.include_router(health.router, prefix="/health", tags=["Health"])
api_router.include_router(external_api.router, prefix="/external", tags=["External APIs"])
api_router.include_router(ml_predictions.router, prefix="/ml", tags=["ML Predictions"])
api_router.include_router(boards.router, prefix="/boards", tags=["Boards"])
api_router.include_router(movies.router, prefix="/movies", tags=["Movies"])
api_router.include_router(comments.router, prefix="/comments", tags=["Comments"])
api_router.include_router(theaters.router, prefix="/theaters", tags=["Theaters"])
api_router.include_router(embedded_movies.router, prefix="/embedded-movies", tags=["Embedded Movies"])
