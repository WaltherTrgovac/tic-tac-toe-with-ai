class BotHard:
    def __init__(self):
        self.player = 'X'
        self.opponent = 'O'
        self.count = 0
        self.min_row = None
        self.min_col = None
        self.max_row = None
        self.max_col = None

    def evaluate(self, grid):
        """
        Evaluation function for the minimax algorithm. It returns 0 when O wins, 2 when X wins,
        1 when it is a draw, and -1 when it is not yet decided

        :param grid: Grid that is being played on
        :return: Evaluation value
        """

        # row win
        for row in range(1, 4):
            if (grid[row][2] == grid[row][4] and grid[row][4] == grid[row][6]
                    and grid[row][2] != ' '):
                if grid[row][2] == self.player:
                    return 2
                elif grid[row][2] == self.opponent:
                    return 0

        # col win
        for col in [2, 4, 6]:
            if (grid[1][col] == grid[2][col] and grid[2][col] == grid[3][col]
                    and grid[1][col] != ' '):
                if grid[1][col] == self.player:
                    return 2
                elif grid[1][col] == self.opponent:
                    return 0

        # diagonal win
        if grid[1][2] == grid[2][4] and grid[2][4] == grid[3][6] and grid[1][2] != ' ':
            if grid[2][4] == self.player:
                return 2
            elif grid[2][4] == self.opponent:
                return 0

        if grid[3][2] == grid[2][4] and grid[2][4] == grid[1][6] and grid[3][2] != ' ':
            if grid[2][4] == self.player:
                return 2
            elif grid[2][4] == self.opponent:
                return 0

        # not decided yet or draw
        for i in range(1, 4):
            for j in [2, 4, 6]:
                if grid[i][j] == ' ':
                    return -1
        return 1

    def max(self, grid):
        """
        Max function for the minimax algorithm. It calculates the biggest value among the possible next moves, calls min
        function if needed, and returns the biggest value

        :param grid: Grid that is being played on
        :return: Maximal value calculated based on next possible moves
        """
        self.count += 1
        # look if we are done, also at the bottom of the tree, then just evaluate
        if self.evaluate(grid) != -1:
            return self.evaluate(grid)

        max_value = -100000
        for i in range(1, 4):
            for j in [2, 4, 6]:
                if grid[i][j] == ' ':
                    self.change_grid(grid, self.player, i, j)
                    value = self.min(grid)
                    if value > max_value:
                        max_value = value
                    self.change_grid(grid, ' ', i, j)

        return max_value

    def min(self, grid):
        """
        Min function for the minimax algorithm. It calculates the smallest value among the possible next moves, calls
        max function if needed, and returns the smallest value

        :param grid: Grid that is being played on
        :return: Minimal value calculated based on next possible moves
        """

        self.count += 1
        if self.evaluate(grid) != -1:
            return self.evaluate(grid)

        min_value = 100000
        for i in range(1, 4):
            for j in [2, 4, 6]:
                if grid[i][j] == ' ':
                    self.change_grid(grid, self.opponent, i, j)
                    value = self.max(grid)
                    if value < min_value:
                        min_value = value
                    self.change_grid(grid, ' ', i, j)

        return min_value

    def min_positions(self, grid):
        """
        Same function as min(), but it is being called just on the top of the tree, so it actually stores the best
        positions

        :param grid: Grid that is being played on
        :return: Best possible next positions
        """
        self.count += 1
        if self.evaluate(grid) != -1:
            return self.evaluate(grid)

        min_value = 100000
        for i in range(1, 4):
            for j in [2, 4, 6]:
                if grid[i][j] == ' ':
                    self.change_grid(grid, self.opponent, i, j)
                    value = self.max(grid)
                    if value < min_value:
                        min_value = value
                        self.min_row = i
                        self.min_col = j
                    self.change_grid(grid, ' ', i, j)

        return min_value

    def max_positions(self, grid):
        """
        Same function as max(), but it is being called just on the top of the tree, so it actually stores the best
        positions

        :param grid: Grid that is being played on
        :return: Best possible next positions
        """
        self.count += 1
        # look if we are done, also at the bottom of the tree, then just evaluate
        if self.evaluate(grid) != -1:
            return self.evaluate(grid)

        max_value = -100000
        for i in range(1, 4):
            for j in [2, 4, 6]:
                if grid[i][j] == ' ':
                    self.change_grid(grid, self.player, i, j)
                    value = self.min(grid)
                    if value > max_value:
                        max_value = value
                        self.max_row = i
                        self.max_col = j
                    self.change_grid(grid, ' ', i, j)

        return max_value

    @staticmethod
    def change_grid(grid, player, position_row, position_col):
        """
        It changes the grid based on the given positions

        :param grid: Grid that is being played on
        :param player: Either 'X' or 'O'
        :param position_row: Row position
        :param position_col: Column position
        :return: Changed grid after the move has been made
        """
        grid[position_row] = grid[position_row][:position_col] + player + grid[position_row][position_col + 1:]
