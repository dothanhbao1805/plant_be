from pydantic import BaseModel
import uuid


class BookCreate(BaseModel):
    title: str
    author: str
    price: float
    quantity: int


class BookUpdate(BaseModel):
    title: str | None = None
    author: str | None = None
    price: float | None = None
    quantity: int | None = None


class BookResponse(BaseModel):
    id: uuid.UUID
    title: str
    author: str
    price: float
    quantity: int

    model_config = {"from_attributes": True}
