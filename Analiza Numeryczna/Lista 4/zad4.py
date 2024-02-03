from math import log

def bisection(a, b, f):
    E = 10 ** -8

    m = (a + b) / 2
    if abs(f(m)) <= E:
        return m
    if f(a) * f(m) < 0:
        return bisection(a, m, f)
    return bisection(m, b, f)


print(bisection(-3, 0, lambda x: x ** 4 - log(x + 4)))
print(bisection(0, 3, lambda x: x ** 4 - log(x + 4)))
