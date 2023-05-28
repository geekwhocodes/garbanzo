from functools import lru_cache
from pydantic import BaseSettings

class Settings(BaseSettings):
    env: str = "dev"
    database_url : str = ""

@lru_cache
def get_settings() -> Settings:
    settings = Settings()
    return settings