from .. import interface, enemies, items
from ..util import move
from ..room import Room
from ..battle import Battle

map_ = """Dortoire, je n'y est pas encor accès"""

def enter(room, player):
    if room.has_been_entered_before:
        interface.print_multiple_lines(
            lines=[
                "Vous tomber sur la forgeronne d'arme de la dernière fois.",
                "Elle ne semble plus proposer d'équipement.",
                "Et les dortoire semble toujours fermer"
            ],
            delay=0
        )
    else:
        room.has_been_entered_before = True

        if player.talked_to_restaurateur:
            interface.print_multiple_lines(
                lines=[
                    "Intiger par un attroupement et en recherche de badge vous tomber sur une forgeronne d'arme.",
                    "Dès qu'elle vous voit elle vous prend a partie"
                    "Forgerone : Prend ca et prépare toi au combat le chanceux !"
                    "Vous : Le chanceux ? On ce connais ?"
                    "Forgerone : Cesse de te dégonfler enfile ca et vite !"
                ],
                delay=0
            )
            if player.class_ == "guerrier":
                    interface.print_multiple_lines(
                        lines=[
                            "Forgerone : Equipement de guerrier, épé, casque.. plastron jambière et voila ."
                        ],
                        delay=0
                    )

                    player.inventory.extend([
                        items.iron_sword,
                        items.iron_helmet,
                        items.iron_breastplate,
                        items.iron_platelegs
                    ])

            if player.class_ == "assassin":
                interface.print_multiple_lines(
                    lines=[
                        "Forgerone : Equipement d' asssasin, arc, haut et bas de combat tactic.. et voila."
                    ],
                    delay=0
                )

                player.inventory.extend([
                    items.oak_bow,
                    items.cow_hide_body,
                    items.cow_hide_legs
                ])

            if player.class_ == "magicien":
                interface.print_multiple_lines(
                    lines=[
                        "Forgerone : Pistolet magique pour les mage avec une robe et un bonus"
                    ],
                    delay=0
                )

                player.inventory.extend([
                    items.ice_staff,
                    items.hood,
                    items.robe
                ])

            interface.print_multiple_lines(
                lines=[
                    "Forgerone : maintenant équipe le ! et affronte moi !",
                ],
                delay=0
            )
            player.talked_to_forgerone = True
            interface.sleep(5)
            interface.print_()

        else:
            interface.print_multiple_lines(
                lines=[
                    "Tu ne semble pas pouvoir entrer sans les clef",
                ],
                delay=0
            )
        
        
    while True:
        if player.talked_to_restaurateur & player.talked_to_forgerone & player.forgerone_boss_defeated:
            additional_commands = ["move"]
        else:
            if player.talked_to_restaurateur & player.talked_to_forgerone:
                additional_commands = ["attack", "move"]
            else:
                additional_commands = ["talk", "move"]
        command = interface.get_game_command(player, room, additional_commands)
        if command == "attack":
            target = interface.get_command(["Forgerone", "cancel"], True)
            if target == "Forgerone":
                battle = Battle(player, enemies.forgerone())
                battle.run()
                
                player.forgerone_boss_defeated = True
                interface.sleep(5)
                interface.print_()

                interface.print_multiple_lines(
                    lines=[
                        "Bravo, tu fais belle usage de ce que je t'es confier, bravo...",
                        "Voici un badge et tu peut garder ton nouveaux équipement tu en aura besoin pour ton prochain combat."
                    ],
                    delay=0
                )
            
            if command == "talk":
                interface.print_multiple_lines(
                    lines=[
                        "Il n'y a pas grand monde a qui parler."
                    ],
                    delay=0
                )
                
                    
        place_to_move = move(["exterieur"])

        if place_to_move == "exterieur":
            from .exterieur import room as exterieur
            exterieur.enter(player)


room = Room(
    map_=map_,
    enter=enter
)