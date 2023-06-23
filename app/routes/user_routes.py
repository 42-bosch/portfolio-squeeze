from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..controllers import user_controller
from ..schemas import user_schema
from ..data_base import get_db

user_router = APIRouter()


@user_router.get("/user/{user_id}", response_model=user_schema.User)
def get_users(user_id: int, db: Session = Depends(get_db)):
    return user_controller.get_user(user_id=user_id, db=db)

@user_router.get("/user/all", response_model=user_schema.User)
def get_users(db: Session = Depends(get_db)):
    return user_controller.get_users(db=db)


@user_router.post("/user", response_model=user_schema.User)
def create_user(user: user_schema.UserCreate, db: Session = Depends(get_db)):
    return user_controller.create_user(user=user, db=db)


@user_router.delete("/user/{user_id}", response_model=user_schema.User)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    return user_controller.delete_user(user_id=user_id, db=db)

@user_router.put("/user/{user_id}", response_model=user_schema.User)
def update_user(user_id: int, user: user_schema.UserCreate, db: Session = Depends(get_db)):
    return user_controller.update_user(user_id=user_id, user=user, db=db)
