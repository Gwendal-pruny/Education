from .. import interface, enemies, items
from ..util import move
from ..room import Room
from ..battle import Battle

map_ = """Tu est dans le hall d’entrée de AU Academy"""

def enter(room, player):
    if room.has_been_entered_before:
        interface.print_multiple_lines(
            lines=[
                "Tu est dans le hall d’entrée de AU Academy, il y a beaucoup d’élèves!"
                ],
            delay=0
        )
    else:
        interface.print_multiple_lines(
            lines=[
                "Tu viens d’entrée dans le hall de AU Academy,",
                "bizarement il n’y a aucun élève, "
                "seulement une dame a l’acceuille et des crie de joie ou de pleure d’une foule au loin",
                "que tu n’arrive pas a disserner."
            ],
            delay=0
        )


    while True:
        additional_commands = ["talk", "move"]

        command = interface.get_game_command(player, room, additional_commands)

        if command == "move":
            if player.forgerone_boss_defeated & player.talked_to_proviseur_second_medal:
                place_to_move = move(["bureau du proviseur", "exterieur", "class 1-A"])
            elif player.talked_to_proviseur:
                place_to_move = move(["bureau du proviseur", "exterieur"])
            else:
                place_to_move = move(["bureau du proviseur"])

            if place_to_move == "bureau du proviseur":
                from .bureau_du_proviseur import room as bureau_du_proviseur
                bureau_du_proviseur.enter(player)
            if place_to_move == "exterieur":
                from .exterieur import room as exterieur
                exterieur.enter(player)
            if place_to_move == "class 1-A":
                from .classe import room as classe
                classe.enter(player)
            
        if command == "talk":
            if player.talked_to_garcons & player.talked_to_acceuil:   
                npc = interface.get_command(
                    ["evelyn", "cancel"],   
                    True
                )
                
            elif player.talked_to_acceuil:
                npc = interface.get_command(
                    ["evelyn", "garcons", "cancel"],   
                    True
                )
            else: 
                npc = interface.get_command(
                    ["acceuil", "garcons", "cancel"],
                    True
                )
            
            if npc == "acceuil":
                interface.print_multiple_lines(
                    lines=[
                        "Vous : Bonjour, je suis la pour m’inscrire a AU vous pouvez maider, je suis au bonne endroit ?",
                        "???  : Hey, je t’attendait, le proviseur veut te voir sont bureau est derrière tu peut y allez mais avent je te conseil d’allez voir le jeune garcons si tu ne la pas déjà fait,",
                        "Vous : Merci evelyn",
                        ],
                    delay=0
                )
                interface.print_()
                player.talked_to_acceuil = True
                
            if npc == "evelyn":
                if player.maeva_boss_defeated:
                    interface.print_multiple_lines(
                        lines=[
                            "Evelyn : Félicitation pour ton premier combat !",
                            "Vous : Merci"
                            ],
                        delay=0
                    )
                    interface.print_()
                    
                if player.talked_to_proviseur:
                    interface.print_multiple_lines(
                        lines=[
                            "Evelyn : Il t'attendent tousse aux millieu de la cours",
                            ],
                        delay=0
                    )
                    interface.print_()
                else:
                    interface.print_multiple_lines(
                        lines=[
                            "Evelyn  : Allez vas dans le bureau, il t'attend",
                            ],
                        delay=0
                    )
                    interface.print_()
                
            if npc == "garcons":
                interface.print_multiple_lines(
                    lines=[
                        "Vous : B-Bonjour ??",
                        "??? : ….",
                        "Vous : Vous allez bien ?",
                        "??? : n’entre SURTOUT pas dans le bureau du proviseur ils sont tousse FOU !!!!!",
                        "Vous : Que c’est-il passez ?",
                        "??? : Laisse moi tranquille !!! Dégage !! sort d’ici !",
                        ],
                    delay=0
                )
                interface.print_()
                player.talked_to_garcons = True


room = Room(
    map_=map_,
    enter=enter
)
