from .. import interface, enemies, items
from ..util import move
from ..room import Room
from ..battle import Battle

map_ = """Tu est a l'exterieur dans la cours"""

def enter(room, player):
    if room.has_been_entered_before:
        interface.print_multiple_lines(
            lines=[
                "Tu est a l'exterieur dans la cours, Il y a des zones d'entrainements et beaucoup d'élèves"
            ],
            delay=4
        )
    else:
        room.has_been_entered_before = True

        interface.print_multiple_lines(
            lines=[
                "Vous : *** Je ne comprend pas, pourquoi me demander de me battre alors que je n’es strictement aucune chance, il le savait, j’en suis sur, c’est un sadique ce type ! ***",
                "??? : Heyy ! ..",
                "??? : Toi la ! T’es le prochain adversere de maeva non ? Le proviseur m’a parler de toi, t’a intérèt a y allez mollot avec elle, sinon t’aura affaire a moi !",
                "??? : Au fait je m’appelle Pierre je suis l’oganisateur membre directionel du BDE de UA Academy Pierre !",
                "Vous : Euh ok ? et comment ca mollot ?",
                "Pierre : Enfin bref tu comprendra bientôt, hésite pas a parler a meava avent de la déf.. Hum.. battre",
                "avent le combat et dès que tu est prêt vien me voir je te donnerai un conseil.",
                "Vous : c’est pas assez scénariser si tu me le dit maintenant ?",
                "Pierre : Oui",
                "Vous : Vous êtes tousse bizarre  ici .."
            ],
            delay=5
        )

    while True:
        additional_commands = ["talk", "move"]

        if hasattr(player, 'talked_to_maeva'):
            additional_commands = ["attack"]

        command = interface.get_game_command(player, room, additional_commands)

        if command == "attack":
            target = interface.get_command(["maeva", "cancel"], True)

            if target == "maeva":
                
                battle = Battle(player, enemies.maeva())
                battle.run()

                player.first_boss_defeated = True
                interface.sleep(5)
                interface.print_multiple_lines(
                        lines=[
                            "Maeva : Quelle endurance ! Tu tappe comme une fillete mais qu'es que tu sait endurer les coups.. tu m'a eu d'épuisement ce n'est que partie remise",
                            "Vous : Pierre m'as dit d'y allez mollot, je ne voulais pas vous blesser.**Et je ne pensait pas te battre aussi facilement**"
                            "Maeva : Tien prend ca et va voir le proviseur le chanceux, la prochaine fois tu rigoleras moins."
                            ],
                        delay=3
                    )
                interface.print_()


        if command == "move":
            place_to_move = move(["hall"])

            if place_to_move == "hall":
                from .hall import room as hall
                hall.enter(player)

        if command == "talk":
            if room.has_been_entered_before: 
                npc = interface.get_command(
                    ["maeva", "cancel"],
                    True
                )
            elif room.has_been_entered_before & player.talked_to_maeva:
                npc = interface.get_command(
                    ["pierre","cancel"],
                    True
                )
                
            if npc == "maeva":
                    interface.print_multiple_lines(
                        lines=[
                            "meava : Tu est venu te battre ? Sans équipement ?",
                            "Vous : on ne m’a pas donnez d’équipement..",
                            "??? : Salut, désoler du retard , mais ton équipement est prêt, vas-y mollo je ne sais pas encor si elle est bien stabiliser pour toi.",
                            "Vous : Pour moi ?",
                            "Maeva : allez cesson de tergiverser , affronte-moi !",
                            ],
                        delay=3
                    )
                    interface.print_()
                    player.talked_to_maeva = True
                    
            if npc == "pierre":
                interface.print_multiple_lines(
                    lines=[
                        "Vous : Vous vouliez me dire quoi ducoup ?",
                        "Pierre : Tu as ton équipement ? Bien ..",
                        "Pierre : maeva as parler de moi ?",
                        "Vous : non pourquoi",
                        "Pierre : pour rien bonne chance pour ton combat, mon conseil c'est d'enfiler t'a super armure CHIAO !",
                        "Vous : vraiment bizzarre ce type..",
                        ],
                    delay=3
                )
                interface.print_()
                player.talked_to_pierre = True
                
                interface.print_multiple_lines(
                lines=[
                    "Tu enfile ton équipement, respire un bon coup. Ta fièrter te pousse devant toute cette foule."
                    "Cependant tu est tout tramblant de peur, problème tu ne sait pas te battre..",
                ],
                delay=4
                )
                if player.class_ == "guerrier":
                    interface.print_multiple_lines(
                        lines=[
                            "Un super équipement a été rajouter a votre inventaire équiper le !",
                            ],
                        delay=4
                    )

                    player.inventory.extend([
                        items.steel_sword,
                        items.steel_helmet,
                        items.steel_breastplate,
                        items.steel_platelegs
                    ])

                if player.class_ == "assassin":
                    interface.print_multiple_lines(
                        lines=[
                            "Un super équipement a été rajouter a votre inventaire équiper le !",
                        ],
                        delay=4
                    )

                    player.inventory.extend([
                        items.willow_bow,
                        items.bear_hide_body,
                        items.bear_hide_legs
                    ])

                if player.class_ == "magicien":
                    interface.print_multiple_lines(
                        lines=[
                            "Un super équipement a été rajouter a votre inventaire équiper le !",
                        ],
                        delay=4
                    )

                    player.inventory.extend([
                        items.fire_staff,
                        items.battle_hood,
                        items.battle_robe
                    ])
                


room = Room(
    map_=map_,
    enter=enter
)
