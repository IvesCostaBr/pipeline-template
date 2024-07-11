from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.routing import APIRouter
from src.driver.responser_fomart import fastapi_formatter
from src.driver.runner import pipeline_runner
from src.utils.decorators import check_permissions
from starlette import status
from src.channel.api.models import (
    example as example_model
)

router = APIRouter(tags=["Repository"])


@router.get("/healtcheck")
async def detail_file():
    return pipeline_runner("healtcheck", {})

@router.post("/examples", response_model=example_model.OutExampleCreate, status_code=status.HTTP_201_CREATED)
@check_permissions("example", ["write"])
async def create(request: Request, data: example_model.InExample):
    response = pipeline_runner("create_example", data.model_dump())
    return fastapi_formatter(response, status.HTTP_400_BAD_REQUEST)
    

@router.get("/examples", response_model=dict)
async def filter_examples(limit: int = None, skip: int = None, key: str = None, value: str = None):
    response = pipeline_runner("get_example", {"limit": limit, "skip": skip, "key": key, "value": value})
    return fastapi_formatter(response, status.HTTP_400_BAD_REQUEST)