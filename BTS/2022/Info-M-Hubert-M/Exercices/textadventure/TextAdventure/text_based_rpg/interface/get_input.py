from .data import DATA
from .built_in_methods import input_



def get_input():

    return input_(DATA["input_prompt"]).strip().lower()
