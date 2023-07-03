from re import match as re_match
from pydantic import BaseModel, validator
from typing import Optional

REGEX_EMAIL = r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+"
REGEX_USERNAME = r"^[a-zA-Z0-9_-]{3,15}$"


class UserBase(BaseModel):
    email: str
    username: str
    hashed_password: str

    @validator("username")
    def username_validator(cls, value):
        if not re_match(REGEX_USERNAME, value):
            raise ValueError("Invalid username")
        return value

    @validator("email")
    def email_validator(cls, value):
        if not re_match(REGEX_EMAIL, value):
            raise ValueError("Invalid email address")
        return value


class UserLogin(BaseModel):
    email: str
    hashed_password: str

class UserUpdate(BaseModel):
    email: Optional[str]
    username: Optional[str]
    password: Optional[str]

    @validator("username")
    def username_validator(cls, value):
        if not re_match(REGEX_USERNAME, value) and value != "":
            raise ValueError("Invalid username")
        return value

    @validator("email")
    def email_validator(cls, value):
        if not re_match(REGEX_EMAIL, value) and value != "":
            raise ValueError("Invalid email address")
        return value



class User(UserBase):
    id: int

    class Config:
        orm_mode = True
