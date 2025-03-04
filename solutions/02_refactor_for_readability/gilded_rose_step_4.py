class GildedRose(object):
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            self._update_item(item)

    def _update_item(self, item):
        if item.name == "Sulfuras, Hand of Ragnaros":
            self._legendary_item_update(item)
        elif item.name == "Aged Brie":
            self._aged_brie_update(item)
        elif item.name == "Backstage passes to a TAFKAL80ETC concert":
            self._backstage_pass_update(item)
        else:
            self._normal_item_update(item)

    def _aged_brie_update(self, item):
        if item.sell_in > 0:
            quality_modifier = 1
        else:
            quality_modifier = 2
        self._modify_quality_and_sell_in(item, quality_modifier)

    def _backstage_pass_update(self, item):
        if item.sell_in > 10:
            quality_modifier = 1
        elif item.sell_in > 5:
            quality_modifier = 2
        elif item.sell_in > 0:
            quality_modifier = 3
        else:
            quality_modifier = -item.quality
        self._modify_quality_and_sell_in(item, quality_modifier)

    def _legendary_item_update(self, _item):
        pass

    def _normal_item_update(self, item):
        if item.sell_in > 0:
            quality_modifier = -1
        else:
            quality_modifier = -2
        self._modify_quality_and_sell_in(item, quality_modifier)

    def _modify_quality_and_sell_in(self, item, quality_modifier):
        item.quality = max(min(50, item.quality + quality_modifier), 0)
        item.sell_in -= 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __eq__(self, other):
        return all(
            [
                self.name == other.name,
                self.sell_in == other.sell_in,
                self.quality == other.quality,
            ]
        )

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
