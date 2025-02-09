import os
from pydantic import BaseSettings


class Settings(BaseSettings):
	DB_USER: str = os.environ.get("DB_USER", "postgres")
	DB_PASSWORD: str = os.environ.get("DB_PASSWORD", "postgres")
	DB_SERVER: str = os.environ.get("DB_SERVER", "blogger-db")   # localhost
	DB_PORT: int = int(os.environ.get("DB_PORT", 5432))
	DB_NAME: str = os.environ.get("DB_NAME", "blogger")
	DB_CONNECTION_STR = f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_SERVER}:{DB_PORT}/{DB_NAME}"
	APP_HOST: str = os.environ.get("APP_HOST", "0.0.0.0")
	APP_PORT: int = os.environ.get("APP_PORT", 8000)


settings = Settings()
