# === app/main.py ===
from fastapi import FastAPI, HTTPException
from .models import Item
from .crud import create_item, read_item, update_item, delete_item

app = FastAPI()

@app.post("/items/")
def create(item: Item):
    return create_item(item)

@app.get("/items/{item_id}")
def read(item_id: int):
    item = read_item(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.put("/items/{item_id}")
def update(item_id: int, item: Item):
    return update_item(item_id, item)

@app.delete("/items/{item_id}")
def delete(item_id: int):
    if not delete_item(item_id):
        raise HTTPException(status_code=404, detail="Item not found")
    return {"detail": "Deleted successfully"}

