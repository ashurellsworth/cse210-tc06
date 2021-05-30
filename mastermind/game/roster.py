class Roster:
    """A collection of players. The responsibility of Roster is to keep track of the players.

    Stereotype: 
        Information Holder

    Attributes:
        _current (integer): The index of the current player.
        _players (list): A list of Player objects.
    """

    def __init__(self):
        """The class constructor."""

        self.current = -1
        self.players = []

    def add_player(self, player):
        """Adds the given player to the roster"""

        if player not in self.players:
            self.players.append(player)

    def get_players(self):
        """Gets the both players."""

        names = (self.players[0], self.players[1])

        return names

    def get_current(self):
        """Gets the current player object."""

        return self.players[self.current]

    def next_player(self):
        """Advances the turn to the next player."""

        self.current = (self.current + 1) % len(self.players)
