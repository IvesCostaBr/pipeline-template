from src.repository import example_repo


def exec(data):
    payload = data.get('payload')
    query = {}
    if payload.get('key') and payload.get('value'):
        query[payload.get('key')] = payload.get('value')
    return example_repo.filter(query,  payload.get('skip') or 0, payload.get('limit') or 1000)