import random


class Board:
    """Comment"""

    def __init__(self):
        """Comment"""

    def to_string(self, names):
        """Sets up the board"""

        text = "\n--------------------"
        for name, names in enumerate(names):
            text += (f"\n{name}: ")
        text += "\n--------------------"
        return text
