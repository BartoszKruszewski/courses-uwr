def czy_pierwsza(n):
    if n < 2:
        return False
    k = 2
    while k * k <= n:
        if n % k == 0:
            return False
        k += 1
    return True


licznik = 0
for i in range(100000):
    if czy_pierwsza(i) and "777" in str(i):
        licznik += 1
        print(i)
print(licznik)