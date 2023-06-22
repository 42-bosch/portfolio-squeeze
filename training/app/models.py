from sqlalchemy.sql.expression import null
from database import Base
from sqlalchemy import String,Integer,Column,Text


class Item(Base):
    __tablename__='items'
    id=Column(Integer,primary_key=True)
    maker=Column(String(255),nullable=False,unique=True)
    quantity=Column(Integer,nullable=False)
    year_birth=Column(Integer,nullable=False)


    def __repr__(self):
        return f"<Item maker={self.maker} quantity={self.quantity}>"