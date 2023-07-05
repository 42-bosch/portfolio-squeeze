from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from typing import Dict

from app.schemas.user_schema import UserBase, UserUpdate
from app.depends import get_session_current_db, verify_token
from app.controllers.user_controller import (
    crud_login_user,
    crud_create_user,
    crud_update_user,
    crud_delete_user,
)

user_router = APIRouter(prefix="/user")


@user_router.post("/login", response_model=Dict[str, str])
def route_login_user(
    user: OAuth2PasswordRequestForm = Depends(),
    session_db: Session = Depends(get_session_current_db),
):
    response = crud_login_user(user=user, session_db=session_db)
    return JSONResponse(content=response, status_code=status.HTTP_200_OK)


@user_router.post("/create", response_model=Dict[str, str])
def route_create_user(
    user: UserBase,
    session_db: Session = Depends(get_session_current_db),
):
    response = crud_create_user(user=user, session_db=session_db)
    return JSONResponse(content=response, status_code=status.HTTP_201_CREATED)


@user_router.delete(
    "/delete", response_model=Dict[str, str],
     dependencies=[Depends(verify_token)]
)
def route_delete_user(
    password: str,
    confirm_password: str,
    current_user=Depends(verify_token),
    session_db: Session = Depends(get_session_current_db),
):
    if password != confirm_password:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Passwords do not match"
        )
    response = crud_delete_user(current_user, password, session_db)
    return JSONResponse(content=response, status_code=status.HTTP_200_OK)


@user_router.put(
    "/uptade/", response_model=Dict[str, str], dependencies=[Depends(verify_token)]
)
def route_update_user(
    password_confirmation: str,
    update_user: UserUpdate,
    current_user=Depends(verify_token),
    session_db: Session = Depends(get_session_current_db),
):
    response = crud_update_user(
        password_confirmation, current_user, update_user, session_db
    )
    return JSONResponse(content=response, status_code=status.HTTP_200_OK)
