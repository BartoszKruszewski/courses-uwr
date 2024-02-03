from data import W_data, w_data
from bezier import bezier
import matplotlib.pyplot as plt

p = bezier(W_data, w_data)
M = 1000
ts = [i / M for i in range(M)]
ws = [p(x) for x in ts]

plt.plot([w[0] for w in ws], [w[1] for w in ws])
plt.show()