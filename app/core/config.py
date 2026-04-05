from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Égide.IA MS"
    API_V1_STR: str = "/api/v1"
    ENVIRONMENT: str = "development"
    GOOGLE_API_KEY: str
    EGIDE_API_KEY: str = "chave_secreta_egide"

    class Config:
        env_file = ".env"
        extra = "ignore"

settings = Settings()