from os import environ
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import jwt
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm


from ..models.user_model import User
from ..schemas.user_schema import UserCreate, UserUpdate, UserLogin


secret_key = environ.get("SECRET_KEY")
algorithm = environ.get("ALGORITHM")
crypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def login_user(user: UserLogin, session_db: Session, expires_delta: int = 30):
    print("entrou no login_user")
    query_user = session_db.query(User)
    db_user = query_user.filter(User.email == user.username).first()

    if db_user is None or not db_user.verify_password(user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credentials icorrect",
        )

    access_token_expires = datetime.utcnow() + timedelta(minutes=expires_delta)
    payload = {
        "sub": db_user.email,
        "exp": access_token_expires,
    }
    access_token = jwt.encode(payload, secret_key, algorithm=algorithm)
    return {
        "access_token": access_token,
        "expires": access_token_expires.isoformat(),
    }


def create_user(user: UserCreate, session_db: Session):
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
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User already exists",
        )


def update_user(id: int, user: UserUpdate, session_db: Session):
    query_user = session_db.query(User)
    db_user = query_user.filter(User.id == id).first()
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )
    db_user.email = user.email
    db_user.username = user.username
    if user.hashed_password:
        db_user.hashed_password = crypt_context.hash(user.hashed_password)
    session_db.commit()
    session_db.refresh(db_user)


def delete_user(id: int, session_db: Session):
    query_user = session_db.query(User)
    db_user = query_user.filter(User.id == id).first()
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )
    session_db.delete(db_user)
    session_db.commit()
