Restoring Division:
```
for i in range(n):
    P, A <<
    P -= B
    A[n - 1] = not P[0]
    if P[0] == 1:
        P += B  (restoring)
return A
```

NonRestoring Division:
```
for i in range(n):
    P, A <<
    if P[0] == 1:
        P += B
    else
        P -= B
    A[n - 1] = not P[0]

if P < 0:
    P += B

return A
```

Algorytm jest podobny do restoring division.
Dla dodatniego P działa tak samo.
Dla ujemnego P, nie wykonujemy restore w rejestrze P,
więc P jest mniejsze o B od wersji restore.
Po przesunieciu P bedzie mniejsze o 2B od wersji restore,
czyli nadal bedzie ujemne wiec algorytm na pewno doda B, co wyrówna wynik.

dzielenie 7/3 (0111/0011)

0000 0111
przesunięcie
0000 111? 
odejmowanie
1101 1110

przesunięcie
1011 110? 
dodawanie
1110 1100

przesunięcie
1101 100? 
dodawanie
0000 1001

przesunięcie
0001 001?
odejmowanie
1110 0010

wyrownanie wyniku
0001 0010

reszta 1, wynik 2