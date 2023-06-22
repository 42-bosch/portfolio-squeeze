from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound

from ..models.car_model import Car

def get_car(db: Session, car_id: int):
    try:
        return db.query(Car).filter(Car.id == car_id).first()
    except NoResultFound:
        return None
