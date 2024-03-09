```
A[n], B[n] - rejestry liczb A i B
P[n] - rejestr pomocniczy

for _ in range(n):
    P, A <<
    P = P - B
    A[n - 1] = not P[0]
    if P[0] == 1:
        P = P + B

A - wynik dzielenia A / B
P - reszta z dzielenia A % B
```

Przykład dzielenie liczb (7 / 3):\
A = 7 = 0111\
B = 3 = 0011\
P = 0 = 0000

P    A\
0000 1110 (P, A <<)\
1101 1110 (P = P - B)\
1101 1110 (A[n - 1] = not P[0])\
0000 1110 (if P[0] == 1: P = P + B)

0001 1100 (P, A <<)\
1110 1100 (P = P - B)\
1110 1100 (A[n - 1] = not P[0])\
0001 1100 (if P[0] == 1: P = P + B)

0011 1000 (P, A <<)\
0000 1000 (P = P - B)\
0000 1001 (A[n - 1] = not P[0])\
0000 1001 (if P[0] == 1: P = P + B)

0001 0010 (P, A <<)\
1110 0010 (P = P - B)\
1110 0010 (A[n - 1] = not P[0])\
0001 0010 (if P[0] == 1: P = P + B)

Wynik:\
P = 0001 = 1\
A = 0010 = 2\
2 * 3 + 1 = 7

