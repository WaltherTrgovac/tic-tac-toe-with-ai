import random


class BotEasy:
    def __init__(self):
        self.legal_move = [1, 2, 3]
        self.row_random_move = random.choice(self.legal_move)
        self.col_random_move = random.choice(self.legal_move)

    def make_easy_move(self, grid):
        """
        Makes a random legal move, but it can happen, that the move has already been made
        :return: Returns a legal and available move according to the easy level
        """
        move_made = False

        while not move_made:
            if grid[self.row_random_move][self.col_random_move * 2] != ' ':
                self.row_random_move = random.choice(self.legal_move)
                self.col_random_move = random.choice(self.legal_move)
            else:
                move_made = True

        return self.row_random_move, self.col_random_move
