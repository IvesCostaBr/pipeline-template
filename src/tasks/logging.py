from src.utils import logger
from src.utils.celery import app


@app.task
def testing():
    logger.info("---------")