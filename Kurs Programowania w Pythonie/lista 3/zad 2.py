def czy_pierwsza(n):
    if n < 2:
        return False
    k = 2
    while k * k <= n:
        if n % k == 0:
            return False
        k += 1
    return True

ilosc_cyfr = 10
ilosc_siodemek = 7
siodemki = "7" * ilosc_siodemek
wolne_miejsca = ilosc_cyfr - ilosc_siodemek
licznik = 0
liczby = []

for i in range(pow(10, wolne_miejsca - 1), pow(10, wolne_miejsca)):
    str_liczba = str(i)
    for j in range(wolne_miejsca + 1):
        liczba = str_liczba[:j] + siodemki + str_liczba[j:]
        if liczba not in liczby:
            liczby.append(liczba)
            if czy_pierwsza(int(liczba)):
                licznik += 1

for i in range(pow(10, wolne_miejsca - 2), pow(10, wolne_miejsca - 1)):
    liczba = siodemki + "0" + str(i)
    if liczba not in liczby:
        liczby.append(liczba)
        if czy_pierwsza(int(liczba)):
            licznik += 1

print(licznik)





