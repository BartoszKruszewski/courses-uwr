from test_range import test_range
from math import sqrt

def newton(x0, a, n = 5):
    xn = x0
    for _ in range(n):
        xn *= 0.5 * (3 - a * xn * xn)
    return xn

A = 9
EXP_VAL = 1 / sqrt(A)
for x0 in test_range(10):
    result = newton(x0, A)
    print(f'{x0}: {(abs(result - EXP_VAL) / EXP_VAL * 100):.0f}%')