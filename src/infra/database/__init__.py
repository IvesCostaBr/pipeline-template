
from src.infra.database.mongo_connection import MongoDatabase
import os


nosql_database = MongoDatabase(
    os.environ.get("MONGO_HOST"),
    os.environ.get("MONGO_PORT"),
    os.environ.get("MONGO_DB_NAME"),
)
