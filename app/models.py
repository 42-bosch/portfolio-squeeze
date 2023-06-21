from sqlalchemy import Column, Integer, String
from .database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    permissions = Column(String, index=True)


class Car(Base):
    __tablename__ = "cars"

    id = Column(Integer, primary_key=True, index=True)
    year = Column(Integer, index=True)
    make = Column(String, index=True)
    model = Column(String, index=True)
    module_Supported = Column(String, index=True)
    important_Coverage_Notes = Column(String, index=True)
    market = Column(String, index=True)
