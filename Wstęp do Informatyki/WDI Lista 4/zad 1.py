def a(n):
    wynik = 1
    for i in range(n):
        wynik *= -1
    wynik *= n
    return wynik


def b(n):
    wynik = 0
    znak = 1
    for i in range(1, n + 1):
        znak *= -1
        wynik += znak / i
    return wynik


def c(n, x):
    wynik = 0
    y = 1
    for i in range(1, n + 1):
        y *= x
        wynik += y * i
    return wynik


print(a(4))
print(b(4))
print(c(4, 10))
