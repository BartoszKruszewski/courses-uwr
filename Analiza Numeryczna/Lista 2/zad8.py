from math import sin

def f(x):
    return 28 * sin(17 / 2 * x) ** 2 / x ** 2

for i in range(10, 21):
    print(f(10 ** -i))
    