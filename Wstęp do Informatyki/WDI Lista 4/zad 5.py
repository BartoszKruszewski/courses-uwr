def dlugosc_bin(n):
    i = 0
    while n > 0:
        n //= 2
        i += 1
    return i


def bin(n):
    tab = [0] * dlugosc_bin(n)
    i = 0
    while n > 0:
        tab[i] = n % 2
        n //= 2
        i += 1
    return tab


def czy_palindrom(tab):
    n = len(tab)
    for i in range(n // 2):
        if tab[i] != tab[n - i - 1]:
            return False
    return True


def czy_binarny_palindrom(n):
    return czy_palindrom(bin(n))

print(czy_binarny_palindrom(50))

