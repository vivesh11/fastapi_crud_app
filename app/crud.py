# === app/crud.py ===
from .models import Item

fake_db: dict[int, Item] = {}

def create_item(item: Item) -> Item:
    fake_db[item.id] = item
    return item

def read_item(item_id: int) -> Item | None:
    return fake_db.get(item_id)

def update_item(item_id: int, item: Item) -> Item:
    fake_db[item_id] = item
    return item

def delete_item(item_id: int) -> bool:
    return fake_db.pop(item_id, None) is not None
