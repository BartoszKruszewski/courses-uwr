import turtle as t
import time

t.tracer(0, 0)
FRAME_RATE = 1 / 60

t.pensize(3)


def tecza(n):
    return hsv_to_rgb(n % 360, 1, 1)


def hsv_to_rgb(h, s, v):
    c = v * s
    x = c * (1 - abs((h / 60) % 2 - 1))
    m = v - c

    r = 0
    g = 0
    b = 0

    if 0 <= h < 60:
        r = c
        g = x
    elif 60 <= h < 120:
        r = x
        g = c
    elif 120 <= h < 180:
        g = c
        b = x
    elif 180 <= h < 240:
        g = x
        b = c
    elif 240 <= h < 300:
        r = x
        b = c
    elif 300 <= h < 360:
        r = c
        b = x

    return (r + m, g + m, b + m)


def square(n):
    for i in range(4):
        t.fd(n)
        t.rt(90)


def polkole(n):
    global kolor
    kolor += 1 / 10
    t.color(tecza(kolor))
    E = 10
    for i in range(E):
        t.fd(n)
        t.rt(180 / E)


def spirala(n):
    def xxx():
        for i in range(n + n % 2):
            polkole(Fibonacci(i))

    return xxx


def Fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    a = 1
    b = 1
    x = a + b
    for i in range(n - 3):
        b = a
        a = x
        x = a + b
    return x


def repeatOnCircle(figure, r, n, angle):
    t.rt(angle)
    for i in range(n):
        t.pu()
        t.rt(360 / n)
        t.fd(r)
        t.pd()
        figure()
        t.pu()
        t.bk(r)
    t.lt(angle)


D1 = 5
D2 = 6
kat = 0
kolor = 0
while True:
    t0 = time.time()
    t.clear()
    repeatOnCircle(lambda: repeatOnCircle(spirala(10), 80, 6, kat / 2), 200, 5, kat)
    kat += D2
    t.update()
    delta = time.time() - t0
    if delta < FRAME_RATE:
        time.sleep(FRAME_RATE - delta)
