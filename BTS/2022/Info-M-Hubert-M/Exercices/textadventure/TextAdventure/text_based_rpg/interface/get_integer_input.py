from .data import DATA
from .get_input import get_input
from .built_in_methods import print_


"""a supp après changement methodo input"""

def get_integer_input(upper_limit):
    unsuitable_input_messsage = DATA["unsuitable_input_messages"][
        "get_integer_input"
    ].format(upper_limit=upper_limit)

    while True:
        received_input = get_input()
        value = None

        try:
            value = int(received_input)
        except ValueError:
            print_(unsuitable_input_messsage)
            continue

        if not 1 <= value <= upper_limit:
            print_(unsuitable_input_messsage)
            continue

        return value
