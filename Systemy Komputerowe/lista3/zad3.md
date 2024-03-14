```
# przesuniecie rejestrow az pierwszym bitem B bedzie 1
k = 0

while B[0] == 0:
    B <<
    P, A <<
    k += 1

for _ in range(n):
    if P[0] == P[1] == P[2]:
        A[n - 1] = 0
        P, A <<
    else:
        A[n - 1] = 1
        P, A <<
        if P[0] == 1:
            P += B
        else:
            P -= B
        
if P[0] == 1:
    P += B        
    A -= 1

P, A >> k
```

Przykład: 7/3 (0111/0011)

przesuniecie o k (k = 2) bitów w lewo
P, A = 00001 1100
B = 1100

00001 1100 zapalenie A[n - 1]
00011 1000 przesuniecie

00011 1000 zapalenie A[n - 1]
00111 0000 przesuniecie

00111 0001 zapalenie A[n - 1]
01110 0010 przesuniecie
01000 0110 odejmowanie

01000 0111 zapalenie A[n - 1]
10000 1110 przesuniecie
11100 1110 dodawanie

10000 1101 wyrownanie wyniku
00100 0011 



