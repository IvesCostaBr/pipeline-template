from fastapi import Depends
from src.utils.exceptions import raised_unauthorized


def get_user(token: str) -> dict|None:
    """Implement your authentication method"""
    return {
        "id": 1
    }

def authenticate(token: str):
    user = get_user(token)
    if not user:
        raised_unauthorized("Usuário não autenticado")
    user["permissions"] = {"example":["read", "write"]}
    return user