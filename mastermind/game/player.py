class Player:
    """Comment"""

    def __init__(self, name):
        """Comment"""

        self._name = name
        self._move = None

    def get_move(self):
        """Returns the player's last move (an instance of Move). If the player 
        hasn't moved yet this method returns None.

        """
        return self._move

    def get_name(self):
        """Returns the player's name.
        """
        return self._name

    def set_guess(self, guess):
        """Sets the player's last guess to the given instance of guess."""

        self._move = guess
