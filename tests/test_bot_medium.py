from main.bot_medium import BotMedium


class TestBotMedium:

    def test_medium_bot_1(self):
        grid = ['---------',
                '| X     |',
                '| O X   |',
                '|   O   |',
                '---------']
        medium_move = BotMedium().make_medium_move(grid)
        expected_move = (3, 3)
        assert medium_move == expected_move

    def test_medium_bot_2(self):
        grid = ['---------',
                '| X X O |',
                '| O X   |',
                '|   O   |',
                '---------']
        medium_move = BotMedium().make_medium_move(grid)
        expected_move = (3, 3)
        assert medium_move == expected_move

    def test_medium_bot_3(self):
        grid = ['---------',
                '| X X   |',
                '| O     |',
                '|   O   |',
                '---------']
        medium_move = BotMedium().make_medium_move(grid)
        expected_move = (1, 3)
        assert medium_move == expected_move

    def test_medium_bot_4(self):
        grid = ['---------',
                '| X X   |',
                '| X   O |',
                '|   O   |',
                '---------']
        medium_move = BotMedium().make_medium_move(grid)
        expected_moves = [(1, 3), (3, 1)]
        assert medium_move in expected_moves

    def test_medium_bot_5(self):
        grid = ['---------',
                '| O O   |',
                '| O   X |',
                '|   X X |',
                '---------']
        medium_move = BotMedium().make_medium_move(grid)
        expected_moves = [(1, 3), (3, 1)]
        assert medium_move in expected_moves

    def test_medium_bot_6(self):
        grid = ['---------',
                '|       |',
                '| O     |',
                '| X X   |',
                '---------']
        medium_move = BotMedium().make_medium_move(grid)
        expected_move = (3, 3)
        assert medium_move == expected_move

    def test_medium_bot_7(self):
        grid = ['---------',
                '| O   O  |',
                '| X X O  |',
                '| X X    |',
                '---------']
        medium_move = BotMedium().make_medium_move(grid)
        expected_moves = [(3, 3), (2, 1)]
        assert medium_move in expected_moves

