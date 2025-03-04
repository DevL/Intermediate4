import pytest
from itertools import starmap
from gilded_rose import GildedRose, Item
from typing import Iterable


def test_normal_item_before_due_date():
    assert_item_update(
        Item(name="normal", sell_in=1, quality=6),
        Item(name="normal", sell_in=0, quality=5),
    )


def test_normal_item_on_due_date():
    assert_item_update(
        Item(name="normal", sell_in=0, quality=5),
        Item(name="normal", sell_in=-1, quality=3),
    )


def test_normal_item_after_due_date():
    assert_item_update(
        Item(name="normal", sell_in=-1, quality=3),
        Item(name="normal", sell_in=-2, quality=1),
    )


def test_normal_item_of_zero_quality():
    assert_item_update(
        Item(name="normal", sell_in=3, quality=0),
        Item(name="normal", sell_in=2, quality=0),
    )


def test_brie_before_due_date():
    assert_item_update(
        Item(name="Aged Brie", sell_in=1, quality=3),
        Item(name="Aged Brie", sell_in=0, quality=4),
    )


def test_brie_before_due_date_with_max_quality():
    assert_item_update(
        Item(name="Aged Brie", sell_in=1, quality=50),
        Item(name="Aged Brie", sell_in=0, quality=50),
    )


def test_brie_on_due_date():
    assert_item_update(
        Item(name="Aged Brie", sell_in=0, quality=3),
        Item(name="Aged Brie", sell_in=-1, quality=5),
    )


def test_brie_on_due_date_close_to_max_quality():
    assert_item_update(
        Item(name="Aged Brie", sell_in=0, quality=49),
        Item(name="Aged Brie", sell_in=-1, quality=50),
    )


def test_brie_on_due_date_with_max_quality():
    assert_item_update(
        Item(name="Aged Brie", sell_in=0, quality=50),
        Item(name="Aged Brie", sell_in=-1, quality=50),
    )


def test_sulfuras_before_due_date():
    assert_item_update(
        Item(name="Sulfuras, Hand of Ragnaros", sell_in=1, quality=80),
        Item(name="Sulfuras, Hand of Ragnaros", sell_in=1, quality=80),
    )


def test_sulfuras_on_due_date():
    assert_item_update(
        Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
        Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
    )


def test_sulfuras_after_due_date():
    assert_item_update(
        Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
        Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
    )


def test_backstage_pass_long_before_concert():
    assert_item_update(
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=11, quality=12),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=13),
    )


def test_backstage_pass_long_before_concert_maximum_quality():
    assert_item_update(
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=11, quality=50),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=50),
    )


def test_backstage_pass_close_to_concert_upper_bound():
    assert_item_update(
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=13),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=9, quality=15),
    )


def test_backstage_pass_close_to_concert_upper_bound_maximum_quality():
    assert_item_update(
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=50),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=9, quality=50),
    )


def test_backstage_pass_close_to_concert_lower_bound():
    assert_item_update(
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=6, quality=21),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=23),
    )


def test_backstage_pass_close_to_concert_lower_bound_maximum_quality():
    assert_item_update(
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=6, quality=50),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=50),
    )


def test_backstage_pass_very_close_to_concert_upper_bound():
    assert_item_update(
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=23),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=4, quality=26),
    )


def test_backstage_pass_very_close_to_concert_upper_bound_maximum_quality():
    assert_item_update(
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=50),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=4, quality=50),
    )


def test_backstage_pass_very_close_to_concert_lower_bound():
    assert_item_update(
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=1, quality=35),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=0, quality=38),
    )


def test_backstage_pass_very_close_to_concert_lower_bound_maximum_quality():
    assert_item_update(
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=1, quality=50),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=0, quality=50),
    )


def test_backstage_pass_by_concert():
    assert_item_update(
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=0, quality=38),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=-1, quality=0),
    )


def test_backstage_pass_after_concert():
    """
    Note that a backstage pass item can be created with a quality above 0 and a negative sell_in value.
    This test ensures that such items will still have their quality set to 0.
    """
    assert_item_update(
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=-1, quality=7),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=-2, quality=0),
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
