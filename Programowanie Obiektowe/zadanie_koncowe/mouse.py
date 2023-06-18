"""Moduł zawierający klasę obsługującą mysz "Mouse".
"""

from pygame import Vector2, mouse
from const import SCREEN_SIZE


class Mouse:
    """Klasa obsługująca myszkę.

    Attributes:
        clicked (bool): Zmienna mówiąca, czy lewy przycisk myszy jest wciśnięty.
        pos (Vector2): Pozycja kursora myszy.
    """

    def __init__(self):
        """Ustawianie początkowych własności myszy.
        """

        # pola z informacją czy wciśnięto lewy przycisk myszy
        self.clicked = False

        # pozycja myszki
        self.pos = Vector2(0, 0)

    def update(self, draw_screen_size: Vector2):
        """Odświeżania pozycji myszy i informacji o wciśnięciu przycisku.

        Args:
            draw_screen_size: Aktualna wielkość płaszczyzny do rysowania.
        """

        # aktualizacja pozycji myszki
        pos = mouse.get_pos()
        self.pos = Vector2(
            pos[0] / (SCREEN_SIZE[0] / draw_screen_size[0]),
            pos[1] / (SCREEN_SIZE[1] / draw_screen_size[1]))

        # aktualizacja informacji o wciśnięciu lewego przycisku myszy
        self.clicked = mouse.get_pressed()[0]
