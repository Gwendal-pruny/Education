from .hall import room as hall
from .shop import room as shop
from .dortoire import room as dortoire
from .exterieur import room as exterieur
from .classe import room as classe

rooms = [
    hall,
    shop,
    dortoire,
    exterieur,
    classe,
]

def reset():
    for room in rooms:
        room.has_been_entered_before = False
