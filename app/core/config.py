import os

from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    PROJECT_NAME: str = "Madkunyah Online Ordering"
    PROJECT_VERSION: str = "1.0.0"

    HOST: str = "0.0.0.0"
    PORT: int = int(os.getenv("PORT", 8000))
    DEBUG: bool = False

    APP_ENV: str = os.getenv("APP_ENV", "development")
    DATABASE_URL: str = os.getenv(
        "DATABASE_URL", "postgresql+asyncpg://devuser:devpass@localhost:5432/devdb"
    )

    class Config:
        env_file = ".env"


@lru_cache
def get_settings():
    return Settings()
