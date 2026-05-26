from pydantic import BaseModel, EmailStr


class UserDTO(BaseModel):
    id: int
    username: str
    email: EmailStr

    model_config = {
        "from_attributes": True,
    }
