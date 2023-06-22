from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound
from fastapi import Depends


from ..models.user_model import User
from ..schemas.user_schema import UserCreate


def get_user(user_id: int, db: Session):
    try:
        return db.query(User).filter(User.id == user_id).first()
    except NoResultFound:
        return None


def get_user_by_email(email: str, db: Session):
    try:
        return db.query(User).filter(User.email == email).first()
    except NoResultFound:
        return None


def create_user(user: UserCreate, db: Session):
    db_user = User(
        email=user.email,
        hashed_password=user.hashed_password,
        permissions=user.permissions
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user(user_id: int, db: Session):
    db_user = db.query(User).filter(User.id == user_id).first()
    db.delete(db_user)
    db.commit()
    return db_user
