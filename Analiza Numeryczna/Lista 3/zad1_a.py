from math import sqrt

def f(x):
    return (x ** 3 + sqrt(x ** 6 + 2023 ** 2)) ** -1

def better_f(x):
    return  sqrt(1 + x ** 6 / 2023 ** 2) / 2023 - x ** 3 / 2023 ** 2

try:
    # |x| >> 0
    #  x < 0
    print(f(-10000)) # dla -10000 mamy dzielenie przez 0
except Exception as e:
    print(e)

print(better_f(-10000))
