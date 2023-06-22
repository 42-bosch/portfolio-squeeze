from fastapi import APIRouter
from ..controllers import car_controller

car_router = APIRouter()


@car_router.get("/cars")
async def get_cars():
    return car_controller.get_cars()
