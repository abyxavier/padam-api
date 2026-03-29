import os
from pydantic_settings import BaseSettings
from functools import lru_cache

# Build absolute path to padam-backend/.env regardless of where VS Code starts execution
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
ENV_PATH = os.path.join(BASE_DIR, ".env")

class Settings(BaseSettings):
    app_name: str = "AI Movie Recommender"
    database_url: str
    open_ai_key: str = ""

    class Config:
        env_file = ENV_PATH

@lru_cache
def get_settings() -> Settings:
    return Settings()
