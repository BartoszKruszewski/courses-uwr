from math import sqrt

def f(x):
    return 4046 / (x ** 7 * sqrt(1 + 1 / x ** 14) + 1)

print(sqrt(1 + 1 / 0.001 ** 14) * 0.001 ** 7)
print(sqrt(1 + 1 / 0.001 ** 14) * 0.001 ** 7 + 1)
print(f(0.001))
