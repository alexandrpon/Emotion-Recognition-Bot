from pydantic import BaseSettings, SecretStr


class Settings(BaseSettings):
    dbs_connections: SecretStr

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


config = Settings()
