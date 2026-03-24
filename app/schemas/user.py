from pydantic import BaseModel, EmailStr
import uuid
from datetime import datetime


class UserCreate(BaseModel):
    email: EmailStr
    password: str
    full_name: str | None = None


class UserResponse(BaseModel):
    id: uuid.UUID
    email: str
    full_name: str | None
    is_active: bool
    created_at: datetime

    model_config = {"from_attributes": True}
