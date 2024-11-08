from fastapi import FastAPI

from post_service.models import Base
from post_service.db import engine

app = FastAPI()


@app.on_event("startup")
async def init_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


@app.get('/')
async def root():
    return {"message": "Hello World"}
