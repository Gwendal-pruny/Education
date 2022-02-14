from .. import util

def generate_random_multiplier():
    """
    Generate a random multiplier for use in different parts of the battle
    algorithm.

    """
    return util.resolve_random_condition([
        (1, 10),
        (5 / 6, 4),
        (7 / 6, 3),
        (2 / 3, 2),
        (4 / 3, 1)
    ])
