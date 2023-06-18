"""Moduł zawierający stałe wykorzystywane w grze.
"""

STANDARD_FRAMERATE = 60
"""Liczba klatek na sekundę, dla której wyznaczane są stałe gry."""

FRAMERATE = 60
"""Maksymalna liczba klatek na sekundę."""

SCREEN_SIZE = (1280, 720)
"""Wielkość okna gry."""

START_DRAW_SCREEN_SIZE = (320, 180)
"""Wielkość płaszczyzny do rysowania."""

MINIMUM_DRAW_SCREEN_SIZE = (180, 90)
"""Minimalna wielkość płaszczyzny do rysowania."""

ZOOM_SPEED = 1.2
"""Prędkość przybliżania mapy."""

MAP_SIZE = 1000
"""Wielkość mapy."""

FOOD_SPAWN_TIME = 20
"""Czas pojawiania się jedzenia."""

SNAKE_BASE_SPEED = 0.6
"""Początkowa prędkość węża."""

SNAKE_BOOST_SPEED = 1.5
"""Prędkość węża przy przyśpieszeniu."""

SNAKE_ACCELERATION = 0.03
"""Przyśpieszenie węża."""

SNAKE_START_LENGTH = 5
"""Początkowa długość węża."""

SNAKE_START_SIZE = 4
"""Początkowy promień "komórki" węża."""

SNAKE_INTERLUDE = 5
"""Odstęp pomiędzy "komórkami" węża."""

SNAKE_SPAWN_TIME = 40
"""Czas pojawiania się węża."""

BACKGROUND_COLOR = (40, 40, 40)
"""Kolor tła."""

FOOD_COLORS = (
    (0, 255, 0), (0, 200, 20), (20, 140, 10), (40, 255, 10), (5, 230, 80))
"""Kolory jedzenia."""

SNAKE_COLORS = (
    (180, 100, 120), (60, 20, 205), (10, 180, 20), (80, 100, 20),
    (240, 180, 25), (42, 90, 205), (87, 10, 120), (78, 100, 100))
"""Kolory węży."""

SNAKE_FADE = 4
"""Siła efektu gradientu na ciele węża."""

PARTICLE_COLORS = (
    (255, 255, 255, 255), (220, 220, 220, 255), (220, 0, 220, 255),
    (110, 0, 110, 255))
"""Kolory cząsteczek."""

PARTICLE_SIZE = (1, 4)
"""Wielkość cząsteczek."""

PARTICLE_TIME = 500
"""Czas trwania cząsteczek."""

PARTICLE_SPEED = 0.5
"""Prędkość cząsteczek."""

PARTICLE_AMOUNT = 5
"""Ilość cząsteczek generowanych przy każdej "komórce" węża."""

START_FOOD_AMOUNT = 150
"""Początkowa ilość jedzenia na mapie."""

FOOD_LIMIT = 200
"""Maksymalna ilość jedzenia na mapie."""

ENEMY_AMOUNT = 25
"""Ilość przeciwników na mapie."""

AI_UPDATE_TIME = 20
"""Odstęp czasu pomiędzy odświeżeniem AI."""

FOOD_TO_GROW = 5
"""Ilość jedzenia, którą musi zjeść wąż, żeby urosnąć o jedną "komórkę"
więcej"""

AI_SPEED_UP_DISTANCE = 200
"""Dystans, po którego przekroczeniu AI przyśpiesza w kierunku celu."""

SNAKE_FOOD_CONSUMPTION_SPEED = 0.1
"""szybkość "spalania" jedzenia podczas przyśpieszenia węża."""

AI_ATTACK_FOCUS_DISTANCE = 100
"""Zasięg w jakim AI zaczyna atakować inne węże."""

AI_SAFETY_DISTANCE = 20
"""Odległość od węża po przekroczeniu, której AI będzie zawracać unikając 
kolizji"""

