"""
This module contains general utility functions for use by Battle methods.
"""

from .. import interface
from .data import DATA

class PlayerHasDiedError(Exception):
    """
    An exception superclass to be raised when the player has died.
    """

    pass

def get_entity_name(battle, entity):
    """
    Determine the identifying string name of the given entity in the battle.
    """
    if entity in [battle.player, battle.player.entity]:
        return "player"

    return "enemy"

def get_opponent(battle, entity):
    """
    Determine the opponent of the given entity in the battle.
    """
    if entity in [battle.player, battle.player.entity]:
        return battle.enemy

    return battle.player

def print_player_message(_, message_name, *args, **kwargs):
    """
    Print a message, prefixed with the player's title.

    """
    message = DATA["messages"]["player"][message_name]

    if args:
        message = message.format(*args)
    elif kwargs:
        message = message.format(**kwargs)

    interface.print_(message)

def print_enemy_message(_, message_name, *args, **kwargs):
    """
    Print a message, prefixed with the enemy's title.
    """
    message = DATA["messages"]["enemy"][message_name]

    if args:
        message = message.format(*args)
    elif kwargs:
        message = message.format(**kwargs)

    interface.print_(message)

def print_value_view(entity):
    """
    Print a view displaying the given entity's health, mana, and stamina.
    """
    interface.print_multiple_lines([
        entity.display_name,
        DATA["values_view_divider_character"] * len(entity.display_name),
        entity.values_view,
        ""
    ])

def print_damage_dealt_message(battle, attack, entity, damage):
    """
    Print a message stating that one entity dealt a certain amount of damage to
    the other entity in the battle.
    """
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
