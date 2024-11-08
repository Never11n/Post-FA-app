import httpx

from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from post_service.db import get_session
from post_service.models import Post
from post_service.schemas import PostCreate, PostOut
from post_service.utils import get_current_user

router = APIRouter(prefix='/posts')

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')


@router.post('/create/', response_model=PostOut, status_code=status.HTTP_201_CREATED)
async def create_post(
        post_data: PostCreate,
        db: AsyncSession = Depends(get_session),
        user_id: int = Depends(get_current_user)):
    query = select(Post).where(Post.title == post_data.title)
    response = await db.execute(query)
    existing_post = response.scalar_one_or_none()
    if existing_post:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Post with this title already exists")
    post = Post(**post_data.model_dump(), user_id=user_id)
    db.add(post)
    await db.commit()
    await db.refresh(post)
    return post
