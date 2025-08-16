# board.py

class Board:
    def __init__(self, fen: str):
        self.fen = fen
        self.board = self._parse_fen(fen)

    def _parse_fen(self, fen: str):
        """Convert FEN string to 2D board array."""
        rows = fen.split()[0].split('/')
        board = []
        for row in rows:
            parsed_row = []
            for char in row:
                if char.isdigit():
                    parsed_row.extend(['.'] * int(char))
                else:
                    parsed_row.append(char)
            board.append(parsed_row)
        return board

    def display(self):
        """Print the board in a human-readable format."""
        for row in self.board:
            print(' '.join(row))
        print()

    def get_piece_at(self, rank: int, file: int):
        """Return the piece at a given position (0-indexed)."""
        return self.board[rank][file]

    def set_piece_at(self, rank: int, file: int, piece: str):
        """Set a piece at a given position."""
        self.board[rank][file] = piece

    def to_fen(self):
        """Convert current board back to FEN (basic version)."""
        fen_rows = []
        for row in self.board:
            fen_row = ''
            empty_count = 0
            for cell in row:
                if cell == '.':
                    empty_count += 1
                else:
                    if empty_count > 0:
                        fen_row += str(empty_count)
                        empty_count = 0
                    fen_row += cell
            if empty_count > 0:
                fen_row += str(empty_count)
            fen_rows.append(fen_row)
        return '/'.join(fen_rows) + ' w KQkq - 0 1'  
