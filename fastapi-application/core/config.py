from pydantic import BaseModel, PostgresDsn
from pydantic_settings import BaseSettings


class ApiPrefix(BaseModel):
    prefix: str = "/api"


class RunConfig(BaseModel):
    host: str = "0.0.0.0"
    port: int = 8000


class DatabaseConfig(BaseModel):
    url: PostgresDsn
    echo: bool = False
    echo_pool: bool = False,
    pool_pre_ping: bool = True,
    pool_size: int = 50,
    max_overflow: int = 10,

class Settings(BaseSettings):
    run: RunConfig = RunConfig()
    api: ApiPrefix = ApiPrefix()
    db: DatabaseConfig


settings = Settings()
