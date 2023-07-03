from sqlalchemy import Column, Integer, String, DateTime, func
from passlib.hash import bcrypt

from ..database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    username = Column(String, unique=True, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    def verify_password(self, password: str):
        return bcrypt.verify(password, self.hashed_password)
