from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    app_name:str="AI Movie Recommender"
    database_url:str
    open_ai_key:str=""

    class Config:
        env_file=".env"
        
@lru_cache
def get_settings()->Settings:
    return Settings()