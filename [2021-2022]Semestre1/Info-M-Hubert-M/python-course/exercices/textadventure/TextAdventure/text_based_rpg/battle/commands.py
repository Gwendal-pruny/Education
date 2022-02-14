"""
This module contains constants and methods relating to commands that can be used
in the battle.
"""

ATTACK = "Attaquer"
REST = "Attendre"
USE_ITEM = "Utiliser un objet"
GO_BACK = "retour"
TURN_COMMANDS = [ATTACK, REST, USE_ITEM]

def get_player_attack_commands(battle):
    """
    Get the list of commands the play can use in the attack phase in the battle.
    """
    commands = battle.player.attack_names.copy()
    commands.append(GO_BACK)
    return commands