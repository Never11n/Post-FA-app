from typing import Optional

from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    email: EmailStr
    username: str
    password: str


class UserOut(BaseModel):
    id: int
    email: EmailStr
    username: str

    class Config:
        orm_mode = True


class TokenData(BaseModel):
    id: Optional[str] = None
