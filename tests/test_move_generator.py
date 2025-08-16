# test_move_generator.py

import unittest
from board import Board
from move_generator import MoveGenerator
from utils import format_move

class TestMoveGenerator(unittest.TestCase):

    def test_white_pawn_moves(self):
        fen = "8/8/8/8/8/8/P7/8 w - - 0 1"
        board = Board(fen)
        generator = MoveGenerator(board)
        moves = generator.generate_moves()

        expected = [((6, 0), (5, 0)), ((6, 0), (4, 0))]
        self.assertCountEqual(moves, expected)

    def test_black_pawn_moves(self):
        fen = "8/p7/8/8/8/8/8/8 b - - 0 1"
        board = Board(fen)
        generator = MoveGenerator(board)
        moves = generator.generate_moves()

        expected = [((1, 0), (2, 0)), ((1, 0), (3, 0))]
        self.assertCountEqual(moves, expected)

    def test_knight_moves_center(self):
        fen = "8/8/8/3N4/8/8/8/8 w - - 0 1"
        board = Board(fen)
        generator = MoveGenerator(board)
        moves = generator.generate_moves()

        expected = [
            ((3, 3), (5, 4)), ((3, 3), (5, 2)),
            ((3, 3), (4, 5)), ((3, 3), (4, 1)),
            ((3, 3), (2, 5)), ((3, 3), (2, 1)),
            ((3, 3), (1, 4)), ((3, 3), (1, 2))
        ]
        self.assertCountEqual(moves, expected)

    def test_knight_moves_edge(self):
        fen = "8/8/8/8/8/8/8/N7 w - - 0 1"
        board = Board(fen)
        generator = MoveGenerator(board)
        moves = generator.generate_moves()

        expected = [((7, 0), (5, 1)), ((7, 0), (6, 2))]
        self.assertCountEqual(moves, expected)

if __name__ == "__main__":
    unittest.main()
