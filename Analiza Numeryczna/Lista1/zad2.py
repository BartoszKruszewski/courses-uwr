from math import sqrt, pow

def f(x):
    return 4046 * (sqrt(pow(x, 14) + 1) - 1) / pow(x, 14)

print(pow(0.001, 14))
print(pow(0.001, 14) + 1)
print(pow(0.001, 14) + 1 - 1)

print(f(0.001))