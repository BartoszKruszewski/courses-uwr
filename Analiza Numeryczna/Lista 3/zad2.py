from math import sqrt

def get_roots(a, b, c):
    x1 = (-b + sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    x2 = (-b - sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    return x1, x2

def better_get_roots(a, b, c):
    if b > 0:
        x1 = (-b - sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    else:
        x1 = (-b + sqrt(b ** 2 - 4 * a * c)) / (2 * a)

    return x1, c / a / x1

print(get_roots(1, 10 ** 31, 1))
print(get_roots(1, -10 ** 31, 1))

print(better_get_roots(1, 10 ** 31, 1))
print(better_get_roots(1, -10 ** 31, 1))