from math import e, factorial
L = 10

def poisson(x, l):
    return l ** x * e ** -l / factorial(x)

for a in [2, 4, 6]:
    print(1 - sum(poisson(x, L) for x in range(a * L)))