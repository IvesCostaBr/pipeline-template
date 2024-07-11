from abc import ABC
from contextlib import contextmanager
from src.infra.database.db_config import SessionLocal


class RepositoryAbs(ABC):
    @contextmanager
    def get_session(self):
        session = SessionLocal()
        try:
            yield session
            session.commit()
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()

    @classmethod
    def get(self, id: int):
        raise NotImplemented()

    @classmethod
    def get_all(self):
        raise NotImplemented()

    @classmethod
    def create(self, data):
        raise NotImplemented()

    @classmethod
    def filter(self, query):
        raise NotImplemented()

    @classmethod
    def update(self, id, data):
        raise NotImplemented()

    @classmethod
    def delete(self, id):
        raise NotImplemented()