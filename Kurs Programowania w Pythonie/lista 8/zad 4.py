import turtle as t
import random

WIELKOSC_MAPY = 100
ILOSC_WZGORZ = 10
PROBA = 100000

START_X = -250
START_Y = -250
WIELKOSC_PIXELA = 5

mapa = []
for y in range(WIELKOSC_MAPY):
    linia = []
    for x in range(WIELKOSC_MAPY):
        linia.append(0)
    mapa.append(linia)

# losowanie wzgorz
for i in range(ILOSC_WZGORZ):
    x, y = random.randint(0, WIELKOSC_MAPY - 1), random.randint(0, WIELKOSC_MAPY - 1)
    mapa[x][y] = 1000

# genrowanie terenu
for i in range(PROBA):
    x, y = random.randint(0, WIELKOSC_MAPY - 1), random.randint(0, WIELKOSC_MAPY - 1)
    WAGA = 0.085
    s = mapa[x][y] * WAGA
    d = WAGA
    for i in [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
        if 0 <= x + i[0] < WIELKOSC_MAPY and 0 <= y + i[1] < WIELKOSC_MAPY:
            if mapa[x + i[0]][y + i[1]] > 0:
                s += mapa[x + i[0]][y + i[1]]
                d += 1
    mapa[x][y] = s / d


# rysowanie
def kolor(n):
    kolory = [[0, 0.5, 0], [0.5, 1, 0], [1, 1, 0], [1, 0.5, 0], [1, 0, 0], [0.5, 0, 0]]
    return kolory[int(n / 1000 * (len(kolory) - 1))]


def rysuj_pixel(x, y, kolor):
    t.pu()
    t.goto((x * WIELKOSC_PIXELA) + START_X, (y * WIELKOSC_PIXELA) + START_Y)
    t.pd()
    t.color(kolor)
    t.begin_fill()
    for i in range(4):
        t.fd(WIELKOSC_PIXELA)
        t.rt(90)
    t.end_fill()


t.tracer(0, 0)

for x in range(WIELKOSC_MAPY):
    for y in range(WIELKOSC_MAPY):
        rysuj_pixel(x, y, kolor(mapa[x][y]))

t.tracer(1, 1)

input()
