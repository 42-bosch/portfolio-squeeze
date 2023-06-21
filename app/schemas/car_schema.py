from pydantic import BaseModel


class CarBase(BaseModel):
    year: int
    make: str
    model: str
    module_Supported: str
    important_Coverage_Notes: str = None
    market: str


class CarCreate(CarBase):
    pass


class Car(CarBase):
    id: int

    class Config:
        orm_mode = True
