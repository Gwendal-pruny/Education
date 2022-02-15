from .data import DATA
from text_based_rpg import interface
from .get_input import get_input
from .generate_readable_list import generate_readable_list
from .built_in_methods import print_
from pprint import pprint
import inquirer
import os
import sys
sys.path.append(os.path.realpath("."))

PLAY = "play"
HELP = "help"
QUIT = "quit"
COMMANDS = [PLAY, HELP, QUIT]

def get_command(commands, list_options=False):
    while True:
        if list_options == True:
            questions = [
                inquirer.List(
                    "choice",
                    message="Vous choissisez",
                    choices=[generate_readable_list(commands)],
                ),
            ]
        questions = [
            inquirer.List(
                "choice",
                message= "Vous choissisez",
                choices= commands,
            ),
        ]
        
        received_input = inquirer.prompt(questions)        
        print_()        

        if received_input in commands:
            return received_input


        