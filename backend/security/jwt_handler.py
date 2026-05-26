from jose import jwt
from datetime import datetime,timedelta
from app.config import JWT_SECRET

def create_token(data):

    payload=data.copy()

    payload["exp"]=(
        datetime.utcnow()
        +timedelta(hours=1)
    )

    return jwt.encode(
        payload,
        JWT_SECRET,
        algorithm="HS256"
    )