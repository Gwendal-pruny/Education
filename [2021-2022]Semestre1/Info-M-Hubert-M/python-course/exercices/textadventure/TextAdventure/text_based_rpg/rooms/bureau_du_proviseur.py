from .. import interface, enemies, items
from ..util import move
from ..room import Room
from ..battle import Battle

map_ = """Tu est dans le bureau du proviseur"""

def enter(room, player):
    if room.has_been_entered_before:
        interface.print_multiple_lines(
            lines=[
                "Le proviseur a l'air occuper..."
            ],
            delay=0
        )
    else:
        room.has_been_entered_before = True

        interface.print_multiple_lines(
            lines=[
                "Quand tu entre dans la pièce, tu vois seulement de dos le proviseur assis sur ca chaisse.",
                "Intimider vous vous annoncer et raprocher doussement."
            ],
            delay=0
        )

    while True:
        additional_commands = ["talk", "move"]

        command = interface.get_game_command(player, room, additional_commands)

        if command == "move":
            place_to_move = move(["hall"])

            if place_to_move == "hall":
                from .hall import room as hall
                hall.enter(player)
                
            
        if command == "talk":
            if room.has_been_entered_before: 
                npc = interface.get_command(
                    ["proviseur", "cancel"],
                True
                )
            else:
                npc = interface.get_command(
                    ["cancel"],
                True
                )


            if npc == "proviseur":
                interface.print_multiple_lines(
                    lines=[
                        "Vous : E..Excuser-moi ! ",
                        "Proviseur : Du calme pas besoin de criez ! Vien raproche toi regarde ce spétacle.",
                        "Vous : Ce sont des élève qui ce batte  a l’exterieur ! Il bouge si vite je n’arrive pas a les suivre !",
                        "Proviseur : HaHA, nous n’avons pas les même notrion de vitesse mon ami !",
                        "Proviseur : Bien tu voit la fille qui est en train de gagner le combat ?",
                        "Vous : A gauche ? Oui.. ",
                        "Proviseur : Tu est son prochaine adverser",
                        "Proviseur : Maintenant sort et affronte la ",
                        "Proviseur : Et dépèche toi elle t’attend déjà !",
                        ],
                    delay=0
                )
                interface.print_()
                player.talked_to_proviseur = True
                

room = Room(
    map_=map_,
    enter=enter
)
