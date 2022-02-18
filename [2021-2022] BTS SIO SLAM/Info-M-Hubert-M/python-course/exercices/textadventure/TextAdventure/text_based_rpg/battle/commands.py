ATTACK = "Attaquer"
REST = "Attendre"
USE_ITEM = "Utiliser un objet"
GO_BACK = "retour"
TURN_COMMANDS = [ATTACK, REST, USE_ITEM]

def get_player_attack_commands(battle):

    commands = battle.player.attack_names.copy()
    commands.append(GO_BACK)
    return commands
