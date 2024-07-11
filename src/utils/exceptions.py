from fastapi import HTTPException
from starlette import status

def raised_unauthorized(msg: str = None):
    if not msg:
        msg = "not authenticated"
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail=msg,
    )

def raised_forbiden(msg: str = None):
    if not msg:
        msg = "forbiden"
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail=msg,
    )