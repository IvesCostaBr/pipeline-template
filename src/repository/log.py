from src.repository.abs.repository import RepositoryAbs
from datetime import datetime
from src.entities import log as log_model


class LogRepository(RepositoryAbs):
    def __init__(self):
        self.entity = "logs"

    def get(self, id: int):
        with self.get_session() as db:
            return db.query(log_model.Log).filter(log_model.Log.id == id).first()

    def get_all(self, skip: int = 0, limit: int = 1000):
        with self.get_session() as db:
            return db.query(log_model.Log).offset(skip).limit(limit).all()

    def create(self, data):
        with self.get_session() as db:
            log_obj = log_model.Log(**data)
            log_obj.created_at = datetime.now()
            db.add(log_obj)
            db.commit()
            db.refresh(log_obj)
            return log_obj

    def filter_query(self, skip: int = 0, limit: int = 1000, **kwargs):
        with self.get_session() as db:
            query = db.query(self.model)
            filters = []
            for key, value in kwargs.items():
                if hasattr(self.model, key):
                    filters.append(
                        getattr(self.model, key) == value)
            if filters:
                query = query.filter(*filters)

            query = query.offset(skip).limit(limit)

            result = query.all()

            return [x.to_dict() for x in result]

    def update(self, id, kwargs):
        with self.get_session() as db:
            try:
                result = db.query(self.model).filter(
                    self.model.id == id).first()

                result.updated_at = datetime.now()
                if not result:
                    return None
                for key, value in kwargs.items():
                    if hasattr(self.model, key):
                        setattr(result, key, value)

                db.commit()
                db.refresh(result)

                return result.to_dict()
            except Exception as ex:
                raise Exception(f"error update {self.entity}")