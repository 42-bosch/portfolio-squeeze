from pydantic import BaseModel
from .car_schema import Car

class UserBase(BaseModel):
    email: str
    permissions: str = "user"
    hashed_password: str


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: int
    cars: list[Car] = []

    class Config:
        orm_mode = True
