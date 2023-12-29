import time

from bot_easy import BotEasy
from bot_medium import BotMedium
from bot_hard import BotHard
from grid import Grid


class GameMenu:
    def __init__(self):
        self.turn = None
        self.game_loop = True
        self.player_functions = {"user": self.human_player, "easy": self.easy_bot_player,
                                 "medium": self.medium_bot_player, "hard": self.hard_bot_player}
        self.player_1 = None
        self.player_2 = None

    def start(self):
        """
        Checks whether the user has given the right input in order to start the game according
        to the correct input
        """
        while self.game_loop:
            players = input().split()

            if len(players) == 1 and players[0] == "exit":
                self.exit()

            elif len(players) == 3 and players[0] == "start":
                if players[1] not in self.player_functions or players[2] not in self.player_functions:
                    print("Bad parameters!")
                else:
                    game = Grid()
                    game.initial_grid("_________")
                    self.player_1 = players[1]
                    self.player_2 = players[2]

                    turn = "player_1"
                    while not game.finished:
                        time.sleep(2)
                        if turn == "player_1":
                            self.player_functions[players[1]](game)
                            turn = "player_2"
                        elif turn == "player_2":
                            self.player_functions[players[2]](game)
                            turn = "player_1"

            else:
                print("Bad parameters!")

    def exit(self):
        """
        Sets the game_loop to False and automatically ends the game
        """
        self.game_loop = False

    @staticmethod
    def human_player(game):
        """
        If user inputs "user" at the start, this function will be called and checks every time when it is user's
        turn, whether the input is correct
        :param game: Grid that is being played on
        """
        correct_input = False
        while not correct_input:
            try:
                position_row, position_column = input("Enter the coordinates: ").split()

            except ValueError:
                print("You should enter numbers!")
                continue

            try:
                if not isinstance(int(position_row), int) or not isinstance(int(position_column), int):
                    print("You should enter numbers!")
                elif int(position_row) not in [1, 2, 3] or int(position_column) not in [1, 2, 3]:
                    print("Coordinates should be from 1 to 3!")
                else:
                    if game.grid[int(position_row)][int(position_column) * 2] != ' ':
                        print("This cell is occupied! Choose another one!")
                    else:
                        game.changing_grid(int(position_row), int(position_column))
                        correct_input = True

            except ValueError:
                print("You should enter numbers!")
                continue

    @staticmethod
    def easy_bot_player(game):
        """
        If user inputs "easy" at the start, this function will be called and moves will be made
        according to the easy bot
        :param game: Grid that is being played on
        """
        print('Making move level "easy"')
        easy_bot_moves = BotEasy().make_easy_move(game.grid)
        game.changing_grid(easy_bot_moves[0], easy_bot_moves[1])

    @staticmethod
    def medium_bot_player(game):
        """
        If user inputs "medium" at the start, this function will be called and moves will be made
        according to the medium bot
        :param game: Grid that is being played on
        """
        print('Making move level "medium"')
        medium_bot_moves = BotMedium().make_medium_move(game.grid)
        game.changing_grid(medium_bot_moves[0], medium_bot_moves[1])

    def hard_bot_player(self, game):
        hard_bot = BotHard()
        if self.player_1 == "hard":
            try:
                print('Making move level "hard"')
                hard_bot.max_positions(game.grid)
                hard_bot_moves = hard_bot.max_row, hard_bot.max_col
                game.changing_grid(hard_bot_moves[0], hard_bot_moves[1] // 2)
            except TypeError:
                pass
        if self.player_2 == "hard":
            try:
                print('Making move level "hard"')
                hard_bot.min_positions(game.grid)
                hard_bot_moves = hard_bot.min_row, hard_bot.min_col
                game.changing_grid(hard_bot_moves[0], hard_bot_moves[1] // 2)
            except TypeError:
                pass


def main():
    GameMenu().start()


if __name__ == "__main__":
    main()
