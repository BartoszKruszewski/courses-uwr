```
A[n], B[n] - rejestry liczb a i b
P[n] - rejestr pomocniczy
RES[n] - rejestr wyjściowy

indeks 0 oznacza najbardziej znaczący bit

for i in n - 1 ... 0:
    # dodanie wyniku mnozenia A przez bit B do P
    P, c = P + A & B[i]

    # przesunięcie wyniku
    RES[i] = P[n - 1]
    P >>
    P[0] = c

return [P[0], ..., P[n - 1], RES[0], ..., RES[n - 1]]
```

Przykładowe obliczenia (9 * 3):\
A = 9 = 1001\
B = 3 = 0011

A & B[3] = 1001\
P + A & B[3] = 1001, 0\
RES = 0001\
P = 0100

A & B[2] = 1001\
P + A & B[2] = 1101, 0\
RES = 0011\
P = 0110

A & B[1] = 0000\
P + A & B[1] = 0110, 0\
RES = 0011\
P = 0011

A & B[0] = 0000\
P + A & B[0] = 0011, 0\
RES = 1011\
P = 0001

Wynik: 0001 1011 = 27 = 9 * 3






