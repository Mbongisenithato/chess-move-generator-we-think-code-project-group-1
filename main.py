from chess.board import Board
from chess.move_generator import generate_moves

fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
board = Board(fen)
moves = generate_moves(board)
print(moves)