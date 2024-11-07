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

    SMTP_HOST: str
    SMTP_PORT: int
    SMTP_USER: str
    SMTP_PASSWORD: str
    SMTP_FROM_EMAIL: str
    SMTP_TLS: bool = True


settings = Settings()