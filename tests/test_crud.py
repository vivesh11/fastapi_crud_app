# === tests/test_crud.py ===
from app.models import Item
from app.crud import create_item, read_item, update_item, delete_item

def test_create_item():
    item = Item(id=1, name="Test Item")
    result = create_item(item)
    assert result.id == 1


def test_read_item():
    item = Item(id=2, name="Read Test")
    create_item(item)
    result = read_item(2)
    assert result is not None
    assert result.name == "Read Test"


def test_update_item():
    item = Item(id=3, name="Old")
    create_item(item)
    updated = Item(id=3, name="Updated")
    result = update_item(3, updated)
    assert result.name == "Updated"


def test_delete_item():
    item = Item(id=4, name="Delete Me")
    create_item(item)
    success = delete_item(4)
    assert success
    assert read_item(4) is None
