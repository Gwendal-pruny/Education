from .. import interface, enemies
from ..util import move, GameOver
from ..room import Room
from ..battle import Battle


map_ = """Classe 1-A, peut être ma futur classe"""

def enter(room, player):
    if room.has_been_entered_before:
        interface.print_multiple_lines(
            lines=[
                "XXXXXXXXXXXXXXXXXXXXXXXXXXXX",
                
            ],
            delay=0
        )
    else:
        interface.print_multiple_lines(
            lines=[
                "Proffesseur : Salut, tu a déjà finit de récolter les 3 badge ?",
                "Vous : Non il m'en manque un..",
                "Proffesseur : Que dirais tu de m'affronter moi pour ton 3 ème combat ?"
                "Proffesseur : cependant défaite ou victoire ne compte plus je t'évalurait directement"
                "Vous : d'accord pas de pitiée",
            ],
            delay=0
        )

    while True:
        additional_commands = ["attack", "move"]
        command = interface.get_game_command(player, room, additional_commands)
        
        if command == "attack":
            target = interface.get_command(["proffesseur", "cancel"], True)

            if target == "proffesseur":
                battle = Battle(player, enemies.proffeseur())
                battle.run()

                player.segond_boss_defeated = True
                interface.sleep(5)
                interface.print_()
                raise GameOver


room = Room(
    map_=map_,
    enter=enter
)
