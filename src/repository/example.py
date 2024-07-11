from src.repository.abs.repository_nosql import RepositoryNoSqlAbs

class ExampleRepository(RepositoryNoSqlAbs):
    def __init__(self):
        super().__init__()
        self.entity = "examples"
