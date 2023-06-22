from fastapi import FastAPI,status,HTTPException
from pydantic import BaseModel
from typing import Optional,List
from database import SessionLocal
import models

app=FastAPI()

class Item(BaseModel): #serializer
    id:int
    maker:str
    quantity:int
    year_birth:int

    class Config:
        orm_mode=True


db=SessionLocal()

@app.get('/items',response_model=List[Item],status_code=200)
def get_all():
    items=db.query(models.Item).all()

    return items

@app.get('/item/{item_id}',response_model=Item,status_code=status.HTTP_200_OK)
def get_one(item_id:int):
    item=db.query(models.Item).filter(models.Item.id==item_id).first()
    return item

@app.post('/items',response_model=Item,
        status_code=status.HTTP_201_CREATED)
def create_one(item:Item):
    db_item=db.query(models.Item).filter(models.Item.maker==item.maker).first()

    if db_item is not None:
        raise HTTPException(status_code=400,detail="Item already exists")


    new_item=models.Item(
        maker=item.maker,
        quantity=item.quantity,
        year_birth=item.year_birth,
    )


    
    db.add(new_item)
    db.commit()

    return new_item

@app.put('/item/{item_id}',response_model=Item,status_code=status.HTTP_200_OK)
def update_one(item_id:int,item:Item):
    item_to_update=db.query(models.Item).filter(models.Item.id==item_id).first()
    item_to_update.maker=item.maker
    item_to_update.quantity=item.quantity
    item_to_update.year_birth=item.year_birth

    db.commit()

    return item_to_update

@app.delete('/item/{item_id}')
def delete_one(item_id:int):
    item_to_delete=db.query(models.Item).filter(models.Item.id==item_id).first()

    if item_to_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Resource Not Found")
    
    db.delete(item_to_delete)
    db.commit()

    return item_to_delete
