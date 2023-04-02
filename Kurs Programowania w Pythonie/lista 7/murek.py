from turtle import *


def kwadrat(bok):
    begin_fill()
    for i in range(4):
        fd(bok)
        rt(90)
    end_fill()


def murek(s, bok, c):
    i = 0
    for a in s:
        if c[i] == "x":
            color('black','black')
        elif c[i] == "y":
            color('black','red')
        elif c[i] == "z":
            color('black','green')
        i += 1
        if a == 'f':
            kwadrat(bok)
            fd(bok)
        elif a == 'b':
            kwadrat(bok)
            fd(bok)
        elif a == 'l':
            bk(bok)
            lt(90)
        elif a == 'r':
            rt(90)
            fd(bok)



color('black', 'yellow')

ht()

tracer(0, 0)  # szybkie rysowanie
BOK = 10
kwadraty = ""
kolory = ""
direction = True
for y in range(BOK):
    for x in range(BOK):
        kwadraty += "f"
        kolory += "y"
    if direction:
        kwadraty += "rfr"
        kolory += "yyy"
    else:
        kwadraty += "lfl"
        kolory += "zzz"
    direction = not direction

murek(kwadraty,10,kolory)

update()  # uaktualnienie rysunku

input()
