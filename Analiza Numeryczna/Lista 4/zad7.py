from math import sqrt
from test_range import test_range, get_e

def newton(m, c, x0):
    e = get_e()

    xn = x0
    i = 0
    
    if c % 2 != 0:
        m *= 2

    while abs(xn - sqrt(m)) >= e and abs(xn - (xn / 2 + m / (2 * xn))) >= e:
        i += 1
        xn = xn / 2 + m / (2 * xn)
        if abs(xn) > 10 ** 6:
            return 0, 0
        
    if c % 2 == 0:
        xn *= 2 ** (c // 2)
    else:
        xn *= 2 ** ((c - 1) // 2)
    return xn, i

M = 0.78125
C = 5
for x0 in test_range(100):
    xn, i = newton(M, C, x0)
    print(x0, 'inf' if xn == 0 else xn, i)


    