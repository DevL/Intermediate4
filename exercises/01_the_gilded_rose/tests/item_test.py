import pytest
from gilded_rose import Item


def test_creating_an_item():
    item = Item(name="Instructor", sell_in=3, quality=5)
    assert item.name == "Instructor"
    assert item.sell_in == 3
    assert item.quality == 5


@pytest.mark.xfail(reason="Item does not implement __eq__ yet...")
def test_equality():
    item = Item(name="Instructor", sell_in=3, quality=5)
    similar_item = Item(name="Instructor", sell_in=3, quality=5)
    different_item = Item(name="Horse", sell_in=100, quality=50)
    assert item == similar_item
    assert item != different_item
