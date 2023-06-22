from fastapi import APIRouter, Depends


from ..controllers import user_controller
from ..schemas import user_schema

from ..data_base import get_db

user_router = APIRouter()


@user_router.get("/users")
async def get_users(id:int):
    return user_controller.get_user(id)


@user_router.post("/users", response_model=user_schema.UserCreate)
async def create_user(user: user_schema.UserCreate, db=Depends(get_db)):
    return user_controller.create_user(user, db)
