from sqlalchemy.orm import Session

from app.models.book import Book


def get_book_by_id(db: Session, book_id) -> Book | None:
    return db.query(Book).filter(Book.id == book_id).first()


def get_all_books(db: Session, skip: int = 0, limit: int = 100) -> list[Book]:
    return db.query(Book).offset(skip).limit(limit).all()


def get_book_by_title(db: Session, title: str) -> Book | None:
    return db.query(Book).filter(Book.title == title).first()


def create_book(
    db: Session, title: str, author: str, price: float, quantity: int
) -> Book:
    book = Book(title=title, author=author, price=price, quantity=quantity)
    db.add(book)
    db.commit()
    db.refresh(book)
    return book


def update_book(db: Session, book: Book, data: dict) -> Book:
    for field, value in data.items():
        setattr(book, field, value)
    db.commit()
    db.refresh(book)
    return book


def delete_book(db: Session, book: Book) -> None:
    db.delete(book)
    db.commit()
