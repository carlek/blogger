import os
from pydantic import BaseSettings


class Settings(BaseSettings):
	DB_USER: str = os.environ.get("DB_USER", "carlek")
	DB_PASSWORD: str = os.environ.get("DB_PASSWORD", "ekekek")
	DB_SERVER: str = os.environ.get("DB_SERVER", "localhost")
	DB_PORT: int = int(os.environ.get("DB_PORT", 5432))
	DB_NAME: str = os.environ.get("DB_NAME", "blogger")
	# DB_CONNECTION_STR = f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_SERVER}:{DB_PORT}/{DB_NAME}"
	DB_CONNECTION_STR = "postgresql+asyncpg://carlek:ekekek@localhost:5432/blogger"
	APP_HOST: str = os.environ.get("APP_HOST", "localhost")
	APP_PORT: int = os.environ.get("APP_PORT", 8000)


settings = Settings()
