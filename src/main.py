from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel


class Item(BaseModel):
    name:str
    description:Optional[str]=None
    price = float
    tax: Optional[float]=None



app = FastAPI()


@app.get('/')
async def root():
    return {'message':'Hello World'}

@app.post('/items')
async def create_item(item:Item):
    item.name.capitalize
    print(item)
    return item