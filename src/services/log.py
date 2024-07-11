from fastapi import HTTPException
from src.repository import log_repo

class LogService:
    def __init__(self):
        self.entity = "log"
        self.repo = log_repo

    def get(self):
        pass

    def get_all(self):
        pass
