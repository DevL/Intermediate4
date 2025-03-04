import pytest
from itertools import starmap
from gilded_rose import GildedRose, Item
from typing import Iterable


def test_conjured_item_before_due_date():
    assert_item_update(
        Item(name="Conjured Instructor", sell_in=1, quality=12),
        Item(name="Conjured Instructor", sell_in=0, quality=10),
    )


def test_conjured_item_on_due_date():
    assert_item_update(
        Item(name="Conjured Exercise", sell_in=0, quality=10),
        Item(name="Conjured Exercise", sell_in=-1, quality=6),
    )


def test_conjured_item_after_due_date():
    assert_item_update(
        Item(name="Conjured Solution", sell_in=-1, quality=6),
        Item(name="Conjured Solution", sell_in=-2, quality=2),
    )


def test_conjured_item_of_zero_quality():
    assert_item_update(
        Item(name="Conjured Concept", sell_in=3, quality=0),
        Item(name="Conjured Concept", sell_in=2, quality=0),
    )


def assert_item_update(item: Item, expected: Item) -> bool:
    """
    Update the quality of a single item and compare it to the expected item.
    """
    return update_quality_and_compare(GildedRose(items=[item]), [expected])


def update_quality_and_compare(store: GildedRose, expected: Iterable[Item]) -> bool:
    """
    Updates the quality of all items in the store and compares them to the expected items.
    """
    store.update_quality()
    assert store.items == list(expected)
    return True
