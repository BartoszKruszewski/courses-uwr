from math import e, factorial
print(f'{1 - sum(20 ** k * e ** -20 / factorial(k) for k in range(41)):.10f}')