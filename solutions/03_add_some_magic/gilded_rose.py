class GildedRose(object):
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            self._update_item(item)

    def _update_item(self, item):
        if item.name == "Sulfuras, Hand of Ragnaros":
            ItemUpdate(item).update()
        elif item.name == "Aged Brie":
            AgedBrieUpdate(item).update()
        elif item.name.startswith("Backstage passes"):
            BackstagePassUpdate(item).update()
        elif item.name.startswith("Conjured"):
            ConjuredItemUpdate(item).update()
        else:
            NormalItemUpdate(item).update()


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


class ItemUpdate:
    def __init__(self, item):
        self.item = item

    def update(self):
        pass

    def _modify_quality_and_sell_in(self, quality_modifier):
        self.item.quality = max(min(50, self.item.quality + quality_modifier), 0)
        self.item.sell_in -= 1


class AgedBrieUpdate(ItemUpdate):
    def update(self):
        if self.item.sell_in > 0:
            quality_modifier = 1
        else:
            quality_modifier = 2
        self._modify_quality_and_sell_in(quality_modifier)


class BackstagePassUpdate(ItemUpdate):
    def update(self):
        if self.item.sell_in > 10:
            quality_modifier = 1
        elif self.item.sell_in > 5:
            quality_modifier = 2
        elif self.item.sell_in > 0:
            quality_modifier = 3
        else:
            quality_modifier = -self.item.quality
        self._modify_quality_and_sell_in(quality_modifier)


class ConjuredItemUpdate(ItemUpdate):
    def update(self):
        if self.item.sell_in > 0:
            quality_modifier = -2
        else:
            quality_modifier = -4
        self._modify_quality_and_sell_in(quality_modifier)


class NormalItemUpdate(ItemUpdate):
    def update(self):
        if self.item.sell_in > 0:
            quality_modifier = -1
        else:
            quality_modifier = -2
        self._modify_quality_and_sell_in(quality_modifier)
