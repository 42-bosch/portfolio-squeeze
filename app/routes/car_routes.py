from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..schemas import car_schema
from ..controllers import car_controller as car_crud
from ..data_base import get_db

car_router = APIRouter()


@car_router.get("/car/{car_id}", response_model=car_schema.Car)
def get_cars(car_id: int, db: Session = Depends(get_db)):
    return car_crud.get_car(car_id=car_id, db=db)

@car_router.get("/car/all", response_model=car_schema.Car)
def get_cars(db: Session = Depends(get_db)):
    return car_crud.get_cars(db=db)


@car_router.post("/car", response_model=car_schema.Car)
def create_car(car: car_schema.CarCreate, db: Session = Depends(get_db)):
    return car_crud.create_car(car=car, db=db)


@car_router.delete("/car/{car_id}", response_model=car_schema.Car)
def delete_car(car_id: int, db: Session = Depends(get_db)):
    return car_crud.delete_car(car_id=car_id, db=db)

@car_router.put("/car/{car_id}", response_model=car_schema.Car)
def update_car(car_id: int, car: car_schema.CarCreate, db: Session = Depends(get_db)):
    return car_crud.update_car(car_id=car_id, car=car, db=db)


# #GET ONE CAR
# @car_router.get("/cars/{car_id}", response_model=car_schema.Car)
# async def get_one_car(car_id: int, db: Session = Depends(get_db)):
# 	return car_crud.get_car(db, car_id)


# #GET ALL CARS
# @car_router.get("/cars", response_model=list[car_schema.Car])
# def get_cars_all(db: Session = Depends(get_db)):
# 	return get_cars_all(db)


# #CREATE ONE CAR
# @car_router.post("/cars", response_model=car_schema.Car)
# async def create_one_car(car: car_schema.Car, db: Session = Depends(get_db)):
# 	return car_crud.create_car(car.dict(), db)


# #UPDATE ONE CAR
# @car_router.put("/cars/{car_id}", response_model=car_schema.Car)
# async def update_one_car(car: car_schema.Car, car_id: int, db: Session = Depends(get_db)):
# 	return car_crud.update_car(car.dict(), car_id, db)


# #DELETE ONE CAR
# @car_router.delete("/cars/{car_id}", response_model=car_schema.Car)
# def delete_single_car(car_id: int, db: Session = Depends(get_db)):
#     return car_crud.delete_car(db, car_id)
