"""Moduł zawierający abstrakcyjną klasę węża "Snake", z której dziedziczą klasy
gracza "Player" oraz przeciwnika "Enemy".
"""

import random
import math
from pygame import Vector2, Color
from const import SNAKE_BASE_SPEED, SNAKE_START_LENGTH, SNAKE_INTERLUDE,\
    MAP_SIZE, SNAKE_COLORS, FOOD_TO_GROW, SNAKE_START_SIZE, SNAKE_BOOST_SPEED,\
    SNAKE_ACCELERATION, SNAKE_FOOD_CONSUMPTION_SPEED, SNAKE_SPAWN_TIME


class Snake:
    """Abstrakcyjna klasa węża.

    Zmiana pozycji, wielkości i koloru węża.

    Attributes:
        eaten_food (int): Ilość zjedzonego jedzenia do tej pory.
        body_size (float): Promień pojedynczej "komórki" ciała.
        dest (Vector2): Pozycja, w kierunku której porusza się wąż.
        speed (float): Prędkość węża.
        is_speeding (bool): Stan przyśpieszania gracza.
        spawn_timer (float): Licznik czasu, jaki pozostał do pojawienia się węża
        color (Color): Kolor węża
    """

    def __init__(self):
        """Przypisanie domyślnych wartości początkowych i wylosowanie pozycji
        początkowej węża.
        """

        # ilość zjedzonego jedzenia
        self.eaten_food = 0

        # lista z elementami ciała (body[0] to głowa)
        head = Vector2(
            random.randrange(-MAP_SIZE, MAP_SIZE),
            random.randrange(-MAP_SIZE, MAP_SIZE))
        self.body = [head - i * Vector2(
            SNAKE_INTERLUDE // 2, SNAKE_INTERLUDE // 2)
            for i in range(SNAKE_START_LENGTH)]

        # szerokość ciała
        self.body_size = math.sqrt(len(self.body)) + SNAKE_START_SIZE

        # cel poruszania się
        self.dest = self.body[0].copy()

        # ustawienie prędkości na bazową prędkość węża
        self.speed = SNAKE_BASE_SPEED

        # czy wąż przyśpiesza
        self.is_speeding = False

        # czas pojawiania się węża
        self.spawn_timer = SNAKE_SPAWN_TIME

        # kolor
        color_info = random.choice(SNAKE_COLORS)
        self.color = Color(color_info[0], color_info[1], color_info[2])

        # ustawienie przezroczystości koloru
        self.__update_color(1)

    def __stay_in_map_area(self):
        """Zmiana pozycji celu poruszania się węża, jeżeli wąż wychodzi poza
        obszar gry.
        """

        if self.body[0].x < -MAP_SIZE:
            self.dest.x = -MAP_SIZE
        elif self.body[0].x > MAP_SIZE:
            self.dest.x = MAP_SIZE
        if self.body[0].y < -MAP_SIZE:
            self.dest.y = -MAP_SIZE
        elif self.body[0].y > MAP_SIZE:
            self.dest.y = MAP_SIZE

    def __update_speed(self, dt: float):
        """Aktualizacja prędkości poruszania się węża, z uwzględnieniem
        zmiennej is_speeding.

        Args:
            dt: Mnożnik zmieniający wartości względem wydajności gry.
        """

        # sprawdzanie, czy należy zwiększyć, czy zmniejszyć prędkość
        if self.is_speeding and self.eaten_food > 0:

            # "gładka" zmiana prędkości
            self.speed += (SNAKE_BOOST_SPEED - self.speed) *\
                          SNAKE_ACCELERATION * dt

            # "zjedzenie" odpowiedniej ilości jedzenia
            self.eaten_food -= dt * SNAKE_FOOD_CONSUMPTION_SPEED

            # aktualizacja wielkości węża
            self.__update_size()
        else:
            # "gładka" zmiana prędkości
            self.speed -= (self.speed - SNAKE_BASE_SPEED) *\
                          SNAKE_ACCELERATION * dt

    def __update_color(self, dt: float):
        """Aktualizacja przeźroczystości koloru węża.

        Args:
            dt: Mnożnik zmieniający wartości względem wydajności gry.
        """

        # aktualizacja licznika czasu pozostałego do całkowitego pojawienia
        # się węża
        self.spawn_timer -= dt
        self.spawn_timer = max(self.spawn_timer, 0)

        # aktualizacja przezroczystości koloru węża
        self.color.a = int((1 - self.spawn_timer / SNAKE_SPAWN_TIME) * 255)

    def update_snake(self, dt: float):
        """Aktualizacja węża.

        Args:
            dt: Mnożnik zmieniający wartości względem wydajności gry.
        """

        # aktualizacja koloru
        self.__update_color(dt)

        # aktualizacja prędkości
        self.__update_speed(dt)

        # przesunięcie węża
        self.__move(dt)

    def __move(self, dt: float):
        """Aktualizacja prędkości poruszania się węża, z uwzględnieniem
        zmiennej is_speeding.

        Args:
            dt: Mnożnik zmieniający wartości względem wydajności gry.
        """

        # jeżeli cel węża jest na jego własnej głowie, to przenieś cel do
        # przodu w kierunku, w jakim się porusza wąż
        if abs(self.body[0].x - self.dest.x) < SNAKE_INTERLUDE and\
                abs(self.body[0].y - self.dest.y) < SNAKE_INTERLUDE:
            if self.body[0] - self.body[1] != Vector2(0, 0):
                self.dest += (self.body[0] - self.body[1]).normalize() * 10

        # zmiana celu, jeżeli wąż jest poza granicami mapy
        self.__stay_in_map_area()

        # przemieszczenie głowy w kierunku celu
        self.body[0].move_towards_ip(self.dest, self.speed * dt)

        # przemieszczenie każdego elementu ciała w kierunku innego
        # następującego go elementu
        for i in range(1, len(self.body)):

            # jeżeli element ciała jest zbyt oddalony od swojego poprzednika
            # to jest przesuwany w jego kierunku
            if self.body[i].distance_to(self.body[i - 1]) > SNAKE_INTERLUDE:
                self.body[i].move_towards_ip(self.body[i - 1], self.speed * dt)

    def __update_size(self):
        """Aktualizacja wielkości węża.
        """

        # jeżeli ciało jest za krótkie dodaj nowy element
        if len(self.body) < self.eaten_food // FOOD_TO_GROW +\
                SNAKE_START_LENGTH:
            self.body.append(self.body[-1].copy())

        # jeżeli ciało jest za długie usuń ostatni element
        elif len(self.body) > self.eaten_food // FOOD_TO_GROW +\
                SNAKE_START_LENGTH:
            self.body.pop(-1)

        # aktualizacja szerokości węża
        self.body_size = math.sqrt(len(self.body)) + SNAKE_START_SIZE

    def grow(self):
        """Zwiększenie ilości zjedzonego jedzenia i aktualizacja wielkości węża.
        """

        # zwiększanie ilości zjedzonego jedzenia o 1
        self.eaten_food += 1

        # aktualizacja wielkości
        self.__update_size()
