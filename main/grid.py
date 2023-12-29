class Grid:
    def __init__(self):
        self.count_x = 0
        self.count_o = 0
        self.turn = 'X'
        self.mapping_initial_dic = {0: [1, 2], 1: [1, 4], 2: [1, 6],
                                    3: [2, 2], 4: [2, 4], 5: [2, 6],
                                    6: [3, 2], 7: [3, 4], 8: [3, 6]}
        self.grid = ['---------',
                     '| _ _ _ |',
                     '| _ _ _ |',
                     '| _ _ _ |',
                     '---------']
        self.finished = False

    def initial_grid(self, initial_state):
        """
        Returns and prints the grid after the initial input

        :param initial_state: Initial grid
        :return: The resulting grid
        """
        for i in range(len(initial_state)):
            if initial_state[i] == '_':
                row, col = self.mapping_initial_dic[i]
                self.grid[row] = self.grid[row][:col] + ' ' + self.grid[row][col + 1:]
            if initial_state[i] == 'X':
                row, col = self.mapping_initial_dic[i]
                self.grid[row] = self.grid[row][:col] + 'X' + self.grid[row][col + 1:]
                self.count_x += 1
            if initial_state[i] == 'O':
                row, col = self.mapping_initial_dic[i]
                self.grid[row] = self.grid[row][:col] + 'O' + self.grid[row][col + 1:]
                self.count_o += 1

        self.printing_grid()

        return self.grid

    def changing_grid(self, position_row, position_column):
        """
        Returns and prints the grid after the input of correct coordinates

        :param position_row: Row position coordinate
        :param position_column: Column position coordinate
        :return: The resulting grid
        """
        if self.turn == 'X':
            self.grid[position_row] = (self.grid[position_row][:position_column * 2] +
                                       'X' + self.grid[position_row][position_column * 2 + 1:])
            self.count_x += 1
            self.turn = 'O'
        else:
            self.grid[position_row] = (self.grid[position_row][:position_column * 2] +
                                       'O' + self.grid[position_row][position_column * 2 + 1:])
            self.count_o += 1
            self.turn = 'X'

        self.printing_grid()
        self.output_state()

        return self.grid

    def output_state(self):
        """
        Checks the state of the game after a player makes a move
        """
        if self.three_in_a_row() and self.turn == 'X':
            print("O wins")
            self.finished = True
        elif self.three_in_a_row() and self.turn == 'O':
            print("X wins")
            self.finished = True
        elif not self.three_in_a_row() and self.count_x == 5 and self.count_o == 4:
            print("Draw")
            self.finished = True
        else:
            pass
            # print("Game not finished")

    def three_in_a_row(self):
        """
        Checks whether there are three in a row symbols on the grid to see if some player won

        :return: True if someone won
        """
        # row win
        for row in range(1, 4):
            if (self.grid[row][2] == self.grid[row][4] and self.grid[row][4] == self.grid[row][6]
                    and self.grid[row][2] != ' '):
                return True

        # col win
        for col in [2, 4, 6]:
            if (self.grid[1][col] == self.grid[2][col] and self.grid[2][col] == self.grid[3][col]
                    and self.grid[1][col] != ' '):
                return True

        # diagonal win
        if self.grid[1][2] == self.grid[2][4] and self.grid[2][4] == self.grid[3][6] and self.grid[1][2] != ' ':
            return True

        if self.grid[3][2] == self.grid[2][4] and self.grid[2][4] == self.grid[1][6] and self.grid[3][2] != ' ':
            return True

    def printing_grid(self):
        """
        Prints the grid
        """
        for row in self.grid:
            print(row)
