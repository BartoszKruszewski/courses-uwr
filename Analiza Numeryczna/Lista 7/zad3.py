import matplotlib.pyplot as plt
from math import prod, cos, pi

def frange(start, stop, step):
    points = []
    while start < stop:
        points.append(start)
        start += step
    return points

def p(points):
    return lambda x: prod([x - point for point in points])

def eq_points(n):
    return frange(-1, 1, 2 / n)

def c_points(n):
    return [cos((2 * k + 1) / (2 * n + 2) * pi) for k in range(0, n + 1)]

ps1 = [p(eq_points(n)) for n in range(4, 21)] # rownoodlegle
ps2 = [p(c_points(n)) for n in range(4, 21)]  # wezly Czebyszewa

xs = frange(-1, 1, 0.01)

N = 20 # wybor odpowiedniego n, -1 oznacza wszystkie

if N == -1:
    for p1, p2 in zip(ps1, ps2):
        ys1 = [p1(x) for x in xs]
        ys2 = [p2(x) for x in xs]
        plt.plot(xs, ys1)
        plt.plot(xs, ys2)
else:
    ys1 = [ps1[N - 4](x) for x in xs]
    ys2 = [ps2[N - 4](x) for x in xs]
    plt.plot(xs, ys1)
    plt.plot(xs, ys2)
plt.show()
