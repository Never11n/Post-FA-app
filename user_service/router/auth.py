from fastapi import Depends, status, HTTPException
from fastapi.routing import APIRouter
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from sqlalchemy import select, or_
from sqlalchemy.ext.asyncio import AsyncSession

from user_service.utils import hash_password, verify, send_email
from user_service.router.oauth2 import create_access_token
from user_service.schemas import UserCreate, UserOut
from user_service.db import get_session
from user_service.models import User

router = APIRouter(prefix="/auth")


@router.post('/signup/', response_model=UserOut, status_code=status.HTTP_201_CREATED)
async def signup(user: UserCreate, db: AsyncSession = Depends(get_session)):
    query = select(User).where(or_(User.email == user.email, User.username == user.username))
    response = await db.execute(query)
    existing_user = response.scalar_one_or_none()
    if existing_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username already exists")

    hashed_password = hash_password(user.password)
    new_user = User(username=user.username, email=user.email, hashed_password=hashed_password)
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    await send_email(f'Welcome to our service!{user.username}', user.email)
    return new_user


@router.post('/login/')
async def login(user_data: OAuth2PasswordRequestForm = Depends(), db: AsyncSession = Depends(get_session)):
    query = select(User).where(User.username == user_data.username)
    result = await db.execute(query)
    user = result.scalar_one_or_none()
    if user and verify(user_data.password, user.hashed_password):
        access_token = await create_access_token(data={'user_id': user.id})
        return {"access_token": access_token, "token_type": "bearer"}
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credentials")

