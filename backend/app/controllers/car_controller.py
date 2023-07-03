from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.models.car_model import Car
from ..schemas.car_schema import CarCreate


def get_car(car_id: int, db: Session):
	car = db.query(Car).filter(Car.id == car_id).first()
	if not car:
		raise HTTPException(
			status_code=status.HTTP_404_NOT_FOUND, detail="Car not found"
		)
	return car


def get_cars(db: Session):
	cars = db.query(Car).all()
	return cars


def get_car_by_maker(maker: str, db: Session):
	car = db.query(Car).filter(Car.maker == maker).first()
	if not car:
		raise HTTPException(
			status_code=status.HTTP_404_NOT_FOUND, detail="Car not found"
		)
	return car


def create_car(car: CarCreate, db: Session):
	db_car = Car(
		maker = car.maker,
		quantity = car.quantity,
		year_birth = car.year_birth,
	)
	try:
		db.add(db_car)
		db.commit()
		db.refresh(db_car)
		return db_car
	except:
		raise HTTPException(
			status_code=status.HTTP_400_BAD_REQUEST, detail="Car already exists"
		)


def update_car(car_id: int, car: CarCreate, db: Session):
	db_car = db.query(Car).filter(Car.id == car_id).first()
	if not db_car:
		raise HTTPException(
			status_code=status.HTTP_404_NOT_FOUND, detail="Car not found"
		)
	db_car.maker = car.maker
	db_car.quantity = car.quantity
	db_car.year_birth = car.year_birth
	db.commit()
	db.refresh(db_car)
	return db_car


def delete_car(car_id: int, db: Session):
	db_car = db.query(Car).filter(Car.id == car_id).first()
	if not db_car:
		raise HTTPException(
			status_code=status.HTTP_404_NOT_FOUND, detail="Car not found"
		)
	db.delete(db_car)
	db.commit()
	return db_car
