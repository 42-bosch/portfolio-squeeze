from sqlalchemy import Column, Integer, String
from app.data_base import Base

class Car(Base):
    __tablename__ = "cars"
    id = Column(Integer, primary_key=True, index=True)
    year = Column(Integer, index=True)
    make = Column(String, index=True)
    model = Column(String, index=True)
    module_Supported = Column(String, index=True)
    important_Coverage_Notes = Column(String, index=True)
    market = Column(String, index=True)
