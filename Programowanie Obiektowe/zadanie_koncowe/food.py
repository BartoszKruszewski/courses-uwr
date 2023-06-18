"""Moduł zawierający klasę jedzenia "Food".
"""

import random
from pygame import Vector2, Color
from const import MAP_SIZE, FOOD_COLORS, FOOD_SPAWN_TIME


class Food:
    """Klasa jedzenia.

    Attributes:
        pos (Vector2): Pozycja jedzenia na mapie.
        color (Color): Kolor jedzenia.
        spawn_timer (float): Czas pozostały do pojawienia się jedzenia.
    """

    def __init__(self, pos: Vector2 = None):
        """Ustawienie domyślnych wartości.

        Jeżeli argument "pos" nie jest podany, to pozycja jedzenia jest
        wybierana losowo.

        Args:
            pos: Pozycja jedzenia.
        """

        # wywołanie konstruktora klasy Snake
        super().__init__()

        # jeżeli nie podano dokładnej pozycji jako argument to wybierz losową
        # pozycję
        if pos is None:
            self.pos = Vector2(
                random.randrange(-MAP_SIZE, MAP_SIZE),
                random.randrange(-MAP_SIZE, MAP_SIZE))
        else:
            self.pos = pos.copy()

        # kolor jedzenia
        color_info = random.choice(FOOD_COLORS)
        self.color = Color(color_info[0], color_info[1], color_info[2])

        # czas, zanim jedzenie się pojawi
        self.spawn_timer = FOOD_SPAWN_TIME

    def update(self, dt: float):
        """Odświeżanie koloru jedzenia.

        Args:
            dt: Mnożnik zmieniający wartości względem wydajności gry.
        """

        # aktualizacja licznika czasu pozostałego do całkowitego pojawienia
        # się jedzenia
        self.spawn_timer -= dt
        self.spawn_timer = max(self.spawn_timer, 0)

        # aktualizacja przezroczystości koloru jedzenia
        self.color.a = int((1 - self.spawn_timer / FOOD_SPAWN_TIME) * 255)
