import random
from . import interface

def set_multiple_attributes(object_, **attributes):

    for key, value in attributes.items():
        setattr(object_, key, value)

def _generate_random_value(upper_limit):
    return random.randint(1, upper_limit)

def resolve_random_condition(chances_data):
    sum_of_chances = sum([
        individual_chance_data[1] for individual_chance_data in chances_data
    ])

    random_value = _generate_random_value(sum_of_chances)
    range_checked = 0

    for individual_chance_data in chances_data:
        key, chance = individual_chance_data
        range_checked += chance

        if random_value <= range_checked:
            return key

def move(locations):
    move_locations = locations.copy()
    move_locations.append("cancel")
    return interface.get_command(move_locations, True)

class GameOver(Exception):
    interface.print_multiple_lines(
        lines=[
            "Proffesseur : félicitation et bienvenue dans la classe ! Tu mérite ta place.",
            "Proffesseur : Je t'invite a t'assoire t'es cammarade vont arriver tu te présentera après",
            "                JOUR 1 : L'ascension", 
            "Félicitation vous êtes arriver a la fin du jour 0 et de mon jeux pour le moment ! "
        ],
        delay=0
    )
    pass
