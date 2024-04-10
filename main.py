from fastapi import FastAPI, Request, responses
from starlette import status
from src.infra.database.db_config import create_db
from src.api.routes import utils
import os

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

create_db()

api = FastAPI(title="Pipeline Project")

api.include_router(utils.router, prefix="/utils")


@api.exception_handler(Exception)
async def exception_handler(request: Request, exc: Exception):
    """Exception generic handler."""
    return responses.JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={"message": str(exc)},
    )
