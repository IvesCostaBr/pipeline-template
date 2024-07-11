from functools import wraps
from fastapi import Request
from src.utils.external_auth import authenticate
from src.utils.exceptions import raised_forbiden

def check_permissions(rule: str, required_permissions: list[str]):
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            request = kwargs.get('request')
            authorization: str = request.headers.get("Authorization")
            user = authenticate(authorization)
            user_permissions = user.get("permissions", {}).get(rule)
            if not all(perm in user_permissions for perm in required_permissions):
                raised_forbiden()
            return await func(*args, **kwargs)
        return wrapper
    return decorator