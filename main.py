from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello" : "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id" : item_id, "q" : q}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: str):
    return {"item_id" : item_id, "item" : item}

@app.post("/items/")
def create_item(item: str):
    return {"item" : item}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    return {"item_id" : item_id}