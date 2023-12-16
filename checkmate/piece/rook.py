from piece import Piece, Position

class Rook(Piece):
    def __str__(self) -> str:
        return Piece.__str__(self) + 'R'

    def get_allowed_movements(self, Board) -> list[Position]:
        pass