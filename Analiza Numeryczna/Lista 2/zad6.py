from math import sqrt

def l(xs):
    return sqrt(sum(x ** 2 for x in xs))

def better_l(xs):
    d = 1
    s = 0
    for x in xs:
        d *= x
    for x in xs:
        u = x / d
        s += u * u
    return sqrt(s) * abs(d)

numbers = (12, 5, -18, 82, 47)
print(l(numbers))
print(better_l(numbers))