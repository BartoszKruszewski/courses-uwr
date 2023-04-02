import math


def invert(f, a, b, y, n=15):
    x = (a + b) / 2
    while n > 0 and f(x) != y:
        x = (a + b) / 2
        if f(x) > y:
            b = x
        else:
            a = x
        n -= 1
        print(x, math.sqrt(y), abs(x - math.sqrt(y)))
    return x


print(invert(lambda x: x * x, 0, 100, 100))
