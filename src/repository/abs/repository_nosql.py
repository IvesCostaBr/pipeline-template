from abc import ABC
from src.infra.database import nosql_database



class RepositoryNoSqlAbs(ABC):
    def __init__(self):
        self.entity = None
        self.db = nosql_database 

    def get(self, id: int):
        return self.db.get(self.entity, id)

    def get_all(self):
        return self.db.get_all(self.entity)

    def create(self, data):
        return self.db.create(self.entity, data)

    def filter(self, query, skip: int, limit: int, exclude_fields: list[str] = []):
        return self.db.filter_query(self.entity, query,skip, limit, exclude_fields)

    def update(self, id, data):
        return self.db.update(self.entity, id, data)

    def delete(self, id):
        return self.db.delete(self.entity, id)

    def exists(self, **kwargs):
        return self.db.exists(self.entity, kwargs)