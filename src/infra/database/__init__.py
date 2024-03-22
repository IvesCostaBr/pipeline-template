
from src.infra.database.mongo_connection import MongoDatabase
import os


user_service_db = MongoDatabase(
    os.environ.get("MONGO_HOST"),
    os.environ.get("MONGO_PORT"),
    os.environ.get("MONGO_DB_USER_SERVICE"),
)
