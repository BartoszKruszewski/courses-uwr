#### Własność kompozycji

Zachodzi gdy:
- H1 na obiekcie X jest spójna
- H2 na obiekcie Y jest spójna
- H = H1 u H2 (na obu obiektach) również jest spójna

#### Kontrprzykład

Załóż dwa procesy P0 i P1 oraz dwa rejestry X i Y z wartościami początkowymi 0.

Weźmy H:
```
W(x, 1) - R(y) - 0
W(y, 1) - R(x) - 0
```

Wtedy H|x oraz H|y są sekwencyjnie spójne.

Wtedy H = H|x u H|y.

Warunki konieczne dla globalnej sekwencji:

- Porządek programowy P0: W(x, 1) < R(y).
- Porządek programowy P1: W(y, 1) < R(x).
- R(y) -> 0 wymaga R(y) < W(y, 1).
- R(x) -> 0 wymaga R(x) < W(x, 1).

Łącznie daje cykl:
W(x, 1) < R(y) < W(y, 1) < R(x) < W(x, 1)

Co daje W(x, 1) < W(x, 1) co jest sprzeczne.
