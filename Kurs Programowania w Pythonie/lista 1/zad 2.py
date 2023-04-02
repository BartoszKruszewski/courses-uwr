def silnia_rek(n):
    if n == 1:
        return 1
    else:
        return silnia_rek(n - 1) * n

def silnia(n):
    a = 1
    for i in range(1,n + 1):
        a *= i
    return a

def odmiana_gramatyczna(n):
    if n == 1:
        return "cyfrę"
    elif n in (2,3,4):
        return "cyfry"
    else:
        return "cyfr"

for i in range(1,101):
    liczba_cyfr = len(str(silnia(i)))
    print(f"{i}! ma {liczba_cyfr} {odmiana_gramatyczna(liczba_cyfr)}")
