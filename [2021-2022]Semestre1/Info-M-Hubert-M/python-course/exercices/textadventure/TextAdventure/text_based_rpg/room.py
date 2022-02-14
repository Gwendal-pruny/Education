class Room:
    def __init__(self, map_, enter):
        """
                The function to call when the user enters the room.
                Implements the user's interaction with the room.

        """
        self.map = map_
        self.enter_function = enter
        self.has_been_entered_before = False

    def enter(self, player):
        self.enter_function(self, player)
