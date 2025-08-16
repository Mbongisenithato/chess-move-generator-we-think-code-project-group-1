# move_generator.py

from board import Board

class MoveGenerator:
    def __init__(self, board: Board):
        self.board = board
        self.moves = []

    def generate_moves(self):
        """Generate pseudo-legal moves for all pieces on the board."""
        self.moves.clear()
        for rank in range(8):
            for file in range(8):
                piece = self.board.get_piece_at(rank, file)
                if piece != '.':
                    color = 'white' if piece.isupper() else 'black'
                    self._generate_piece_moves(piece, rank, file, color)
        return self.moves

    def _generate_piece_moves(self, piece, rank, file, color):
        """Dispatch move generation based on piece type."""
        piece_type = piece.lower()
        if piece_type == 'p':
            self._generate_pawn_moves(rank, file, color)
        elif piece_type == 'n':
            self._generate_knight_moves(rank, file, color)
        # Add other pieces: bishop, rook, queen, king

    def _generate_pawn_moves(self, rank, file, color):
        """Generate basic pawn moves (no en passant or promotion)."""
        direction = -1 if color == 'white' else 1
        start_rank = 6 if color == 'white' else 1

        # Single move forward
        if self.board.get_piece_at(rank + direction, file) == '.':
            self.moves.append(((rank, file), (rank + direction, file)))

        # Double move from starting rank
        if rank == start_rank and self.board.get_piece_at(rank + direction * 2, file) == '.':
            self.moves.append(((rank, file), (rank + direction * 2, file)))

        # Captures
        for df in [-1, 1]:
            target_file = file + df
            if 0 <= target_file < 8:
                target_piece = self.board.get_piece_at(rank + direction, target_file)
                if target_piece != '.' and target_piece.isupper() != (color == 'white'):
                    self.moves.append(((rank, file), (rank + direction, target_file)))

    def _generate_knight_moves(self, rank, file, color):
        """Generate knight moves."""
        directions = [
            (2, 1), (1, 2), (-1, 2), (-2, 1),
            (-2, -1), (-1, -2), (1, -2), (2, -1)
        ]
        for dr, df in directions:
            r, f = rank + dr, file + df
            if 0 <= r < 8 and 0 <= f < 8:
                target = self.board.get_piece_at(r, f)
                if target == '.' or target.isupper() != (color == 'white'):
                    self.moves.append(((rank, file), (r, f)))
