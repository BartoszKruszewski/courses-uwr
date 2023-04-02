from losowanie_fragmentow import losuj_fragment


def fragment_dlugosc(n):
    fragment = losuj_fragment()
    while len(fragment) != n:
        fragment = losuj_fragment()
    return fragment


def losuj_haslo(n):
    if n == 0:
        return ""
    elif n <= 4:
        return fragment_dlugosc(n)
    elif n == 5:
        return fragment_dlugosc(2) + fragment_dlugosc(3)
    else:
        fragment = losuj_fragment()
        return fragment + losuj_haslo(n - len(fragment))


for i in range(10):
    print(losuj_haslo(6))
for i in range(10):
    print(losuj_haslo(18))
