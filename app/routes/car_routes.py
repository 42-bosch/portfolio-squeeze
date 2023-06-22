from fastapi import APIRouter
from ..controllers import car_controller

car_router = APIRouter()


@car_router.get("/cars")
async def get_cars():
    return car_controller.get_cars()

@car_router.post("/cars")
async def create_car(car):
    return car_controller.create_car(car)
