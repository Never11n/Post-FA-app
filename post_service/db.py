from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from post_service.settings import settings

SQLALCHEMY_DATABASE_URL = (f"postgresql+asyncpg://"
                           f"{settings.POST_DATABASE_USERNAME}:{settings.POST_DATABASE_PASSWORD}@"
                           f"{settings.POST_DATABASE_HOST}:{settings.POST_DATABASE_PORT}"
                           f"/{settings.POST_DATABASE_NAME}")

engine = create_async_engine(SQLALCHEMY_DATABASE_URL, echo=True)

SessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False, )

Base = declarative_base()


async def get_session() -> AsyncSession:
    async with SessionLocal() as session:
        yield session
