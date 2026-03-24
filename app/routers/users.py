# app/routers/users.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.deps import get_db
from app.schemas.user import UserCreate, UserResponse
from app.services import user_service

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/")
def get_users():
    return {"message": "users route working"}


@router.post("/", response_model=UserResponse, status_code=201)
def create_user(data: UserCreate, db: Session = Depends(get_db)):
    return user_service.create_user(db, data)
