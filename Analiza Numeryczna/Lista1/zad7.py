from math import e

for k in range(20):
    print(k, 2000000 * (1 - 2 / e) ** k)

# k wynosi pomiędzy 9 a 10, takze 10 wystarczy zeby osiagnac odpowiednio maly blad
