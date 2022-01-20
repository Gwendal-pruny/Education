from .hall import room as hall
from .shop import room as shop
from .town_square import room as town_square
from .center_of_town import room as center_of_town
from .mountain_exterior import room as mountain_exterior
from .exterieur import room as exterieur
from .second_room import room as second_room

rooms = [
    hall,
    shop,
    town_square,
    center_of_town,
    mountain_exterior,
    exterieur,
    second_room
]

def reset():
    for room in rooms:
        room.has_been_entered_before = False
