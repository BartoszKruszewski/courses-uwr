from math import log

def I(n):
    res = log(2024 / 2023)
    for i in range(n):
        res = 1/n - 2023 * res
    return res

for i in range(1, 21):
    print(i, I(i))
