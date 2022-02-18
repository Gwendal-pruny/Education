
from . import item, attack

iron_sword = item.Item(
    display_name="Epé",
    type_=item.EQUIPPABLE,
    equip_location="arms",
    effects=[item.ItemEffect(stat="strength", modifier=5), item.ItemEffect(stat="dexterity", modifier=-2)],
    attacks=[
        attack.Attack(
            name="Coup d'épé",
            display_name="Coup d'épé",
            type_=attack.MELEE,
            damage=3,
            stamina_cost=2,
            description_of_being_used="coup d'épé"
        ),
        attack.Attack(
            name="Super coup d'épé",
            display_name="coup d'épé fort",
            type_=attack.MELEE,
            damage=7,
            stamina_cost=5,
            description_of_being_used="super coup d'épé fort"
        )
    ]
)

iron_helmet = item.Item(
    display_name="Casque",
    type_=item.EQUIPPABLE,
    equip_location="head",
    effects=[
        item.ItemEffect(stat="defence", modifier=3),
        item.ItemEffect(stat="strength", modifier=1),
        item.ItemEffect(stat="dexterity", modifier=-1)
    ]
)

iron_breastplate = item.Item(
    display_name="Plastron",
    type_=item.EQUIPPABLE,
    equip_location="torso",
    effects=[item.ItemEffect(stat="defence", modifier=4), item.ItemEffect(stat="strength", modifier=2), item.ItemEffect(stat="dexterity", modifier=-2)]
)

iron_platelegs = item.Item(
    display_name="Jambière",
    type_=item.EQUIPPABLE,
    equip_location="legs",
    effects=[item.ItemEffect(stat="defence", modifier=3), item.ItemEffect(stat="strength", modifier=1), item.ItemEffect(stat="dexterity", modifier=-1)]
)

oak_bow = item.Item(
    display_name="Arc",
    type_=item.EQUIPPABLE,
    equip_location="arms",
    effects=[item.ItemEffect(stat="archery", modifier=4), item.ItemEffect(stat="dexterity", modifier=-1)],
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
    effects=[item.ItemEffect(stat="defence", modifier=4), item.ItemEffect(stat="archery", modifier=3)]
)

cow_hide_legs = item.Item(
    display_name="Camouflage bas de vache",
    type_=item.EQUIPPABLE,
    equip_location="legs",
    effects=[item.ItemEffect(stat="defence", modifier=3), item.ItemEffect(stat="archery", modifier=2)]
)

ice_staff = item.Item(
    display_name="Pistolet de glace",
    type_=item.EQUIPPABLE,
    equip_location="arms",
    effects=[item.ItemEffect(stat="magic", modifier=4), item.ItemEffect(stat="dexterity", modifier=-2)],
    attacks=[
        attack.Attack(
            name="icebolt",
            display_name="Icebolt",
            type_=attack.MAGIC,
            damage=3,
            mana_cost=4,
            description_of_being_used="Balle de glace"
        )
    ]
)

robe = item.Item(
    display_name="Robe",
    type_=item.EQUIPPABLE,
    equip_location="torso",
    effects=[item.ItemEffect(stat="defence", modifier=3), item.ItemEffect(stat="magic", modifier=4)]
)

hood = item.Item(
    display_name="Hood",
    type_=item.EQUIPPABLE,
    equip_location="head",
    effects=[item.ItemEffect(stat="defence", modifier=2), item.ItemEffect(stat="magic", modifier=3)]
)

steel_sword = item.Item(
    display_name="Epé magique",
    type_=item.EQUIPPABLE,
    equip_location="arms",
    effects=[item.ItemEffect(stat="strength", modifier=9), item.ItemEffect(stat="dexterity", modifier=-8)],
    attacks=[
        attack.Attack(
            name="Coup de l'épé de feux",
            display_name="Coup d'épé magique",
            type_=attack.MELEE,
            damage=15,
            stamina_cost=10,
            description_of_being_used="tranche avec ton épé enflamer"
        ),
        attack.Attack(
            name="Coup tranchant",
            display_name="Coup tranchant",
            type_=attack.MELEE,
            damage=7,
            stamina_cost=4,
            description_of_being_used="tranche"
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
    effects=[item.ItemEffect(stat="archery", modifier=9), item.ItemEffect(stat="dexterity", modifier=-2)],
    attacks=[
        attack.Attack(
            name="Flèche enflamer",
            display_name="Shoot",
            type_=attack.RANGED,
            damage=6,
            stamina_cost=2,
            description_of_being_used="flèche enflamer"
        )
    ]
)

hide_body = item.Item(
    display_name="hide body",
    type_=item.EQUIPPABLE,
    equip_location="torso",
    effects=[item.ItemEffect(stat="defence", modifier=10), item.ItemEffect(stat="archery", modifier=6)]
)

hide_legs = item.Item(
    display_name="hide legs",
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
