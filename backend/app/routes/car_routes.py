from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from ..schemas import car_schema
from ..controllers import car_controller as car_crud
from ..depends import get_session_current_db, verify_token

car_router = APIRouter()


# GET ONE CAR
@car_router.get("/car/id/{car_id}", response_model=car_schema.Car)
def get_cars(car_id: int, db: Session = Depends(get_session_current_db)):
    return car_crud.get_car(car_id=car_id, db=db)


# GET ALL CARS
@car_router.get("/cars", response_model=List[car_schema.Car])
def get_cars(db: Session = Depends(get_session_current_db)):
    return car_crud.get_cars(db=db)


# GET CAR BY MAKER
@car_router.get("/car/maker/{maker}", response_model=car_schema.Car)
def get_car_by_maker(maker: str, db: Session = Depends(get_session_current_db)):
    return car_crud.get_car_by_maker(maker=maker, db=db)


# CREATE CAR
@car_router.post("/car", response_model=car_schema.Car, dependencies=[Depends(verify_token)])
def create_car(car: car_schema.CarCreate, db: Session = Depends(get_session_current_db)):
    return car_crud.create_car(car=car, db=db)


# UPDATE CAR
@car_router.put("/car/{car_id}", response_model=car_schema.Car, dependencies=[Depends(verify_token)])
def update_car(car_id: int, car: car_schema.CarCreate, db: Session = Depends(get_session_current_db)):
    return car_crud.update_car(car_id=car_id, car=car, db=db)


# DELETE CAR
@car_router.delete("/car/{car_id}", response_model=car_schema.Car, dependencies=[Depends(verify_token)])
def delete_car(car_id: int, db: Session = Depends(get_session_current_db)):
    return car_crud.delete_car(car_id=car_id, db=db)
