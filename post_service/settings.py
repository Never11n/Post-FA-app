from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env')

    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    POST_DATABASE_USERNAME: str
    POST_DATABASE_PASSWORD: str
    POST_DATABASE_NAME: str
    POST_DATABASE_HOST: str
    POST_DATABASE_PORT: int


settings = Settings()
