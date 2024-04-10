from abc import ABC


class RepositoryAbs(ABC):
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
