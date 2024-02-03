from math import cos, pow

def f(x):
    return 14 * (1 - cos(17 * x)) / pow(x, 2)

for i in range(11, 21):
    print(f(pow(10, -1 * i)))

print(cos(17 * pow(10, -11)))