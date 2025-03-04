class GildedRose(object):
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            self._update_item(item)

    def _update_item(self, item):
        if item.name == "Sulfuras, Hand of Ragnaros":
            return

        elif item.name == "Aged Brie":
            if item.sell_in > 0:
                quality_modifier = 1
            else:
                quality_modifier = 2

            item.quality = max(min(50, item.quality + quality_modifier), 0)
            item.sell_in -= 1
            return

        elif item.name == "Backstage passes to a TAFKAL80ETC concert":
            if item.sell_in > 10:
                quality_modifier = 1
            elif item.sell_in > 5:
                quality_modifier = 2
            elif item.sell_in > 0:
                quality_modifier = 3
            else:
                quality_modifier = -item.quality

            item.quality = max(min(50, item.quality + quality_modifier), 0)
            item.sell_in -= 1
            return

        else:
            if item.sell_in > 0:
                quality_modifier = -1
            else:
                quality_modifier = -2
            item.quality = max(min(50, item.quality + quality_modifier), 0)
            item.sell_in -= 1
            return


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
