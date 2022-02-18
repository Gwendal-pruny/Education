"""This module contains code for the main command loop of the game."""

from .get_command import get_command
from .print_multiple_lines import print_multiple_lines
from .built_in_methods import print_

_MAP = "carte"
_STATS = "statistiques"
_INVENTORY = "inventaire"
_EQUIPMENT = "équipment"
_CONSUME_ITEM = "utilisée un objet"
_DISCARD_ITEM = "jeter un objet"
_EQUIP_ITEM = "équiper un objet"
_UNEQUIP_ITEM = "déséquipe un objet"

_BASE_COMMANDS = [
    _MAP,
    _STATS,
    _INVENTORY,
    _EQUIPMENT,
    _CONSUME_ITEM,
    _DISCARD_ITEM,
    _EQUIP_ITEM,
    _UNEQUIP_ITEM
]

def get_game_command(player, room, additional_commands=[]):

    commands = additional_commands.copy()
    commands.extend(_BASE_COMMANDS)

    while True:
        print_()
        command = get_command(commands, True)

        if command in additional_commands:
            return command

        if command == _MAP:
            print_multiple_lines(room.map.split("\n"), 1)

        if command == _STATS:
            player.stats_view()

        if command == _INVENTORY:
            player.inventory_view()

        if command == _EQUIPMENT:
            player.equipment_view()

        if command == _CONSUME_ITEM:
            player.use_item_interface()

        if command == _DISCARD_ITEM:
            player.discard_item_interface()

        if command == _EQUIP_ITEM:
            player.equip_item_interface()

        if command == _UNEQUIP_ITEM:
            player.unequip_item_interface()
