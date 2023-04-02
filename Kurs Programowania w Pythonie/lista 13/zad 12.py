# zad 5 2019

import turtle as t


def repeatOnFigure(d, n, mult):
    PRECISION = 10
    if d >= PRECISION:
        t.pd()
        for i in range(n):
            t.rt(360 // n)
            t.fd(d)
            repeatOnFigure(d * mult, n, mult)


t.tracer(0, 0)

repeatOnFigure(300, 3, 0.5) # trojkat
#repeatOnFigure(300, 4, 0.5) # kwadrat
#repeatOnFigure(200, 4, 0.3) # kwadrat2
#repeatOnFigure(200, 6, 0.3)  # hex

t.tracer(1, 1)
input()
