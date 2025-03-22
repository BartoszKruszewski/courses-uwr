from FigureEnum import FigureEnum
from Field import Field
from dataclasses import dataclass


@dataclass
class Move:
    figure: FigureEnum
    field: Field
