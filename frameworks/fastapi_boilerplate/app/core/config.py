"""Settings for the application."""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):  # type: ignore[misc]
    """Settings for the application."""

    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "Test Project"
    BACKEND_CORS_ORIGINS: list[str] =  ["http://localhost:4200"]


settings: Settings = Settings()
