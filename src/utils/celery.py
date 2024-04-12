from celery import Celery
from celery.schedules import crontab
import os


app = Celery(
    "uoleti_api",
    broker=os.environ.get("CACHE_URI"),
    backend=os.environ.get("CACHE_URI"),
    include=[
        "src.tasks.logging",
    ],
)

app.autodiscover_tasks()
app.conf.timezone = "America/Sao_Paulo"
app.conf.broker_connection_retry_on_startup = True

app.conf.beat_schedule = {
    "update-limit-daily": {
        "task": "src.tasks.logging.testing",
        "schedule": crontab(minute=0, hour=0),
    },
    "validate-international-transacton": {
        "task": "src.tasks.logging.testing",
        "schedule": crontab(minute="*/1"),
    },
}
