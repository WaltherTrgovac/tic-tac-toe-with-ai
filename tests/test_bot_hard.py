from main.bot_hard import BotHard


class TestBotHard:
    
    def setup_method(self):
        self.hard_bot = BotHard()

    def test_hard_bot_1(self):
        grid = ['---------',
                '| X X   |',
                '| O X   |',
                '| O O   |',
                '---------']
        self.hard_bot.max_positions(grid)
        hard_move = (self.hard_bot.max_row, self.hard_bot.max_col // 2)
        expected_move = (1, 3)
        assert hard_move == expected_move

    def test_hard_bot_2(self):
        grid = ['---------',
                '| X     |',
                '| O X   |',
                '|   O   |',
                '---------']
        self.hard_bot.max_positions(grid)
        hard_move = (self.hard_bot.max_row, self.hard_bot.max_col // 2)
        expected_move = (1, 2)
        assert hard_move == expected_move

    def test_hard_bot_3(self):
        grid = ['---------',
                '|       |',
                '|       |',
                '|       |',
                '---------']
        self.hard_bot.max_positions(grid)
        hard_move = (self.hard_bot.max_row, self.hard_bot.max_col // 2)
        expected_moves = [(1, 1), (1, 3), (3, 1), (3, 3)]
        assert hard_move in expected_moves

    def test_hard_bot_4(self):
        grid = ['---------',
                '| X     |',
                '|       |',
                '|       |',
                '---------']
        self.hard_bot.min_positions(grid)
        hard_move = (self.hard_bot.min_row, self.hard_bot.min_col // 2)
        expected_move = (2, 2)
        assert hard_move == expected_move

    def test_hard_bot_5(self):
        grid = ['---------',
                '| X     |',
                '|   O   |',
                '|       |',
                '---------']
        self.hard_bot.max_positions(grid)
        hard_move = (self.hard_bot.max_row, self.hard_bot.max_col // 2)
        expected_moves = [(1, 2), (2, 1)]
        assert hard_move in expected_moves

