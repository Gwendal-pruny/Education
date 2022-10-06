from collections import namedtuple

from .util import set_multiple_attributes

EQUIPPABLE = object()
CONSUMABLE = object()

class Item:
    def __init__(
            self,
            display_name,
            type_,
            equip_location=None,
            effects=None,
            attacks=None
    ):
        if effects is None:
            effects = []

        if attacks is None:
            attacks = []

        set_multiple_attributes(
            self,
            display_name=display_name,
            type=type_,
            equip_location=equip_location,
            effects=effects,
            attacks=attacks,
        )

ItemEffect = namedtuple("ItemEffect", ["stat", "modifier"])
