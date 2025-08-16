# utils.py

def algebraic_to_index(square: str):
    """Convert algebraic notation (e.g. 'e4') to board indices (rank, file)."""
    file = ord(square[0].lower()) - ord('a')
    rank = 8 - int(square[1])
    return rank, file

def index_to_algebraic(rank: int, file: int):
    """Convert board indices to algebraic notation (e.g. (6, 4) → 'e2')."""
    return chr(file + ord('a')) + str(8 - rank)

def is_valid_square(square: str):
    """Check if a square string is valid algebraic notation."""
    if len(square) != 2:
        return False
    file, rank = square[0], square[1]
    return file in 'abcdefgh' and rank in '12345678'

def format_move(start, end):
    """Format a move tuple ((r1, f1), (r2, f2)) as algebraic string."""
    return f"{index_to_algebraic(*start)} → {index_to_algebraic(*end)}"

def validate_fen(fen: str):
    """Basic FEN validation (structure only)."""
    parts = fen.strip().split()
    if len(parts) != 6:
        return False
    rows = parts[0].split('/')
    if len(rows) != 8:
        return False
    for row in rows:
        count = 0
        for char in row:
            if char.isdigit():
                count += int(char)
            elif char.isalpha():
                count += 1
            else:
                return False
        if count != 8:
            return False
    return True
