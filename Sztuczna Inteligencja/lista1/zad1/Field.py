from __future__ import annotations

from Config import Config


class Field:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def parse(self, name: str):
        self.x = {
            "a": 0,
            "b": 1,
            "c": 2,
            "d": 3,
            "e": 4,
            "f": 5,
            "g": 6,
            "h": 7,
        }[name[0]]
        self.y = int(name[1]) - 1

    def __eq__(self, value: Field):
        return self.x == value.x and self.y == value.y
    
    def shift(self, x, y) -> Field:
        return Field(self.x + x, self.y + y)
    
    def in_board(self) -> bool:
        return 0 <= self.x < Config.BOARD_SIZE and 0 <= self.y < Config.BOARD_SIZE
