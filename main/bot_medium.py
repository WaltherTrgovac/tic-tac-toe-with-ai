from bot_easy import BotEasy


class BotMedium(BotEasy):
    def __init__(self):
        super().__init__()
        self.all_moves = [[1, 2], [1, 4], [1, 6],
                          [2, 2], [2, 4], [2, 6],
                          [3, 2], [3, 4], [3, 6]]
        self.row_medium_move = None
        self.col_medium_move = None

    def make_medium_move(self, grid):
        """
        Makes a move that checks whether there are 2 moves in a row and plays the third move in a row,
        if such move is not available, it returns a random move from bot_easy
        :return: Returns a legal and available move according to the medium level
        """
        # check if there is a 2 in a row
        for row in range(1, 4):
            if grid[row][2] == grid[row][4] and grid[row][4] != ' ' and grid[row][6] == ' ':
                self.row_medium_move, self.col_medium_move = row, 3
            if grid[row][4] == grid[row][6] and grid[row][4] != ' ' and grid[row][2] == ' ':
                self.row_medium_move, self.col_medium_move = row, 1

        # check if there is a 2 in a column
        for col in [2, 4, 6]:
            if grid[1][col] == grid[2][col] and grid[2][col] != ' ' and grid[3][col] == ' ':
                self.row_medium_move, self.col_medium_move = 3, (col // 2)
            if grid[2][col] == grid[3][col] and grid[2][col] != ' ' and grid[1][col] == ' ':
                self.row_medium_move, self.col_medium_move = 1, (col // 2)

        # check if there is 2 in a diagonal
        if grid[1][2] == grid[2][4] and grid[2][4] != ' ' and grid[3][6] == ' ':
            self.row_medium_move, self.col_medium_move = 3, 3
        if grid[1][6] == grid[2][4] and grid[2][4] != ' ' and grid[3][2] == ' ':
            self.row_medium_move, self.col_medium_move = 3, 1
        if grid[3][2] == grid[2][4] and grid[2][4] != ' ' and grid[1][6] == ' ':
            self.row_medium_move, self.col_medium_move = 1, 3
        if grid[3][6] == grid[2][4] and grid[2][4] != ' ' and grid[1][2] == ' ':
            self.row_medium_move, self.col_medium_move = 1, 1

        # if medium move hasn't been made, make a random move
        if self.row_medium_move is not None and self.col_medium_move is not None:
            return self.row_medium_move, self.col_medium_move
        else:
            return self.make_easy_move(grid)
