"""Moduł zawierający klasę cząsteczki "Particle", wykorzystywaną podczas
tworzenia efektów cząsteczkowych.
"""

import random
from pygame import Vector2, Color
from const import PARTICLE_COLORS, PARTICLE_SIZE, PARTICLE_TIME, PARTICLE_SPEED


class Particle:
    """Klasa cząsteczki, służących do wyświetlania efektów cząsteczkowych.

    Attributes:
        pos (Vector2): Pozycja cząsteczki.
        color (Color): Kolor cząsteczki.
        size (int): Wielkość cząsteczki.
        timer (float): Czas pozostały do zniknięcia cząsteczki.
        direction (Vector2): Kierunek poruszania się cząsteczki.
    """

    def __init__(self, pos: Vector2):
        """Ustawienie początkowych wartości cząsteczki.

        Ustawienie podanej pozycji oraz wylosowanie koloru, wielkości i
        kierunku poruszania się cząsteczki.

        Args:
            pos: Początkowa pozycja cząsteczki.
        """

        # pozycja cząsteczki
        self.pos = pos.copy()

        # kolor
        color_info = random.choice(PARTICLE_COLORS)
        self.color = Color(color_info[0], color_info[1], color_info[2])

        # wielkość
        self.size = random.randint(PARTICLE_SIZE[0], PARTICLE_SIZE[1])

        # czas trwania
        self.timer = PARTICLE_TIME

        # kierunek
        self.direction = Vector2(
            random.randint(-100, 100) / 100, random.randint(
                -100, 100) / 100)

    def update(self, dt: float):
        """Odświeżanie pozycji i przezroczystości koloru cząsteczki.

        Args:
            dt: Mnożnik zmieniający wartości względem wydajności gry.
        """

        # aktualizacja pozycji cząsteczki
        self.pos += self.direction * dt * PARTICLE_SPEED

        # zmiana przezroczystości koloru
        self.color.a = int(self.color[3] * self.timer / PARTICLE_TIME)

        # aktualizacja zegara
        self.timer -= dt
