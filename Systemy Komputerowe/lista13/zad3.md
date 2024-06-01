#### FCFS (First-Come, First-Served)

Najpierw wykonywane są procesy, które zostały pierwsze wprowadzone.

```
[P1--] [P2-] [P3--------] [P4----] [P5-----]
     2     3           11        15       20
```

Czasy przetworzenia:

- P1: $2$
- P2: $3$
- P3: $11$
- P4: $15$
- P5: $20$

Czasy oczekiwania:

- P1: $0$
- P2: $2$
- P3: $3$
- P4: $11$
- P5: $15$
- Średni: $(0 + 2 + 3 + 11 + 15) / 5 = 6.2$

#### SJF (Shortest-Jobs-First)

Najpierw wykonywane są najkrótsze procesy.

```
[P2-] [P1--] [P4----] [P5-----] [P3--------]
    1      3        7        12           20
```

Czasy przetworzenia:

- P1: $3$
- P2: $1$
- P3: $20$
- P4: $7$
- P5: $12$

Czasy oczekiwania:

- P1: $1$
- P2: $0$
- P3: $12$
- P4: $3$
- P5: $7$
- Średni: $(1 + 0 + 12 + 3 + 7) / 5 = 4.6$

#### Priorytetowy bez wywłaszczeń

Procesy są wykonywane zgodnie z kolejnością priorytetów.

```
[P3--------] [P5-----] [P1--] [P4----] [P2-]
           8        13     15       19    20
```

Czasy przetworzenia:

- P1: $15$
- P2: $20$
- P3: $8$
- P4: $19$
- P5: $13$

Czasy oczekiwania:

- P1: $13$
- P2: $19$
- P3: $0$
- P4: $15$
- P5: $8$
- Średni: $(13 + 19 + 0 + 15 + 8) / 5 = 11$

#### Karuzelowy z Q = 2

Procesy są wykonywane po Q faz w kolejności w jakiej zostały wczytane.

```
[P1--] [P2-] [P3--] [P4--] [P5--] [P3--] [P4--] [P5--] [P3--] [P5-] [P3--]
     2     3      5      7      9     11     13     15     17    18     20
```

Czasy przetworzenia:

- P1: $2$
- P2: $3$
- P3: $20$
- P4: $13$
- P5: $18$

Czasy oczekiwania:

- P1: $0$
- P2: $2$
- P3: $3 + 4 + 4 + 1 = 12$
- P4: $5 + 4 = 9$
- P5: $7 + 4 + 2 = 13$
- Średni: $(0 + 2 + 12 + 9 + 13) / 5 = 7.2$
