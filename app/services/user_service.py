from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.repositories import user_repo
from app.core.security import hash_password
from app.schemas.user import UserCreate
from app.models.user import User


def create_user(db: Session, data: UserCreate) -> User:
    existing = user_repo.get_user_by_email(db, data.email)
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email đã được sử dụng",
        )
    hashed = hash_password(data.password)
    return user_repo.create_user(db, data.email, hashed, data.full_name)
