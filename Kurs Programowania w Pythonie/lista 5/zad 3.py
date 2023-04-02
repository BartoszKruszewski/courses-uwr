from duze_cyfry import *
import turtle as t
import random

BOK = 10
START_X = -300
START_Y = 0

t.speed("fastest")


def kwadrat(x, y, kolor):
    t.pu()
    t.goto(x, y)
    t.pd()
    t.color(kolor)
    t.begin_fill()
    for i in range(4):
        t.fd(BOK)
        t.rt(90)
    t.end_fill()
    t.pu()


def losowy_kolor():
    return [random.randint(0, 255) / 255, random.randint(0, 255) / 255, random.randint(0, 255) / 255]


def rysuj_liczbe(n):
    kolory = []
    for cyfra in str(n):
        kolory.append(losowy_kolor())
    for y in range(5):
        linia = ""
        for cyfra in str(n):
            linia += daj_cyfre(int(cyfra))[y] + " "
        x = 0
        for znak in linia:
            if znak == "#":
                print(kolory[x // 6])
                kwadrat(START_X + x * BOK, START_Y - y * BOK, kolory[x // 6])
            x += 1


rysuj_liczbe("123456789")
input()
