from text_based_rpg import interface
from text_based_rpg.start_game import start_game

PLAY = "play"
QUIT = "quit"
COMMANDS = [PLAY, QUIT]

def play():
    while True:
        interface.print_("Bienvenue sur mon jeu text-based RPG.\n")

        interface.print_("Vous pouvez choisire entre : " + interface.generate_readable_list(COMMANDS))
        command = interface.get_command(COMMANDS)

        if command == PLAY:
            start_game()

        if command == QUIT:
            interface.print_(help_text)
            
            break
