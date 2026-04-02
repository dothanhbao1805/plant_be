import uuid

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.deps import get_db, require_role
from app.models.user import User, UserRole
from app.schemas.book import BookCreate, BookResponse, BookUpdate
from app.services import book_service

router = APIRouter(prefix="/books", tags=["books"])


@router.get("/", response_model=list[BookResponse])
def get_books(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return book_service.get_all_books(db, skip, limit)


@router.get("/{book_id}", response_model=BookResponse)
def get_book(book_id: uuid.UUID, db: Session = Depends(get_db)):
    return book_service.get_book(db, book_id)


@router.post("/", response_model=BookResponse, status_code=201)
def create_book(data: BookCreate, db: Session = Depends(get_db)):
    return book_service.create_book(db, data)


@router.put("/{book_id}", response_model=BookResponse)
def update_book(book_id: uuid.UUID, data: BookUpdate, db: Session = Depends(get_db)):
    return book_service.update_book(db, book_id, data)


@router.delete("/{book_id}", status_code=204)
def delete_book(
    book_id: uuid.UUID,
    db: Session = Depends(get_db),
    _: User = Depends(require_role(UserRole.admin)),
):
    book_service.delete_book(db, book_id)
