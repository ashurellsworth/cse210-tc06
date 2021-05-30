from game.board import Board
from game.console import Console
from game.guess import Guess
from game.player import Player
from game.roster import Roster


class Director:
    """Comment"""

    def __init__(self):
        """Comment"""

        self._board = Board()
        self._console = Console()
        self._roster = Roster()
        self._keep_playing = True
        self._guess = None

    def start_game(self):
        """Starts the game"""

        self._prepare_game()

        while self._keep_playing:
            players = self._roster.get_players()
            players = (players[0].get_name(), players[1].get_name())
            board = self._board.to_string(players)
            self._console.write(board)

            player = self._roster.get_current()
            self._console.write(f"\n{player.get_name()}'s turn:")
            guess = self._console.read_number("What is your guess? ")
            guess = Guess(guess)
            player.set_guess(guess)
            self._board.check_guess(guess)
            break
            player = self._roster.get_current()
            print(player)

    def _prepare_game(self):
        """Prepares the game before it begins."""

        self._console.write("Hello welcome to Mastermind!")
        self._board.prepare_num()

        for n in range(2):
            name = self._console.read(f"Enter a name for player {n + 1}: ")
            player = Player(name)
            self._roster.add_player(player)

    def _do_updates(self):
        player = self._roster.get_current()
        guess = player.get_move()
        self._board.apply(guess)

    def _do_outputs(self):
        if self._board.is_empty():
            winner = self._roster.get_current()
            name = winner.get_name()
            print(f"\n{name} won!")
            self._keep_playing = False
        self._roster.next_player()


# welcome
# get number

# get name1
# get name2

# print board
#     get name
#     get last guess
#     give hint *,o,x
# player 1 turn
# get their guess and store it
# loop to print board
