from enum import Enum
from abc import ABC
from checkmate.board import Board

class Color(Enum):
    Black = 0
    White = 1

class Position:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

class Piece(ABC):
    def __init__(self, color: Color, pos: Position) -> None:
        self._color = color
        self._pos = pos
    
    def __str__(self) -> str:
        return 'B' if self._color == Color.Black else 'W'
    
    def get_allowed_movements(self, Board) -> list[Position]:
        pass
