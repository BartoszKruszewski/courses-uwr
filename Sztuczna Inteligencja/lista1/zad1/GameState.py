from Field import Field


class GameState:
    def __init__(self, input: str):
        values = input.split(" ")
        self.turn = values[0] == "white"
        self.white_king = Field(values[1])
        self.white_rook = Field(values[2])
        self.black_king = Field(values[3])
