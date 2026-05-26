from fastapi import Depends, HTTPException, Header, Cookie, status
from sqlalchemy.orm import Session
from database import get_db
from models.user import User
from auth.jwt_handler import verify_token
from typing import Optional

def get_current_user(
    db: Session = Depends(get_db),
    jwt_cookie: Optional[str] = Cookie(None, alias="JWT"),
    authorization: Optional[str] = Header(None)
) -> User:
    token = None
    if authorization and authorization.startswith("Bearer "):
        token = authorization[7:]
    elif jwt_cookie:
        token = jwt_cookie

    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not authenticated"
        )

    payload = verify_token(token)
    if not payload:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not authenticated"
        )

    user = db.query(User).filter(User.id == payload["user_id"]).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found"
        )
    return user
