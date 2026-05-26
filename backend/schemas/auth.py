from typing import Optional
from pydantic import BaseModel, EmailStr

from .user import UserDTO


class RegisterRequest(BaseModel):
    username: str
    password: str
    email: EmailStr


class LoginRequest(BaseModel):
    username: str
    email: Optional[EmailStr] = None
    password: str


class LoginResponse(BaseModel):
    token: str
    user: UserDTO
