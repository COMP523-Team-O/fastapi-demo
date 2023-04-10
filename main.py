from fastapi import FastAPI, Path
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: int

items = {}

@app.get("/")  
def home():
    return {"Hello": "world!"}

@app.get("/get-item/{item_id}")
def get_item(item_id: int = Path(description="The item ID you requested")):
    return items[item_id]

@app.get("/get-by-name")
def get_by_name(name: str = None):
    for item_id in items:
        if items[item_id]["name"] == name:
            return items[item_id]
        return {"Item": "Not found"}
    
@app.post("/create-item/{item_id}")
def create_item(item_id: int, item: Item):
    if item_id in items:
        return {"Error": "ID already exists"}
    items[item_id] = {"name": item.name, "price": item.price}
    return items[item_id]

@app.put("/update-item/{item_id}")
def update_item(item_id: int, item: Item):
    if item_id not in items:
        return {"Error": "ID does not exist"}
    items[item_id] = item
    return items[item_id]

@app.delete("/delete-item")
def delete_item(item_id: int):
    if item_id not in items:
        return {"Error": "ID not in items"}
    del items[item_id]
    return {"Success": "Item deleted"}