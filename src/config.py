from pathlib import Path

from pydantic import SecretStr, PositiveInt
from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker


class Config(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
        case_sensitive=False,
    )

    BASE_DIR: Path = Path(__file__).resolve().parent.parent

    pguser: str = "admin"
    postgres_user: str = "admin"
    postgres_password: str = "admin"
    postgres_host: str = "scanner_db:5432"
    postgres_db: str = "admin"
    postgres_echo: bool = True

    @property
    def postgres_url(self) -> str:
        return (f"postgresql+psycopg://"
                f"{self.postgres_user}"
                f":{self.postgres_password}"
                f"@{self.postgres_host}"
                f"/{self.postgres_db}")


    JWT_ACCESS_SECRET_KEY: SecretStr = ""
    JWT_REFRESH_SECRET_KEY: SecretStr = ""
    JWT_ACCESS_ALGORITHM: str = "HS256"
    JWT_REFRESH_ALGORITHM: str = "HS512"
    JWT_ACCESS_EXP: PositiveInt = 15
    JWT_REFRESH_EXP: PositiveInt = 60
    JWT_TOKEN_TYPE: str = "Bearer"


config = Config()

engine = create_async_engine(
    url=config.postgres_url,
    echo=config.postgres_echo,
)

sessionmaker = async_sessionmaker(bind=engine, expire_on_commit=False)

