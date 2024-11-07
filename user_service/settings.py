from pydantic import EmailStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env')

    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    USER_DATABASE_USERNAME: str
    USER_DATABASE_PASSWORD: str
    USER_DATABASE_NAME: str
    USER_DATABASE_HOST: str
    USER_DATABASE_PORT: int

    MAIL_USERNAME: str
    MAIL_HOST: str
    MAIL_PORT: int
    MAIL_PASSWORD: str
    MAIL_SENDER: EmailStr


settings = Settings()
