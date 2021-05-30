import random


class Board:
    """Comment"""

    def __init__(self):
        """Comment"""
        self._number = 0

    def to_string(self, names):
        """Sets up the board"""

        text = "\n--------------------"
        for name in names:
            text += (f"\nPlayer {name}: ----, ****")
        text += "\n--------------------"
        return text

    def prepare_num(self):
        """sets up code"""
        self._number = random.randint(1000, 9999)
        print(self._number)

    def check_guess(self, guess):

        lst1 = list(map(int, str(guess._guess)))
        lst2 = list(map(int, str(self._number)))

        result = any(elem in lst1 for elem in lst2)
        print(result)
