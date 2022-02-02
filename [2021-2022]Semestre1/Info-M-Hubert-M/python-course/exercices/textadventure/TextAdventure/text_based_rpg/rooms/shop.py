from .. import interface, items
from ..util import move
from ..room import Room

map_ = """Caféteria, très animer et plein de vie, et une bonne odeur de nourriture japonaise"""

def enter(room, player):
    if room.has_been_entered_before:
        interface.print_multiple_lines(
            lines=[
                "Caféteria, très animer et plein de vie, et une bonne odeur de nourriture japonaise",
            ],
            delay=0
        )
    else:
        room.has_been_entered_before = True

        interface.print_multiple_lines(
            lines=[
                "Caféteria, très animer et plein de vie, et une bonne odeur de nourriture japonaise",
            ],
            delay=0
        )

    while True:
        additional_commands = ["talk"]

        if player.can_progress_to_mountain:
            additional_commands = ["move"]

        command = interface.get_game_command(
            player,
            room,
            additional_commands
        )

        if command == "talk":
            npc = interface.get_command(
                ["Restaurateur", "cancel"],
                True
            )

            if npc == "Restaurateur":
                interface.print_multiple_lines(
                    lines=[
                        "Bonjour ! je ne t'avais jamais vue ici avent ?",
                        "Vous : Non je viens d'arriver aujourd'hui je n'est pas encor obtenu tout mes badge d'admission"
                        "Je vais te donner un conseil, \"Mange et bois pendant t'es combat !\"",
                        "Avec un ramen dans le bid on ce sans revivre !"
                        "Le Redbull pour l'énergie et la forme ! et le saké pour tout exploser !"
                    ],
                    delay=0
                )

                for _ in range(3):
                    player.inventory.append(items.health_potion())

                if player.class_ in ["guerrier", "assassin"]:
                    interface.print_("Le Ramen a été ajouter a votre inventaire")

                    for _ in range(3):
                        player.inventory.append(items.stamina_potion())
                else:
                    interface.print_("Le RedBull a été ajouter a votre inventaire")

                    for _ in range(3):
                        player.inventory.append(items.mana_potion())
                    interface.print_("Le saké a été ajouter a votre inventaire")


                interface.print_("Utiliser \"use item\" pour manger et boire ce que vous avez prit, vosu devirez pourvoir combattre dans l'arène sans risque")

                interface.print_()
                player.can_progress_to_mountain = True
        else:
            place_to_move = move(["outside"])

            if place_to_move == "outside":
                from .center_of_town import room as center_of_town
                center_of_town.enter(player)

room = Room(
    map_=map_,
    enter=enter
)
