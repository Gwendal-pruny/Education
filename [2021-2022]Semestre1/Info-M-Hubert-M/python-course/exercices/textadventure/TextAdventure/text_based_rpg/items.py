"""This modules contains the code representing the items in the game."""

from . import item, attack

iron_sword = item.Item(
    display_name="Epé",
    type_=item.EQUIPPABLE,
    equip_location="arms",
    effects=[item.ItemEffect(stat="strength", modifier=5), item.ItemEffect(stat="dexterity", modifier=-2)],
    attacks=[
        attack.Attack(
            name="stab",
            display_name="Stab",
            type_=attack.MELEE,
            damage=3,
            stamina_cost=2,
            description_of_being_used="stab"
        ),
        attack.Attack(
            name="slash",
            display_name="Slash",
            type_=attack.MELEE,
            damage=5,
            stamina_cost=4,
            description_of_being_used="slash"
        )
    ]
)

iron_helmet = item.Item(
    display_name="Casque",
    type_=item.EQUIPPABLE,
    equip_location="head",
    effects=[
        item.ItemEffect(stat="defence", modifier=4),
        item.ItemEffect(stat="strength", modifier=1),
        item.ItemEffect(stat="dexterity", modifier=-1)
    ]
)

iron_breastplate = item.Item(
    display_name="Plastron",
    type_=item.EQUIPPABLE,
    equip_location="torso",
    effects=[item.ItemEffect(stat="defence", modifier=6), item.ItemEffect(stat="strength", modifier=2), item.ItemEffect(stat="dexterity", modifier=-2)]
)

iron_platelegs = item.Item(
    display_name="Jambière",
    type_=item.EQUIPPABLE,
    equip_location="legs",
    effects=[item.ItemEffect(stat="defence", modifier=5), item.ItemEffect(stat="strength", modifier=1), item.ItemEffect(stat="dexterity", modifier=-1)]
)

oak_bow = item.Item(
    display_name="Arc",
    type_=item.EQUIPPABLE,
    equip_location="arms",
    effects=[item.ItemEffect(stat="archery", modifier=5), item.ItemEffect(stat="dexterity", modifier=-1)],
    attacks=[
        attack.Attack(
            name="shoot",
            display_name="Shoot",
            type_=attack.RANGED,
            damage=3,
            stamina_cost=1,
            description_of_being_used="shoot"
        )
    ]
)

cow_hide_body = item.Item(
    display_name="Camouflage haut de vache",
    type_=item.EQUIPPABLE,
    equip_location="torso",
    effects=[item.ItemEffect(stat="defence", modifier=5), item.ItemEffect(stat="archery", modifier=3)]
)

cow_hide_legs = item.Item(
    display_name="Camouflage bas de vache",
    type_=item.EQUIPPABLE,
    equip_location="legs",
    effects=[item.ItemEffect(stat="defence", modifier=4), item.ItemEffect(stat="archery", modifier=2)]
)

ice_staff = item.Item(
    display_name="Pistolet de glace",
    type_=item.EQUIPPABLE,
    equip_location="arms",
    effects=[item.ItemEffect(stat="magic", modifier=5), item.ItemEffect(stat="dexterity", modifier=-2)],
    attacks=[
        attack.Attack(
            name="icebolt",
            display_name="Icebolt",
            type_=attack.MAGIC,
            damage=3,
            mana_cost=4,
            description_of_being_used="fire an icebolt at"
        )
    ]
)

robe = item.Item(
    display_name="Robe",
    type_=item.EQUIPPABLE,
    equip_location="torso",
    effects=[item.ItemEffect(stat="defence", modifier=4), item.ItemEffect(stat="magic", modifier=4)]
)

hood = item.Item(
    display_name="Hood",
    type_=item.EQUIPPABLE,
    equip_location="head",
    effects=[item.ItemEffect(stat="defence", modifier=3), item.ItemEffect(stat="magic", modifier=3)]
)

steel_sword = item.Item(
    display_name="Epé magique",
    type_=item.EQUIPPABLE,
    equip_location="arms",
    effects=[item.ItemEffect(stat="strength", modifier=10), item.ItemEffect(stat="dexterity", modifier=-4)],
    attacks=[
        attack.Attack(
            name="stab",
            display_name="Stab",
            type_=attack.MELEE,
            damage=6,
            stamina_cost=4,
            description_of_being_used="stab"
        ),
        attack.Attack(
            name="slash",
            display_name="Slash",
            type_=attack.MELEE,
            damage=10,
            stamina_cost=8,
            description_of_being_used="slash"
        )
    ]
)

steel_helmet = item.Item(
    display_name="Casque megique",
    type_=item.EQUIPPABLE,
    equip_location="head",
    effects=[
        item.ItemEffect(stat="defence", modifier=8),
        item.ItemEffect(stat="strength", modifier=2),
        item.ItemEffect(stat="dexterity", modifier=-2)
    ]
)

steel_breastplate = item.Item(
    display_name="Plastron magique",
    type_=item.EQUIPPABLE,
    equip_location="torso",
    effects=[item.ItemEffect(stat="defence", modifier=12), item.ItemEffect(stat="strength", modifier=4), item.ItemEffect(stat="dexterity", modifier=-4)]
)

steel_platelegs = item.Item(
    display_name="Jambière magique",
    type_=item.EQUIPPABLE,
    equip_location="legs",
    effects=[item.ItemEffect(stat="defence", modifier=10), item.ItemEffect(stat="strength", modifier=2), item.ItemEffect(stat="dexterity", modifier=-2)]
)

willow_bow = item.Item(
    display_name="Arc magique",
    type_=item.EQUIPPABLE,
    equip_location="arms",
    effects=[item.ItemEffect(stat="archery", modifier=10), item.ItemEffect(stat="dexterity", modifier=-2)],
    attacks=[
        attack.Attack(
            name="shoot",
            display_name="Shoot",
            type_=attack.RANGED,
            damage=6,
            stamina_cost=2,
            description_of_being_used="shoot"
        )
    ]
)

bear_hide_body = item.Item(
    display_name="Bear hide body",
    type_=item.EQUIPPABLE,
    equip_location="torso",
    effects=[item.ItemEffect(stat="defence", modifier=10), item.ItemEffect(stat="archery", modifier=6)]
)

bear_hide_legs = item.Item(
    display_name="Bear hide legs",
    type_=item.EQUIPPABLE,
    equip_location="legs",
    effects=[item.ItemEffect(stat="defence", modifier=8), item.ItemEffect(stat="archery", modifier=4)]
)

fire_staff = item.Item(
    display_name="Pistolet enflamer",
    type_=item.EQUIPPABLE,
    equip_location="arms",
    effects=[item.ItemEffect(stat="magic", modifier=10), item.ItemEffect(stat="dexterity", modifier=-4)],
    attacks=[
        attack.Attack(
            name="fireblast",
            display_name="Fireblast",
            type_=attack.MAGIC,
            damage=6,
            mana_cost=6,
            description_of_being_used="fireblast"
        )
    ]
)

battle_robe = item.Item(
    display_name="Robe de combat",
    type_=item.EQUIPPABLE,
    equip_location="torso",
    effects=[item.ItemEffect(stat="defence", modifier=8), item.ItemEffect(stat="magic", modifier=8)]
)

battle_hood = item.Item(
    display_name="hood de combat",
    type_=item.EQUIPPABLE,
    equip_location="head",
    effects=[item.ItemEffect(stat="defence", modifier=6), item.ItemEffect(stat="magic", modifier=6)]
)

def health_potion():
    return item.Item(
        display_name="Ramen",
        type_=item.CONSUMABLE,
        effects=[item.ItemEffect(stat="health", modifier=10)]
    )

def stamina_potion():
    return item.Item(
        display_name="Redbull",
        type_=item.CONSUMABLE,
        effects=[item.ItemEffect(stat="stamina", modifier=10)]
    )

def mana_potion():
    return item.Item(
        display_name="Saké",
        type_=item.CONSUMABLE,
        effects=[item.ItemEffect(stat="mana", modifier=10)]
    )
