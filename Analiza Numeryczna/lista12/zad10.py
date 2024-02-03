from numpy import zeros as Array
from math import sin, pi

def romberg(func, a, b, m, k):
    h = b - a

    t = Array((m + 1, k + 1))
    t[0, 0] = 0.5 * h * (func(a) + func(b)) 

    for i in range(1, m + 1):
        h *= 0.5
        s = sum(func(a + j * h) for j in range(1, 2 ** i, 2))
        t[i, 0] = 0.5 * t[i - 1, 0] + s * h

        for j in range(1, min(i, k) + 1):
            mult = 4 ** j
            t[i, j] = (mult * t[i, j - 1] - t[i, j - 1]) / (mult - 1)

    return t[m, k]

func_a = lambda x: 2024 * x ** 8 - 1977 * x ** 4 - 1981
func_b = lambda x: 1 / (1 + x ** 2)
func_c = lambda x: sin((5 * x) - (pi / 3))

print(romberg(func_a, -3, 2, 20, 20)) # git
print(romberg(func_b, -3, 3, 20, 20)) # dokladnosc do 13 miejsca
print(romberg(func_c, -3 * pi, pi / 6, 20, 20)) # dokladnosc do 14 miejsca
