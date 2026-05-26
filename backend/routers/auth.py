from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session

from database import get_db
from schemas.auth import RegisterRequest, LoginRequest
from services.auth_service import register_user, login_user
from schemas.user import UserDTO
from auth.dependencies import get_current_user

router = APIRouter(prefix="/api/auth", tags=["auth"])


@router.post("/register-user")
def register_user_route(register_request: RegisterRequest, db: Session = Depends(get_db)):
    try:
        return register_user(db, register_request)
    except ValueError as error:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(error))


@router.post("/login", response_model=UserDTO)
def login_route(login_request: LoginRequest, response: Response, db: Session = Depends(get_db)):
    try:
        login_response = login_user(db, login_request)
    except ValueError as error:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(error))

    response.set_cookie(
        key="JWT",
        value=login_response.token,
        httponly=True,
        secure=False,
        samesite="lax",
        path="/",
        max_age=60 * 60,
    )
    return login_response.user


@router.post("/logout")
def logout_route(response: Response):
    response.delete_cookie(
        key="JWT",
        path="/",
        samesite="strict",
    )
    return "Logged Out Successfully"


@router.get("/getcurrentuser", response_model=UserDTO)
def get_current_user_route(current_user=Depends(get_current_user)):
    return UserDTO(id=current_user.id, username=current_user.username, email=current_user.email)
