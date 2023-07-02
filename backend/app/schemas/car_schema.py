from pydantic import BaseModel


class CarBase(BaseModel):
    maker:str
    quantity:int
    year_birth:int


class CarCreate(CarBase):
    pass


class Car(CarBase):
    id: int

    class Config:
        orm_mode = True
