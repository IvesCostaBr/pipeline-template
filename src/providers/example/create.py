from src.repository import example_repo

def exec(data):
    payload = data.get('payload')
    id = example_repo.create(payload)
    return {"id": id}