from fastapi import FastAPI

from user_service.models import Base
from user_service.db import engine
from user_service.router import auth_router

app = FastAPI()

@app.on_event("startup")
async def init_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

app.include_router(auth_router)

