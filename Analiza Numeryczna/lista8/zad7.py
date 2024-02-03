from data import xs as xs_data, ys as ys_data
from nifs3 import get_s
import matplotlib.pyplot as plt

ts_data = [k / len(xs_data) for k in range(len(xs_data))]
sx = get_s(ts_data, xs_data)
sy = get_s(ts_data, ys_data)

M = 1000
us = [k / M for k in range(M)]

plt.plot(xs_data, ys_data)
plt.plot([sx(u) for u in us], [sy(u) for u in us])
plt.show()

