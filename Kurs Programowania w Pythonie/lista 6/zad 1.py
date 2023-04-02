import turtle as t
import duze_cyfry
import random

WIELKOSC_PLANSZY = 30
WIELKOSC_KWADRATU = 10
ILOSC_PROB = 100
KOLORY = ["red", "blue", "green", "purple", "yellow", "brown", "orange", "pink"]

t.speed(10.5)
plansza = []


def daj_punkty(n):
    N = 5
    P = []
    cyfra = duze_cyfry.cyfry[n].split("\n")[1:]
    for y in range(N):
        for x in range(len(cyfra[y])):
            if cyfra[y][x] == "#":
                P.append((x, y))
    return P


def czy_wolne(x, y, n, plansza, kolor):
    punkty = daj_punkty(n)
    for i in punkty:
        if plansza[i[1] + y][i[0] + x] != "puste":
            return False
        else:
            if plansza[i[1] + y + 1][i[0] + x] == kolor or plansza[i[1] + y][i[0] + x + 1] == kolor or plansza[i[1] + y - 1][
                i[0] + x] == kolor or plansza[i[1] + y][i[0] + x - 1] == kolor:
                return False
    return True


def dodaj_do_planszy(x, y, n, plansza, kolor):
    punkty = daj_punkty(n)
    for i in punkty:
        plansza[i[1] + y][i[0] + x] = kolor


def rysuj_cyfre(x, y, n, kolor):
    PRZESUNIECIE_X = 300
    PRZESUNIECIE_Y = 300
    punkty = daj_punkty(n)
    for i in punkty:
        t.pu()
        t.goto((i[0] - x) * WIELKOSC_KWADRATU + PRZESUNIECIE_X, (-i[1] - y) * WIELKOSC_KWADRATU + PRZESUNIECIE_Y)
        t.pd()
        t.begin_fill()
        t.color("black")
        for i in range(4):
            t.fd(WIELKOSC_KWADRATU)
            t.rt(90)
        t.color(kolor)
        t.end_fill()


for y in range(WIELKOSC_PLANSZY):
    linia = []
    for x in range(WIELKOSC_PLANSZY):
        linia.append("puste")
    plansza.append(linia)

for i in range(ILOSC_PROB):
    n = random.randint(0, 9)
    kolor = random.choice(KOLORY)
    x = random.randint(1, WIELKOSC_PLANSZY - 6)
    y = random.randint(1, WIELKOSC_PLANSZY - 6)
    if czy_wolne(x, y, n, plansza, kolor):
        dodaj_do_planszy(x, y, n, plansza, kolor)
        rysuj_cyfre(x, y, n, kolor)

input()
