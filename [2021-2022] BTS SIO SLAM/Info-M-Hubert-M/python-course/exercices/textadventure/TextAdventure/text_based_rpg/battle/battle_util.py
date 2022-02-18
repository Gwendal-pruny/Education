from .. import interface
from .data import DATA

class PlayerHasDiedError(Exception):

    pass

def get_entity_name(battle, entity):

    if entity in [battle.player, battle.player.entity]:
        return "player"

    return "enemy"

def get_opponent(battle, entity):
    if entity in [battle.player, battle.player.entity]:
        return battle.enemy

    return battle.player

def print_player_message(_, message_name, *args, **kwargs):
    message = DATA["messages"]["player"][message_name]

    if args:
        message = message.format(*args)
    elif kwargs:
        message = message.format(**kwargs)

    interface.print_(message)

def print_enemy_message(_, message_name, *args, **kwargs):
    message = DATA["messages"]["enemy"][message_name]

    if args:
        message = message.format(*args)
    elif kwargs:
        message = message.format(**kwargs)

    interface.print_(message)

def print_value_view(entity):
    interface.print_multiple_lines([
        entity.display_name,
        DATA["values_view_divider_character"] * len(entity.display_name),
        entity.values_view,
        ""
    ])

def print_damage_dealt_message(battle, attack, entity, damage):
    attack_description = attack.description_of_being_used

    entity_name = battle.get_entity_name(entity)
    opponent = battle.get_opponent(entity)
    opponent_name = battle.get_entity_name(opponent)

    if opponent == battle.player:
        attack_description += "s"

    interface.print_(
        DATA["messages"][entity_name]["damage_dealt"].format(
            attack_description=attack_description,
            opponent=DATA["prefixes"][opponent_name],
            damage=damage
        )
    )
