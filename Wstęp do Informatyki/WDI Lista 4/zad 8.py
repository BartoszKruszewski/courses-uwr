def ile_cyfr(n):
    tab = [0] * 10
    while n > 0:
        tab[n % 10] += 1
        n //= 10
    return tab


def czy_podobne(n, m):
    ile_cyfr_n = ile_cyfr(n)
    ile_cyfr_m = ile_cyfr(m)

    for i in range(10):
        if ile_cyfr_n[i] != ile_cyfr_m[i]:
            return False
    return True


print(czy_podobne(11223344, 11341234))
