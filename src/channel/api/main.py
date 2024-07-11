from src.channel.api.routes import utils
from src.infra.database.db_config import create_db
from starlette import status
from fastapi import FastAPI, Request, responses
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv
# import sentry_sdk


# sentry_sdk.init(
#     dsn=os.environ.get('SENTRY_DSN'),
#     traces_sample_rate=0.1,
#     profiles_sample_rate=0.1,
# )


if os.environ.get("DEPLOY") and bool(int(os.environ.get("DEPLOY"))):
    from src.utils.secrets import start_secret_env
    if os.path.exists("./src/configs/credential-gcp.json"):
        start_secret_env()
        load_dotenv()
        os.remove(".env")
else:
    load_dotenv()


ROOT_PATH = os.path.dirname(os.path.abspath(__file__))


create_db()

api = FastAPI(title="Pipeline Project")

origins = [
    "*",
]

api.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


api.include_router(utils.router, prefix="/utils")


@api.exception_handler(Exception)
async def exception_handler(request: Request, exc: Exception):
    """Exception generic handler."""
    return responses.JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={"message": str(exc)},
    )
