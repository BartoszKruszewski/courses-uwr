from nifs3 import get_s
import matplotlib.pyplot as plt

xs_data = [-7, -4, -2, 0, 1, 5, 10]
ys_data = [-16185, -10116, -6070, -2024, -1, 8091, 18206]
s = get_s(xs_data, ys_data)

f = lambda x: 2023 * x - 2024
for x, y in zip(xs_data, ys_data):
    print(f(x), y)

M = 1000
xs = [k / 100 for k in range(-100, 100)]
ys = [s(x) for x in xs]

plt.plot(xs, ys)
plt.show()

