#### Algorytm

1. Przydzielenie $Q$ czasu
2. Jeżeli proces przerwał działanie szybciej (np czekanie na I/O) to następnym razem przydzielone mu zostanie $Q - P$ czasu.
3. Jeżeli proces wykorzystał cały przydzielony czas to dalej dostanie $Q$ czasu

#### Przykład

$Q_0 = 3$

P1:

- całkowity czas: $6$
- oczekiwanie na I/O: $2$

P2:

- całkowity czas: $9$
- bez oczekiwania na I/O

```
[P1--] [P2---] [P1-] [P2---] [P1--] [P2---] [P1-]
     2       5     6       9     11      14    15
```

#### Podsumowanie

Jak widać na przykładzie, mocno faworyzowane są procesy bez oczekiwania na operacja wejścia/wyjścia.
