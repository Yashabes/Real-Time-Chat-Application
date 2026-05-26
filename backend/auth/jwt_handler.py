from datetime import datetime, timedelta
from typing import Optional

from jose import JWTError, jwt
from fastapi import Request

from config import settings


def create_access_token(username: str, user_id: int) -> str:
    now = datetime.utcnow()
    payload = {
        "sub": username,
        "userId": str(user_id),
        "iat": now,
        "exp": now + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES),
    }
    return jwt.encode(payload, settings.JWT_SECRET_KEY, algorithm=settings.ALGORITHM)


def decode_access_token(token: str) -> Optional[dict]:
    try:
        payload = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.ALGORITHM])
        username: str = payload.get("sub")
        user_id: str = payload.get("userId")
        if username is None or user_id is None:
            return None
        return {"username": username, "user_id": int(user_id)}
    except JWTError:
        return None


def get_token_from_request(request: Request) -> Optional[str]:
    auth_header = request.headers.get("Authorization")
    if auth_header and auth_header.startswith("Bearer "):
        return auth_header[7:]

    jwt_cookie = request.cookies.get("JWT")
    if jwt_cookie:
        return jwt_cookie

    return None
