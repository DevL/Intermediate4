import pytest
from itertools import starmap
from gilded_rose import GildedRose, Item
from typing import Iterable


def test_normal_item_before_due_date_withhout_using_helper_functions():
    """
    This test can be deleted in favour of the one that follows.
    It only is present here to demonstrate the utility of introducing
    test helper functions.
    """
    store = GildedRose([Item(name="normal", sell_in=1, quality=5)])
    store.update_quality()
    assert store.items[0].name == "normal"
    assert store.items[0].sell_in == 0
    assert store.items[0].quality == 4


def test_normal_item_before_due_date():
    update_quality_and_compare(
        GildedRose([Item(name="normal", sell_in=1, quality=5)]),
        [Item(name="normal", sell_in=0, quality=4)],
    )


def test_normal_item_before_due_date():
    assert_item_update(
        Item(name="normal", sell_in=1, quality=5),
        Item(name="normal", sell_in=0, quality=4),
    )


@pytest.mark.skip(reason="Pending")
def test_normal_item_on_due_date():
    pass


@pytest.mark.skip(reason="Pending")
def test_normal_item_after_due_date():
    pass


@pytest.mark.skip(reason="Pending")
def test_normal_item_of_zero_quality():
    pass


@pytest.mark.skip(reason="Pending")
def test_brie_before_due_date():
    pass


@pytest.mark.skip(reason="Pending")
def test_brie_before_due_date_with_max_quality():
    pass


@pytest.mark.skip(reason="Pending")
def test_brie_on_due_date():
    pass


@pytest.mark.skip(reason="Pending")
def test_brie_on_due_date_close_to_max_quality():
    pass


@pytest.mark.skip(reason="Pending")
def test_brie_on_due_date_with_max_quality():
    pass


@pytest.mark.skip(reason="Pending")
def test_sulfuras_before_due_date():
    pass


@pytest.mark.skip(reason="Pending")
def test_sulfuras_on_due_date():
    pass


@pytest.mark.skip(reason="Pending")
def test_sulfuras_after_due_date():
    pass


@pytest.mark.skip(reason="Pending")
def test_backstage_pass_long_before_concert():
    pass


@pytest.mark.skip(reason="Pending")
def test_backstage_pass_long_before_concert_maximum_quality():
    pass


@pytest.mark.skip(reason="Pending")
def test_backstage_pass_close_to_concert_upper_bound():
    pass


@pytest.mark.skip(reason="Pending")
def test_backstage_pass_close_to_concert_upper_bound_maximum_quality():
    pass


@pytest.mark.skip(reason="Pending")
def test_backstage_pass_close_to_concert_lower_bound():
    pass


@pytest.mark.skip(reason="Pending")
def test_backstage_pass_close_to_concert_lower_bound_maximum_quality():
    pass


@pytest.mark.skip(reason="Pending")
def test_backstage_pass_very_close_to_concert_upper_bound():
    pass


@pytest.mark.skip(reason="Pending")
def test_backstage_pass_very_close_to_concert_upper_bound_maximum_quality():
    pass


@pytest.mark.skip(reason="Pending")
def test_backstage_pass_very_close_to_concert_lower_bound():
    pass


@pytest.mark.skip(reason="Pending")
def test_backstage_pass_very_close_to_concert_lower_bound_maximum_quality():
    pass


@pytest.mark.skip(reason="Pending")
def test_backstage_pass_by_concert():
    pass


@pytest.mark.skip(reason="Pending")
def test_backstage_pass_after_concert():
    pass


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
    return compare_items(store.items, expected)


def compare_items(actual_items: Iterable[Item], expected_items: Iterable[Item]) -> bool:
    """
    Compare two iterables containing Item instances. The order must match.

    Implementing Item.__eq__ will make this redundant in a later step.
    """
    return all(starmap(_compare_item, zip(actual_items, expected_items)))


def _compare_item(actual: Item, expected: Item) -> bool:
    """
    Compare two Item instances based on their attributes.

    Implementing Item.__eq__ will make this redundant in a later step.
    """
    assert actual.name == expected.name
    assert actual.sell_in == expected.sell_in
    assert actual.quality == expected.quality
    return True
