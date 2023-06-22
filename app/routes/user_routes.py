from fastapi import APIRouter
from ..controllers import user_controller

user_router = APIRouter()


@user_router.get("/users")
async def get_users():
    return user_controller.get_users()
