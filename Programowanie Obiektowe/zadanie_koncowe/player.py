"""Moduł zawierający klasę węża gracza "Player", która dziedziczy po klasie
abstrakcyjnej węża "Snake".
"""

from pygame import Vector2
from snake import Snake
from mouse import Mouse
from const import SNAKE_START_LENGTH


class Player(Snake):
    """Klasa węża gracza, dziedzicząca z klasy Snake.

    Ustawianie celu poruszania się węże, na podstawie wskaźnika myszki.
    """
    def __init__(self):
        """Ustawienie pozycji startowej ciała gracza
        """

        # wywołanie konstruktora klasy Snake
        super().__init__()

        # dodanie elementów ciała węża na środku planszy
        self.body = [Vector2(0, 0) for _ in range(SNAKE_START_LENGTH)]

    def update(self, mouse: Mouse, dt: float, scroll: Vector2):
        """Ustawienie kierunku poruszania na pozycję wskaźnika myszki

        Args:
            mouse: Obiekt myszki
            dt: Mnożnik zmieniający wartości względem wydajności gry.
            scroll: Przesunięcie płaszczyzny do rysowania.
        """

        # wywołanie funkcji aktualizującej z klasy bazowej
        self.update_snake(dt)

        # ustawienie przyśpieszenia
        self.is_speeding = mouse.clicked

        # ustawienie celu poruszania się na wskaźnik myszy
        self.dest = mouse.pos - scroll

        # przemieszczenie się
        self.update_snake(dt)
