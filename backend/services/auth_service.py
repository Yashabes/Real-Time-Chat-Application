from sqlalchemy.orm import Session

from auth.password import hash_password, verify_password
from auth.jwt_handler import create_access_token
from schemas.auth import RegisterRequest, LoginRequest, LoginResponse
from schemas.user import UserDTO
from models.user import User


def convert_to_dto(user: User) -> UserDTO:
    return UserDTO(id=user.id, username=user.username, email=user.email)


def register_user(db: Session, form: RegisterRequest) -> str:
    existing_username = db.query(User).filter(User.username == form.username).first()
    if existing_username:
        raise ValueError("Username is already in use")

    existing_email = db.query(User).filter(User.email == form.email).first()
    if existing_email:
        raise ValueError("Email is already in use")

    user = User(
        username=form.username,
        email=form.email,
        password=hash_password(form.password),
        role="ROLE_USER",
        is_online=False,
    )
    db.add(user)
    db.commit()
    db.refresh(user)

    return "User registered successfully"


def login_user(db: Session, form: LoginRequest) -> LoginResponse:
    user = db.query(User).filter(User.username == form.username).first()
    if user is None:
        raise ValueError("Username not found")

    if not verify_password(form.password, user.password):
        raise ValueError("Invalid username or password")

    token = create_access_token(user.username, user.id)
    return LoginResponse(token=token, user=convert_to_dto(user))
