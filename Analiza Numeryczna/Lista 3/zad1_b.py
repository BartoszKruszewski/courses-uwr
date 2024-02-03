from math import log2

def f(x):
    return log2(x) - 2

def better_f(x):
    return log2(x / 4)

# utrata cyfr znaczacych dla x ~ 4
print(f(4))
print(f(4 + 10 ** -10))

print(better_f(4))
print(better_f(4 + 10 ** -10))