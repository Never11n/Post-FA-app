from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class PostCreate(BaseModel):
    title: str
    content: str


class PostOut(BaseModel):
    id: int
    creator_id: int
    title: str
    content: str
    created_at: datetime


class TokenData(BaseModel):
    id: Optional[str] = None

