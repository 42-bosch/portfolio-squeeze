from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound
from ..models.car_model import Car
from ..schemas.car_schema import CarCreate

def get_car(db: Session, car_id: int):
    try:
        return db.query(Car).filter(Car.id == car_id).first()
    except NoResultFound:
        return None

def get_all_cars(db: Session):
    return db.query(Car).all()

def create_car(car: CarCreate, db: Session):
    db_car = Car(
        maker=car.maker,
        quantity=car.quantity,
        year_birth=car.year_birth
    )
    db.add(db_car)
    db.commit()
    db.refresh(db_car)
    return db_car

def delete_car(car_id: int, db: Session):
    db_car_del = db.query(Car).filter(Car.id == car_id).first()
    if db_car_del:
        db.delete(db_car_del)
        db.commit()
    return db_car_del

def update_car(car: Car, car_id: int, db: Session):
    db_car_upd = db.query(Car).filter(Car.id == car_id).first()
    db_car_upd.maker=car.maker
    db_car_upd.quantity=car.quantity
    db_car_upd.year_birth=car.year_birth

    db.commit()

    return db_car_upd
