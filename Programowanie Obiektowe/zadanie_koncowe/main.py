# -----------------------------------------------------------------------------
# Bartosz Kruszewski
# Zadanie końcowe na przedmiot "Programowanie obiektowe"
# Gra "Slither.io"
# Data utworzenia: 29.05.2023
# Wersja 1.0.0
# -----------------------------------------------------------------------------
# Wykorzystywany język: Python 3.11
# Wykorzystywana biblioteka: Pygame 2.3
# -----------------------------------------------------------------------------
# Instalacja elementów niezbędnych do uruchomienia programu:
# Interpreter Python 3.11:
#   1. Pobranie interpretera Pythona ze strony https://www.python.org.
#   2. Instalacja zgodnie z zalecanymi ustawieniami instalatora (należy
#    zaznaczyć opcję dodającą Pythona do ścieżki systemu).
# Biblioteka Pygame 2.3:
#   1. Uruchomienie wiersza poleceń systemu Windows (cmd).
#   2. Wpisanie "pip install pygame".
#   3. Jeżeli polecenie nie zostanie rozpoznane, należy upewnić się,
#      że interpreter Pythona został poprawnie zainstalowany i dodany
#      do ścieżki systemu.
#   4. Jeżeli w dalszym ciągu polecenie "pip install pygame" nie jest
#      wykonywane prawidłowo, należy spróbować użyć polecenia "python -m pip
#      install pygame".
# -----------------------------------------------------------------------------
# Uruchomienie Programu:
# 1. Należy upewnić się, że pliki:
#   - main.py
#   - snake.py
#   - player.py
#   - enemy.py
#   - particle.py
#   - food.py
#   - mouse.py
#   - const.py
#    Znajdują się w jednym folderze.
# 2. Uruchomienie wiersza poleceń systemu Windows (cmd).
# 3. Przejście do folderu, gdzie znajdują się pliku programu.
# 4. Użycie polecenia "python main.py".
# -----------------------------------------------------------------------------
# Dodatkowe informacje
# -----------------------------------------------------------------------------
# Językiem użytym do udokumentowania całego programu, jest język polski.
# Najczęściej stosowana konwencja komentowania kodu napisanego w Pythonie
# zakłada używanie "docstrings". Są to komentarze umieszczane
# pod nazwami klas, funkcji czy stałych, które są "rozumiane" przez IDE i moduł
# Sphinx (użyty do utworzenia automatycznej dokumentacji tego projektu).
# Sphinx zakłada bardzo precyzyjny sposób, w jaki mają być przedstawione
# argumenty oraz atrybuty funkcji. W związku z tym sekcje z opisem argumentów
# funkcji, zwracanych przez nie wartości i sekcje atrybutów klas są nazwane:
# "Args", "Returns", "Attributes". Proszę traktować je jako część kodu,
# który tak samo, jak one jest napisany w języku angielskim.
# -----------------------------------------------------------------------------

"""Główny moduł gry. Wywołuje pozostałe wszystkie moduły projektu. Uruchomienie
tego modułu skutkuje uruchomieniem gry.
"""

from pygame import *
import pygame.gfxdraw
from math import sqrt, sin, cos
from const import *
from mouse import Mouse
from player import Player
from enemy import Enemy
from snake import Snake
from food import Food
from particle import Particle


class Main:
    """Główna klasa programu. Odpowiada za przygotowanie elementów gry, obsługę
    głównej pętli gry oraz rysowanie.

    Attributes:
        screen (Surface): Płaszczyzna ekranu.
        draw_screen (Surface): Płaszczyzna do rysowania.
        draw_screen_size (Vector2): Wymiary płaszczyzny do rysowania.
        clock (Clock): Zegar gry.
        dt (float): Mnożnik zmieniający wartości względem wydajności gry.
        mouse (Mouse): Obiekt myszki.
        is_running (bool): Zmienna kontrolująca, czy gra ma być uruchomiona.
        scroll (Vector2): Przesunięcie obszaru rysowania gry.
        particles (list[Particle]): Lista obiektów cząsteczek.
        player (Player): Obiekt węża gracza.
        enemies (list[Enemies]): Lista obiektów przeciwników.
        food (list[Food]): Lista obiektów jedzenia.
    """

    def __init__(self):
        """Inicjowanie programu
        """

        # inicjowanie modułu pygame
        init()

        # utworzenie płaszczyzny ekranu oraz płaszczyzny do rysowania
        self.screen = display.set_mode(SCREEN_SIZE)
        self.draw_screen_size = Vector2(
            START_DRAW_SCREEN_SIZE[0], START_DRAW_SCREEN_SIZE[1])
        self.draw_screen = Surface(self.draw_screen_size)
        
        # ustawienie nazwy okna
        display.set_caption("Slither.io")
        
        # utworzenie zegara gry
        self.clock = time.Clock()

        # utworzenie zmiennej przechowującej skalar do modyfikowania
        # przesunięć obiektów w stosunku do szybkości generowania klatek obrazu
        self.dt = 1

        # utworzenie obiektu myszki
        self.mouse = Mouse()

        # utworzenie zmiennej do kontroli zakończenia działania programu
        self.is_running = True

        # utworzenie wektora przesunięcia wyświetlanej planszy
        self.scroll = Vector2(0, 0)

        # utworzenie listy cząsteczek (efekt wizualny)
        self.particles = []

        # utworzenie obiektu węża gracza
        self.player = Player()

        # utworzenie listy obiektów węży przeciwników
        self.enemies = [Enemy() for _ in range(ENEMY_AMOUNT)]

        # utworzenie listy obiektów jedzenia
        self.food = [Food() for _ in range(START_FOOD_AMOUNT)]

        # główna pętla gry
        while self.is_running:
            # aktualizowanie akcji
            self.events_update()

            # aktualizowanie stanu myszki
            self.mouse.update(self.draw_screen_size)

            # główne operacje na obiektach gry
            self.game()

            # rysowanie nowej klatki obrazu
            self.draw()

            # odświeżanie ekranu
            self.display_update()

            # aktualizacja "delta time"
            self.dt = self.clock.tick(FRAMERATE) * STANDARD_FRAMERATE / 1000

    def add_food(self):
        """Dodanie nowego obiektu jedzenia, po wcześniejszym znalezieniu
        wolnej pozycji.
        """

        # tworzenie nowego obiektu jedzenia
        new_food = Food()

        # wybieranie niezajętej pozycji
        is_good_pos = False

        # tworzenie listy wszystkich węży
        all_snakes = [self.player]
        all_snakes.extend(self.enemies)

        # losowanie pozycji, aż pozycja będzie odpowiednia
        while not is_good_pos:

            # losowanie pozycji
            new_food = Food()
            is_good_pos = True

            # sprawdzanie każdego węża
            for snake in all_snakes:

                # sprawdzanie ciał węży czy są wystarczająco oddalone
                for body in snake.body:
                    if new_food.pos.distance_to(
                            body) < SNAKE_INTERLUDE + snake.body_size:
                        is_good_pos = False
                        break

        # dodanie nowego jedzenia
        self.food.append(new_food)

    def is_in_screen_range(self, vector: Vector2, shift: float = 0) -> bool:
        """Sprawdzanie, czy okrąg o podanej pozycji środka i promieniu znajduje
        się w zasięgu rysowania.

        Args:
            vector: Środek okręgu.
            shift: Promień okręgu.

        Returns:
            Prawda, jeżeli okrąg jest w zasięgu rysowania, fałsz w przeciwnym
            przypadku.
        """

        return -shift < (vector + self.scroll).x < self.draw_screen_size[
            0] + shift and -shift < (vector + self.scroll).y <\
            self.draw_screen_size[1] + shift

    def events_update(self):
        """Sprawdzanie, czy wywołano zdarzenie z modułu pygame i wykonanie
        powiązanych z nim poleceń.
        """

        # sprawdzanie akcji z modułu pygame
        for e in event.get():

            # jeżeli kliknięto krzyżyk do wyłączania okna to zakończ
            # działanie programu
            if e.type == QUIT:
                self.is_running = False

            # sprawdzanie, czy użyto kółka od myszy
            elif e.type == pygame.MOUSEWHEEL:

                # przybliżenie lub oddalenie mapy w zależności od tego,
                # w którą stronę przesunięto kółko
                if e.y == -1:
                    self.draw_screen_size *= ZOOM_SPEED
                else:
                    self.draw_screen_size //= ZOOM_SPEED

                # sprawdzenie, czy nie przekroczono limitów przybliżenia
                self.draw_screen_size.x = max(
                    self.draw_screen_size.x, MINIMUM_DRAW_SCREEN_SIZE[0])
                self.draw_screen_size.y = max(
                    self.draw_screen_size.y, MINIMUM_DRAW_SCREEN_SIZE[1])
                self.draw_screen_size.x = min(
                    self.draw_screen_size.x, SCREEN_SIZE[0])
                self.draw_screen_size.y = min(
                    self.draw_screen_size.y, SCREEN_SIZE[1])

        # sprawdzanie jakie przyciski z klawiatury wciśnięto
        keys = key.get_pressed()

        # jeżeli kliknięto ESC do to zakończ działanie programu
        if keys[K_ESCAPE]:
            self.is_running = False

    def draw_circle(self, pos: Vector2, r: float, c: Color, **kwargs):
        """Rysowanie koła.

        Args:
            pos: Pozycja środka koła.
            r: Promień koła.
            c: Kolor koła.
            **kwargs: Dodatkowe argumenty rysowania.
        """

        # sprawdzanie jaki typ koła został wybrany i rysowanie koła
        # na podanej pozycji przesuniętego o wektor przesunięcia
        # wyświetlanego ekranu
        if "aa" in kwargs and kwargs["aa"]:
            pygame.gfxdraw.aacircle(
                self.draw_screen, int(round(pos.x + self.scroll.x)),
                int(round(pos.y + self.scroll.y)), int(r), c)
        elif "fill" in kwargs and kwargs["fill"]:
            pygame.gfxdraw.filled_circle(
                self.draw_screen, int(round(pos.x + self.scroll.x)),
                int(round(pos.y + self.scroll.y)), int(r), c)
        else:
            pygame.gfxdraw.circle(
                self.draw_screen, int(round(pos.x + self.scroll.x)),
                int(round(pos.y + self.scroll.y)), int(r), c)

    def draw_eye(self, pos: Vector2, size: float, transparency):
        """Rysowanie oka węża.

        Args:
            pos: Pozycja, na której ma zostać narysowane oko.
            size: Wielkość oka.
            transparency (int): Przeźroczystość oka.
        """

        self.draw_circle(
            pos, size, pygame.Color(255, 255, 255, transparency), fill = True)
        self.draw_circle(pos, size, pygame.Color(0, 0, 0, transparency))
        self.draw_circle(
            pos, size - 2, pygame.Color(0, 0, 0, transparency), fill = True)

    def draw_snake(self, snake: Snake):
        """Rysowanie węża.

        Args:
            snake: Obiekt węża do narysowania.
        """

        # rysowanie poświaty dookoła węża symbolizującej jego prędkość
        amount_of_light = (snake.speed - SNAKE_BASE_SPEED) / (
                SNAKE_BOOST_SPEED - SNAKE_BASE_SPEED) * 255

        for body in snake.body[::-1]:
            # sprawdzanie, czy ciało jest w zasięgu rysowania
            if self.is_in_screen_range(body, snake.body_size):
                # rysowanie wypełnienia kolorem "komórki" ciała
                self.draw_circle(
                    body, snake.body_size + 1,
                    pygame.Color(255, 255, 255, int(amount_of_light)),
                    aa = True)

        # rysowanie ciała węża
        snake_body_color = snake.color
        for body in snake.body[::-1]:

            # przyciemnianie kolejnych elementów ciała węża
            snake_body_color = pygame.Color(
                max(snake_body_color[0] - SNAKE_FADE, 0),
                max(snake_body_color[1] - SNAKE_FADE, 0),
                max(snake_body_color[2] - SNAKE_FADE, 0),
                snake_body_color[3])

            # sprawdzanie, czy ciało jest w zasięgu rysowania
            if self.is_in_screen_range(body, snake.body_size):

                # rysowanie wypełnienia kolorem "komórki" ciała
                self.draw_circle(
                    body, snake.body_size, snake_body_color,
                    fill = True)

                # rysowanie konturu "komórki" ciała
                self.draw_circle(
                    body, snake.body_size,
                    pygame.Color(0, 0, 0, snake_body_color[3]))

                # rysowanie cieniowania "komórki" ciała
                self.draw_circle(
                    body, snake.body_size,
                    pygame.Color(0, 0, 0, snake_body_color[3]),
                    aa = True)

        # sprawdzanie, czy kierunek węża nie jest równy pozycji jego
        # głowy, co uniemożliwiłoby ustalenia pozycji oczu
        if (snake.dest - snake.body[0]).length() != 0:

            # ustalanie pozycji oczu
            eye_pos = snake.body[0] +\
                      (snake.dest - snake.body[0]).normalize() *\
                      (snake.body_size - int(sqrt(snake.body_size)) - 2)

            # rysowanie lewego oka
            self.draw_eye(
                self.rotate_point(eye_pos, snake.body[0], 1),
                sqrt(snake.body_size), snake.color.a)

            # rysowanie prawego oka
            self.draw_eye(
                self.rotate_point(eye_pos, snake.body[0], -1),
                sqrt(snake.body_size), snake.color.a)

    def draw(self):
        """Rysowanie wszystkich elementów gry.
        """

        # ustawienie wielkości płaszczyzny do rysowania
        if self.draw_screen_size != self.draw_screen.get_size():
            self.draw_screen = Surface(self.draw_screen_size)

        # wypełnianie tła jednolitym kolorem
        self.draw_screen.fill(BACKGROUND_COLOR)

        # rysowanie węża gracza
        self.draw_snake(self.player)

        # rysowanie węży przeciwników
        for enemy in self.enemies:
            self.draw_snake(enemy)

        # rysowanie jedzenia
        for food in self.food:

            # sprawdzanie, czy jedzenie jest w zasięgu rysowania
            if self.is_in_screen_range(food.pos):

                # rysowanie kółka na o właściwościach podanego jedzenia
                self.draw_circle(food.pos, 2, food.color)

        # rysowanie cząsteczek
        for particle in self.particles:

            # sprawdzanie, czy cząsteczka jest w zasięgu rysowania
            if self.is_in_screen_range(particle.pos):

                # rysowanie kółka o właściwościach podanej cząsteczki
                self.draw_circle(particle.pos, particle.size, particle.color)

    @staticmethod
    def rotate_point(v1: Vector2, v2: Vector2, angle: float):
        """Funkcja zwracająca punkt wektor będący wektorem v1 obróconym o
        podany kąt wokół wektora v2.

        Args:
            v1: Wektor, który będzie obracany.
            v2: Wektor, wokół którego wektor v1 będzie obracany.
            angle: Kąt, o jaki wektor v1 będzie obracany wokół wektora v2.
        Returns:
            Wektor, będący wektorem v1 obróconym o kąt angle, wokół wektora v2.
        """

        d = v1 - v2
        new_x = d.x * cos(angle) - d.y * sin(angle) + v2.x
        new_y = d.x * sin(angle) + d.y * cos(angle) + v2.y
        return Vector2(new_x, new_y)

    @staticmethod
    def check_snake_collisions(snake: Snake, other_snakes: list[Snake]) -> bool:
        """Funkcja sprawdzająca kolizje podanego węża z innymi wężami.

        Args:
            snake: Wąż, którego kolizje są sprawdzane.
            other_snakes: Lista pozostałych węży.
        Returns:
            Prawda, jeżeli wystąpiła kolizja, fałsz w przeciwnym przypadku.
        """
        # sprawdzanie dystansu do elementów ciała każdego wybranego węża
        for other_snake in other_snakes:
            for body in other_snake.body:
                if snake.body[0].distance_to(
                        body) < SNAKE_INTERLUDE + other_snake.body_size:
                    return True
        return False

    def game(self):
        """
        Główna logika gry
        """

        # aktualizowanie węża gracza
        self.player.update(self.mouse, self.dt, self.scroll)

        # sprawdzanie kolizji gracza
        if self.check_snake_collisions(self.player, self.enemies):

            # dodanie cząsteczek
            for body in self.player.body:
                for _ in range(PARTICLE_AMOUNT):
                    self.particles.append(Particle(body))

            # resetowania obiektu gracza
            self.player = Player()

        # zmiana przesunięcia płaszczyzny rysowania
        self.scroll -= self.player.body[0] - Vector2(
            self.draw_screen_size[0] // 2,
            self.draw_screen_size[1] // 2) + self.scroll

        # ograniczenie przesunięcia, żeby nie wychodziło poza granice mapy
        self.scroll.x = min(self.scroll.x, MAP_SIZE)
        self.scroll.x = max(self.scroll.x, -MAP_SIZE + self.draw_screen_size[0])
        self.scroll.y = min(self.scroll.y, MAP_SIZE)
        self.scroll.y = max(self.scroll.y, -MAP_SIZE + self.draw_screen_size[1])

        # utworzenie listy wszystkich węży na mapie
        all_snakes = [self.player]
        all_snakes.extend(self.enemies)

        # aktualizowanie węży przeciwników
        i = 0
        while i < len(self.enemies):

            # usuwanie z listy sprawdzanego węża (nie sprawdzamy kolizji z
            # samym sobą)
            other_snakes = [
                snake for snake in all_snakes if snake is not self.enemies[i]]

            # aktualizowanie węża
            self.enemies[i].update(self.food, other_snakes, self.dt)

            # dodanie cząsteczek, jeżeli prędkość węża jest większa niż
            # prędkość bazowa
            # sprawdzanie kolizji z innymi wężami
            if self.check_snake_collisions(self.enemies[i], other_snakes):

                # jeżeli wystąpiła kolizja, wąż jest usuwany z listy, a na
                # miejsce jego ciała są dodawane jedzenie i cząsteczki
                for body in self.enemies[i].body:
                    self.food.append(Food(body))
                    for _ in range(PARTICLE_AMOUNT):
                        self.particles.append(Particle(body))
                self.enemies.pop(i)
                self.enemies.append(Enemy())
            else:
                i += 1

        # aktualizowanie i sprawdzanie kolizji jedzenia
        i = 0
        while i < len(self.food):

            # aktualizowanie jedzenia
            self.food[i].update(self.dt)
            is_deleted = False

            # sprawdzanie, jedzenie już się pojawiło
            if self.food[i].spawn_timer == 0:

                # sprawdzanie każdego węża
                for snake in all_snakes:

                    # sprawdzanie dystansu pomiędzy głową węża a jedzeniem
                    if self.food[i].pos.distance_to(
                            snake.body[0]) < SNAKE_INTERLUDE + snake.body_size:

                        # usuwanie jedzenia
                        self.food.pop(i)

                        # sprawdzanie, czy nie przekroczono limitu ilości
                        # jedzenia na mapie
                        if len(self.food) < FOOD_LIMIT:

                            # dodawanie nowego jedzenia
                            self.add_food()

                        # zwiększanie węża
                        snake.grow()

                        # wyjście z pętli
                        is_deleted = True
                        break

            if not is_deleted:
                i += 1

        # aktualizowanie cząsteczek
        i = 0
        while i < len(self.particles):

            # aktualizowanie pojedynczej cząsteczki
            self.particles[i].update(self.dt)

            # sprawdzanie, czy już minął czas trwania cząsteczki
            if self.particles[i].timer <= 0:

                # usuwanie cząsteczki z listy
                self.particles.pop(i)
            else:
                i += 1

    def display_update(self):
        """Odświeżanie ekranu.
        """
        # rysowanie przeskalowanej płaszczyzny do rysowania na płaszczyźnie
        # ekranu
        self.screen.blit(
            transform.scale(self.draw_screen, SCREEN_SIZE), (0, 0))

        # odświeżenie ekranu
        display.update()


# wywołanie programu
if __name__ == '__main__':
    Main()
