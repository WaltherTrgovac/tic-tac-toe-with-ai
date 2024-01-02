from main.bot_easy import BotEasy


class TestBotEasy:

    def setup_method(self):
        self.legal_moves = [(1, 1), (1, 2), (1, 3),
                            (2, 1), (2, 2), (2, 3),
                            (3, 1), (3, 2), (3, 3)]
        self.grid = ['---------',
                     '|       |',
                     '|       |',
                     '|       |',
                     '---------']

    def test_legal_moves(self):
        easy_move = BotEasy().make_easy_move(self.grid)
        legal_moves = self.legal_moves
        assert easy_move in legal_moves


