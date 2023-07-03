from os import environ
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import jwt

from app.models.user_model import User
from app.schemas.user_schema import UserBase, UserUpdate, UserLogin


secret_key = environ.get("SECRET_KEY")
algorithm = environ.get("ALGORITHM")
crypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def crud_login_user(user: UserLogin, session_db: Session, expires_delta: int = 30):
    print("entrou no login_user")
    query_user = session_db.query(User)
    db_user = query_user.filter(User.email == user.username).first()

    if db_user is None or not db_user.verify_password(user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Credentials icorrect"
        )

    access_token_expires = datetime.utcnow() + timedelta(minutes=expires_delta)
    payload = {
        "sub": db_user.email,
        "exp": access_token_expires,
    }
    access_token = jwt.encode(payload, secret_key, algorithm=algorithm)
    return {"access_token": access_token, "expires": access_token_expires.isoformat()}


def crud_create_user(user: UserBase, session_db: Session):
    db_user = User(
        email=user.email,
        username=user.username,
        hashed_password=crypt_context.hash(user.hashed_password),
    )
    try:
        session_db.add(db_user)
        session_db.commit()
        session_db.refresh(db_user)
    except:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="User already exists"
        )
    return {"message": "User created successfully"}


def crud_update_user(
    password_confirmation: str,
    current_user: UserBase,
    update_user: UserUpdate,
    session_db: Session,
):
    if not current_user.verify_password(password_confirmation):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Password incorrect"
        )
    if update_user.email:
        current_user.email = update_user.email
    if update_user.username:
        current_user.username = update_user.username
    if update_user.password:
        current_user.hashed_password = crypt_context.hash(update_user.password)
        print("entrou no update_user.password")
    session_db.commit()

    return {"message": "User updated successfully"}


def crud_delete_user(user, password: str, session_db: Session):
    if not user.verify_password(password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Password incorrect"
        )
    session_db.delete(user)
    session_db.commit()
    return {"message": "User deleted successfully"}
