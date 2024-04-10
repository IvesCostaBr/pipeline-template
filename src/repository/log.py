from sqlalchemy.orm import Session
from src.repository.abs.repository import RepositoryAbs
from src.models import log as log_schema
from sqlalchemy.orm import Session


class LogRepository(RepositoryAbs):
    def __init__(self):
        self.entity = "logs"

    def get(self, db: Session, id: int):
        return db.query(log_schema.Log).filter(log_schema.Log.id == id).first()

    def get_all(self, db: Session, skip: int = 0, limit: int = 1000):
        return db.query(log_schema.Log).offset(skip).limit(limit).all()

    def create(self, db: Session, data: log_schema.LogModel):
        try:
            log_obj = log_schema.Log(**data.model_dump())
            db.add(log_obj)
            db.commit()
            db.refresh(log_obj)
            return log_obj
        except Exception as ex:
            print("erro in add register")

    def filter(self, db: Session):
        pass

    def update(self, id, data):
        pass
