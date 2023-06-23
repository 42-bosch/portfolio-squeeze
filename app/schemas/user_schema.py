from pydantic import BaseModel
from typing import Optional

class UserBase(BaseModel):
    email: str
    permissions: Optional[str] = "user"
    hashed_password: str


class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int

    class Config:
        orm_mode = True
