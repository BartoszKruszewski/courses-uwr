def dlugosc_karna(n, k):
    i = 0
    while n > 0:
        n //= k
        i += 1
    return i


def liczba_karna(n, k):
    tab = [0] * dlugosc_karna(n, k)
    i = 0
    while n > 0:
        tab[i] = n % k
        n //= k
        i += 1
    return tab


def czy_palindrom(tab):
    n = len(tab)
    for i in range(n // 2):
        if tab[i] != tab[n - i - 1]:
            return False
    return True


def czy_karny_palindrom(n, k):
    return czy_palindrom(liczba_karna(n, k))


print(czy_karny_palindrom(1000, 10))
