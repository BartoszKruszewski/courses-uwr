Algorytm Booth'a mnozenia liczb dodatnich:
```
A, B - rejestry z n-bitowymi liczbami do mnozenia
P - rejestr pomocniczy
L - rejestr jednoelementowy do wykrywania rodzaju operacji

while i > n:
    if A[n - 1] == L:
        P, A, L >>
        i++
    elif A[n - 1] == 1 and L == 0:
        P += B
    else A[n - 1] == 0 and L == 1:
        P -= B

return [P..., A...]
```

Mnozac liczby ze znakiem postepujemy identcznie,
z tym ze na koniec sprawdzamy bit A[n - 1],
jest to przesuniety bit znaku i XORujemy go z B[0],
a nastepnie dopisujemy do wyniku jako bit znaku.