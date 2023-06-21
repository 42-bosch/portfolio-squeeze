from typing import Annotated
from pydantic import BaseModel


class CarBase(BaseModel):
    year: int
    make: str
    model: str
    module_Supported: str
    important_Coverage_Notes: str
    market: str


class CarCreate(CarBase):
    pass


class Car(CarBase):
    id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str
    permissions: str
    password: str


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: int
    cars: list[Car] = []

    class Config:
        orm_mode = True
