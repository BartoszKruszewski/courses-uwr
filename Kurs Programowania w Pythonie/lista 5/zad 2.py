import turtle as t

t.speed(0)


def bok(n):
    if n > 10:
        bok(n / 2)
        t.lt(90)
        bok(n / 3)
        t.rt(90)
        bok(n / 3)
        t.rt(90)
        bok(n / 3)
        t.lt(90)
        bok(n / 2)
    else:
        t.fd(n)


def platek():
    for i in range(4):
        bok(100)
        t.rt(90)


platek()
input()
