from . import interface
from .battle.battle_util import PlayerHasDiedError
from .create_player import create_player
from .rooms.hall import room as hall
from .util import GameOver
from .rooms.reset import reset as reset_rooms

def start_game():
    reset_rooms()
    player = create_player()

    try:
        hall.enter(player)
        
        
        
        
        
    except (PlayerHasDiedError, GameOver) as exception:
        if isinstance(exception, PlayerHasDiedError):
            interface.print_multiple_lines(
                lines=[
                    "=" * 20,
                    "",
                    "",
                    "",
                    "Your are dead.... it's not impossible to win.. u r jst bad",
                    "",
                    "",
                    "",
                    "=" * 20
                ],
                delay=0
            )
        else:
            interface.sleep(7)
            interface.print_multiple_lines(
                lines=[
                    "SPEACHLESS END"
                ],
                delay=0
            )

            interface.print_()
            interface.sleep(7)
