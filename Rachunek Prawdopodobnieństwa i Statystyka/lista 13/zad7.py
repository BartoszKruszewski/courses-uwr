from scipy.stats import chi2, norm
from math import sqrt

for r in (range(21), range(20, 41)):
    for n in (10, 20, 40):
        m = 0
        argm = None
        for z in r:
            x = abs((chi2.cdf(sqrt(2 * n) * z / 10 + n, n)) - norm.cdf(z / 10))
            if x > m:
                m = x
                argm = z / 10
        print(f'n: {n}, argmax: {argm}, max: {m}')
