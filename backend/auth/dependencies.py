from fastapi import Depends, HTTPException, status, Request
from sqlalchemy.orm import Session

from database import get_db
from services.user_service import get_user_by_id
from auth.jwt_handler import get_token_from_request, decode_access_token


def get_current_user(request: Request, db: Session = Depends(get_db)):
    token = get_token_from_request(request)
    if token is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authentication credentials were not provided.",
        )

    token_data = decode_access_token(token)
    if token_data is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired authentication token.",
        )

    user = get_user_by_id(db, token_data["user_id"])
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found.",
        )

    return user
