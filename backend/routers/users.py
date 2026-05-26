from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from schemas.user import UserDTO
from services.user_service import get_online_users, get_all_users

router = APIRouter(prefix="/api/users", tags=["users"])


@router.get("/online", response_model=List[UserDTO])
def get_online_users_route(db: Session = Depends(get_db)):
    users = get_online_users(db)
    return [UserDTO(id=user.id, username=user.username, email=user.email) for user in users]


@router.get("/all", response_model=List[UserDTO])
def get_all_users_route(db: Session = Depends(get_db)):
    users = get_all_users(db)
    return [UserDTO(id=user.id, username=user.username, email=user.email) for user in users]
