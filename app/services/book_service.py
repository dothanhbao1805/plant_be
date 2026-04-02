import uuid

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.book import Book
from app.repositories import book_repo
from app.schemas.book import BookCreate, BookUpdate


def create_book(db: Session, data: BookCreate) -> Book:
    existing = book_repo.get_book_by_title(db, data.title)
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Tiêu đề đã được sử dụng",
        )

    return book_repo.create_book(db, data.title, data.author, data.price, data.quantity)


def get_all_books(db: Session, skip: int = 0, limit: int = 100) -> list[Book]:
    return book_repo.get_all_books(db, skip, limit)


def get_book(db: Session, book_id: uuid.UUID) -> Book:
    book = book_repo.get_book_by_id(db, book_id)
    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Không tìm thấy sách",
        )
    return book


def update_book(db: Session, book_id: uuid.UUID, data: BookUpdate) -> Book:
    book = get_book(db, book_id)
    # Chỉ update các field được gửi lên, bỏ qua field None
    update_data = data.model_dump(exclude_unset=True)
    return book_repo.update_book(db, book, update_data)


def delete_book(db: Session, book_id: uuid.UUID) -> None:
    book = get_book(db, book_id)
    book_repo.delete_book(db, book)
