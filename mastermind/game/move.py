class Move:
    """Keep track of the guesses"""

    def __init__(self, attempt):
        """Comment"""
        self._attempt = attempt

    def get_attempt(self):
        """Returns the guess"""
        return self._attempt
