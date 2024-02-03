from math import sqrt

def x(k):
    if k == 1:
        return 2
    return 2 ** (k - 1) * sqrt(2 * (1 - sqrt(1 - (x(k - 1) / 2 ** (k - 1)) ** 2)))

def better_x(k):
    if k == 1:
        return 2
    prev_x = better_x(k - 1)
    return prev_x * sqrt(2 / (1 + sqrt(1 - (prev_x / 2 ** (k - 1)) ** 2)))

for i in range(1, 100):
    print(better_x(i))