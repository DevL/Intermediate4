import pytest
from gilded_rose import GildedRose, Item


def test_the_gilded_rose_can_have_items():
    items = [Item(name="Instructor", sell_in=3, quality=5)]
    store = GildedRose(items)
    assert store.items == items


def test_the_gilded_rose_can_have_items_that_age():
    items = [Item(name="Instructor", sell_in=3, quality=5)]
    store = GildedRose(items)
    store.update_quality()
    assert len(store.items) == 1
    updated_item = store.items[0]
    assert updated_item.name == "Instructor"
    assert updated_item.sell_in == 2
    assert updated_item.quality == 4


@pytest.mark.xfail(reason="Item does not implement __eq__ yet...")
def test_checking_updated_items_using_equality():
    items = [Item(name="Instructor", sell_in=3, quality=5)]
    store = GildedRose(items)
    store.update_quality()

    expected_items = [Item(name="Instructor", sell_in=2, quality=4)]
    assert store.items == expected_items
