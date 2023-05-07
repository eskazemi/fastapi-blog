from pydantic import BaseSettings, Field
from functools import lru_cache


class Settings(BaseSettings):
    api_prefix: str = Field(..., env="API_PREFIX")
    debug: str = Field(..., env="DEBUG")
    access_token_expire_minutes: str = Field(...,
                                             env="ACCESS_TOKEN_EXPIRE_MINUTES")
    secret_key: str = Field(..., env="SECRET_KEY")
    algorithm: str = Field(..., env="ALGORITHM")
    name: str = Field(..., env="PROJ_NAME")
    project_version: str = Field(..., env="PROJECT_VERSION")
    origins: str = Field(..., env="ORIGINS")
    postgres_user: str = Field(..., env="POSTGRES_USER")
    postgres_password: str = Field(..., env="POSTGRES_PASSWORD")
    postgres_server: str = Field(default="localhost", env="POSTGRES_SERVER")
    postgres_port: int = Field(default=5432, env="POSTGRES_PORT")
    postgres_db: str = Field(..., env="POSTGRES_DB")

    class Config:
        env_file = ".env"


@lru_cache
def get_setting():
    return Settings()
