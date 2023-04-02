from duze_cyfry import daj_cyfre

def wypisz_liczbe(n):
    napis = str(n)
    for i in range(5):
        linia = ""
        for j in napis:
            linia += daj_cyfre(int(j))[i] + " "
        print(linia)

wypisz_liczbe(1234567890)