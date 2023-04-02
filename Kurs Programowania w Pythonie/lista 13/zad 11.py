# zad 4 2019
import math


def wczytaj_mape(nazwa_pliku):
    return [list(l.rstrip()) for l in open(nazwa_pliku, "r").readlines()]


def odleglosc(x1, x2, y1, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def zbadaj_koordynaty_stanowisk(mapa):
    koordynaty = []
    for y in range(len(mapa)):
        for x in range(len(mapa[0])):
            if mapa[y][x] == "#":
                koordynaty.append((x,y))
    return koordynaty

M = wczytaj_mape("mapa.txt")
K = zbadaj_koordynaty_stanowisk(M)
odleglosci = []
for i in K:
    for j in K:
        odleglosci.append(odleglosc(i[0],i[1],j[0],j[1]))

print(max(odleglosci)) # max odleglosc
print(sum(odleglosci)/len(odleglosci)) # srednia odleglosc
print(len(K)/(len(M)*len(M[0]))) # srednia liczba stanowisk na kwadrat jednostkowy mapy

