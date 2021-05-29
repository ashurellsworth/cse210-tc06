from game.board import Board
from game.console import Console
from game.move import Move
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
        self._move = None

    def start_game(self):
        """Starts the game"""

        self._prepare_game()
        names = self._roster.get_players()

        while self._keep_playing:
            board = self._board.to_string(names)
            self._console.write(board)
            break

        #     self._get_inputs()
        #     self._do_updates()
        #     self._do_outputs()

    def _prepare_game(self):
        """Prepares the game before it begins."""

        self._console.write("Hello welcome to Mastermind!")

        for n in range(2):
            name = self._console.read(f"Enter a name for player {n + 1}: ")
            player = Player(name)
            self._roster.add_player(player)

    def _get_inputs(self):

        # # display the game board
        # board = self._board.to_string()
        # self._console.write(board)
        # # get next player's move
        player = self._roster.get_current()
        self._console.write(f"{player.get_name()}'s turn:")
        attempt = self._console.read_number("What is your guess? ")
        guess = Move(attempt)
        player.set_guess(guess)

    # def _do_updates(self):
    #     """Updates the important game information for each round of play. In
    #     this case, that means updating the board with the current move.

    #     Args:
    #         self (Director): An instance of Director.
    #     """
    #     player = self._roster.get_current()
    #     move = player.get_move()
    #     self._board.apply(move)

    def _do_outputs(self):
        """Outputs the important game information for each round of play. In
        this case, that means checking if there are stones left and declaring the winner.

        Args:
            self (Director): An instance of Director.
        """
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
