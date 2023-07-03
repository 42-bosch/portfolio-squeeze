from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm

from ..controllers import user_controller
from ..schemas import user_schema
from ..depends import get_session_current_db

user_router = APIRouter(prefix="/user")


@user_router.post("/login")
def login_user(
    user: OAuth2PasswordRequestForm = Depends(),
    session_db: Session = Depends(get_session_current_db),
):
    response = user_controller.login_user(user=user, session_db=session_db)
    return JSONResponse(
        content=response,
        status_code=status.HTTP_200_OK,
    )


@user_router.post("/create", response_model=user_schema.User)
def create_user(
    user: user_schema.UserCreate,
    session_db: Session = Depends(get_session_current_db),
):
    user_controller.create_user(user=user, session_db=session_db)
    return JSONResponse(
        content={"message": "User created successfully"},
        status_code=status.HTTP_201_CREATED,
    )


@user_router.delete("/delete/{id}", response_model=user_schema.User)
def delete_user(
    id: int,
    session_db: Session = Depends(get_session_current_db),
):
    deleted_user = user_controller.delete_user(id=id, session_db=session_db)
    return JSONResponse(
        content={
            "message": "User deleted successfully",
            "user": deleted_user,
        },
        status_code=status.HTTP_200_OK,
    )


@user_router.put("/uptade/{id}", response_model=user_schema.User)
def update_user(
    id: int,
    user_schema: user_schema.UserUpdate,
    session_db: Session = Depends(get_session_current_db),
):
    user_controller.update_user(
        id=id,
        user=user_schema,
        session_db=session_db,
    )
    return JSONResponse(
        content={"message": "User updated successfully"},
        status_code=status.HTTP_200_OK,
    )
