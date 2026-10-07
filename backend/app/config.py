from pydantic_settings import BaseSettings
import os


class Settings(BaseSettings):
    app_name: str = "AI Study Assistant"
    database_url: str = "sqlite:///./study_assistant.db"
    openai_api_key: str = ""
    backend_url: str = "http://localhost:8000"

    class Config:
        env_file = ".env"
        case_sensitive = False


settings = Settings()
