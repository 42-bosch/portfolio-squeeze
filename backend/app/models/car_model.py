from sqlalchemy import Column, Integer, String
from ..database import Base

class Car(Base):
	__tablename__ = "cars"
	id = Column(Integer, primary_key=True, index=True)
	maker = Column(String, nullable=False,unique=True)
	quantity=Column(Integer, nullable=False)
	year_birth=Column(Integer, nullable=False)
