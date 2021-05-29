  
import random


class Board:
    """Comment"""

    def __init__(self):
        """Comment"""
        self._number = []
        self._prepare()

    def to_string(self, names):
        """Sets up the board"""

        text = "\n--------------------"
        for name, names in enumerate(self._names):
            text += (f"\n{name}: ")
        text += "\n--------------------"
        return text

    def _prepare(self):
        """sets up code"""
        number = random.randiant(1000, 9999)
        for n in range(number):
            self._number.append(code)