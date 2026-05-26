from sqlalchemy.orm import Session
from typing import List, Optional

from models.user import User


def get_user_by_id(db: Session, user_id: int) -> Optional[User]:
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_username(db: Session, username: str) -> Optional[User]:
    return db.query(User).filter(User.username == username).first()


def user_exists(db: Session, username: str) -> bool:
    return db.query(User).filter(User.username == username).first() is not None


def set_user_online_status(db: Session, username: str, is_online: bool) -> None:
    user = db.query(User).filter(User.username == username).first()
    if user:
        user.is_online = is_online
        db.commit()


def get_online_users(db: Session) -> List[User]:
    return db.query(User).filter(User.is_online.is_(True)).all()


def get_all_users(db: Session) -> List[User]:
    return db.query(User).all()
