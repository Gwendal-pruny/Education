from collections import namedtuple

from .util import set_multiple_attributes

class Attack:
    def __init__(
            self,
            name,
            display_name,
            type_,
            damage,
            description_of_being_used="",
            stamina_cost=0,
            mana_cost=0
    ):
        set_multiple_attributes(
            self,
            name=name,
            display_name=display_name,
            type=type_,
            damage=damage,
            description_of_being_used=description_of_being_used,
            stamina_cost=stamina_cost,
            mana_cost=mana_cost
        )

_AttackStyle = namedtuple("AttackStyle", ["damage_stat"])

MELEE = _AttackStyle(damage_stat="strength")
RANGED = _AttackStyle(damage_stat="archery")
MAGIC = _AttackStyle(damage_stat="magic")
