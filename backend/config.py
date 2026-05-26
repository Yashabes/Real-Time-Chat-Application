from typing import List

from pydantic import AnyHttpUrl, Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str = Field(
        default="mysql+mysqlconnector://root:Virendra%40123@localhost:3306/RealTimeChatApp",
        env="DATABASE_URL",
    )
    JWT_SECRET_KEY: str = Field(default="zH5kF#nM9$aW2xS4yU7vB3jR8qL6tC1d", env="JWT_SECRET")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = Field(default=60, env="ACCESS_TOKEN_EXPIRE")
    ALGORITHM: str = Field(default="HS256", env="JWT_ALGORITHM")
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = [
        "http://localhost:5173",
        "http://localhost:3000",
    ]

    model_config = {
        "env_file": ".env",
        "env_file_encoding": "utf-8",
        "extra": "ignore",
        "env_prefix": "",
    }


settings = Settings()
