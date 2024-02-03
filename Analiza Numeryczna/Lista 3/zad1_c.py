from math import atan, pi

def arcctg(x):
    return pi/2 - atan(x)

def f(x):
    return x ** -3 * (pi/2 - x - arcctg(x))

def better_f(x):
    return atan(x) / x ** 3 - x ** -2

def better_better_f(x):
    N = 10
    return sum((-1) ** (i + 1) * x ** i / (3 + 2 * i) for i in range(N))

print(f(0.0000001)) # dla x ~ 0 gubi cyfry znaczace
print(better_f(0.0000001))
print(better_better_f(0.0000001))