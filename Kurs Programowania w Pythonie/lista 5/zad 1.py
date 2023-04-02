def F(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1


def energia_liczby(n):
    l = 0
    while n != 1:
        l += 1
        n = F(n)
    return l


def mediana(lista):
    if len(lista) % 2 == 1:
        return lista[len(lista) // 2]
    else:
        return (lista[len(lista) // 2] + lista[len(lista) // 2 + 1]) / 2


def analiza_collatza(a, b):
    energie = []
    for i in range(a, b + 1):
        energie.append(energia_liczby(i))
    print("Średnia:", sum(energie) / len(energie))
    print("Mediana:", mediana(energie))
    print("Maksimum:", max(energie))
    print("Minimum:", min(energie))


analiza_collatza(1, 100)
