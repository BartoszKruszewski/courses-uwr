import matplotlib.pyplot as pt
from interpolation import get_w
from aproxymation import Aproxymation

M = 100
N = 4 # od 4 jest git

with open('punkty.csv', 'r') as file:
    data = list(sorted(
        [tuple(float(v) for v in line.rstrip().split(', '))
        for line in file.readlines()],
        key= lambda x: x[0])
    )

f = lambda t: (t - 1.2) * (t + 4.7) * (t - 2.3)
w = get_w(data)
a = Aproxymation(data)

xs = [k / M for k in range(int(-4 * M), int(M * 5))]

# pt.plot(xs, [f(x) for x in xs])
pt.scatter([d[0] for d in data], [d[1] for d in data])
# pt.plot(xs, [w(x) for x in xs])
pt.plot(xs, [a(x, N) for x in xs])
pt.show()