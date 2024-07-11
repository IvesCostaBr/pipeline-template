from fastapi.routing import APIRouter
from src.driver.runner import pipeline_runner


router = APIRouter(tags=["Repository"])


@router.get("/healtcheck")
async def detail_file():
    return pipeline_runner("healtcheck", {})
