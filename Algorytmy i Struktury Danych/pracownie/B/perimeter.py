from math import sqrt

a = (-8645409, 9232520)
b = (-8653139, 9297618)
c = (-8650012, 9297915)

def dist(a, b):
    return sqrt((a[0] - b[0]) * (a[0] - b[0]) + (a[1] - b[1]) * (a[1] - b[1]))

print(dist(a, b) + dist(b, c) + dist(c, a))