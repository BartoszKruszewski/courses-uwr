import turtle as t
import random

def kwadrat(a,kolor):
    t.pd()
    t.color((0,0,0))
    t.begin_fill()
    for i in range(4):
        t.fd(a)
        t.rt(90)
    t.color(kolor)
    t.end_fill()
    t.pu()

def losowy_jasny_kolor():
    return (random.randint(0, 155) / 255 + 100 / 255, random.randint(0, 155) / 255 + 100 / 255, random.randint(0, 155) / 255 + 100 / 255)

def losowy_ciemny_kolor():
    return (random.randint(0, 100) / 255, random.randint(0, 100) / 255, random.randint(0, 100) / 255)

a = 10
b = 5
c = 4

t.speed("fastest")

for rzedy_glowne in range(c):
    for kolumny_glowne in range(c):
        for rzedy in range(b):
            for kolumny in range(b):
                t.goto((rzedy_glowne * b + rzedy) * a, (kolumny_glowne * b + kolumny) * a)
                if rzedy_glowne % 2 == kolumny_glowne % 2:
                    kolor = losowy_ciemny_kolor()
                else:
                    kolor = losowy_jasny_kolor()
                kwadrat(a,kolor)

