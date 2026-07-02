from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite+aiosqlite:///./cq_housing.db"
    DATABASE_URL_SYNC: str = "sqlite:///./cq_housing.db"
    SECRET_KEY: str = "dev-secret"
    DEBUG: bool = True
    MOCK_DEFAULT_COUNT: int = 10000

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
