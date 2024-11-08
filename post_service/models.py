from sqlalchemy import String, DateTime, func
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import Mapped


class Base(DeclarativeBase):
    pass


class Post(Base):
    __tablename__ = "posts"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    content: Mapped[str] = mapped_column(String(5000), nullable=False)
    created_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    user_id: Mapped[int] = mapped_column(nullable=False)
