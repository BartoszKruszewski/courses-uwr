#### Definicja

Historię G może powstać przez zakończenie lub odrzucenie niezakończonych wywołań. Wszystkie wywołania na diagramach są zakończone, więc traktujemy G jako identyczną do H.

Trzeba sprawdzić czy da się ułożyć sekwencyjną historię S, która:
- Zachowuje wszystkie relacje uporządkowania z H
- Jest legalna (każdy read zwraca wartość z ostatniego write)

#### Diagram 1

Historia G:
```
B: r.write(1)
A: r.read(1)
C: r.write(2)
A: r: 1
C: r: void
B: r: void
B: r.read(2)
B: r: 2
```

Historia S:
```
B: r.write(1)
B: r: void
A: r.read(1)
A: r: 1
C: r.write(2)
C: r: void
B: r.read(2)
B: r: 2
```

Kolejność G:
```
B r.write(1) => B r.read(2)
A r.read(1) => B r.read(2)
C r.write(2) => B r.read(2)
```

Kolejność S:
```
B r.write(1) => A r.read(1) => C r.write(2) => B r.read(2)
```

#### Diagram 2

Historia G:
```
B: r.write(1)
A: r.read(1)
C: r.write(2)
A: r: 1
C: r: void
B: r: void
B: r.read(1)
B: r: 1
```

Historia S:
```
C: r.write(2)
C: r: void
B: r.write(1)
B: r: void
A: r.read(1)
A: r: 1
B: r.read(1)
B: r: 1
```

Kolejność G:
```
C r.write(2) -> B r.read(1),
B r.write(1) -> B r.read(1),
A r.read(1) -> B r.read(1)
```

Kolejność S:
```
C r.write(2) -> B r.write(1) -> A r.read(1) -> B r.read(1)
```

#### Diagram 3

Historia G:
```
A: p.enq(x)
A: p: void
B: p.enq(y)
B: p: void
A: p.deq(y)
A: p: y
```

G nie odpowiada żadnej legalnej sekwencyjnej historii S.

```
p.enq(x) -> p.enq(y) -> p.deq(y)
```

Co jest sprzeczne.

#### Diagram 4

Historia G:
```
A: p.enq(x)
A: p: void
B: q.enq(y)
B: q: void
A: q.enq(x)
A: q: void
B: p.enq(y)
B: p: void
A: p.deq(y)
A: p: y
B: q.deq(x)
B: q: 
```

G nie odpowiada żadnej legalnej sekwencyjnej historii S, 

```
p.enq(x) -> p.enq(y) -> p.deq(y)
q.enq(y) -> q.enq(x) -> q.deq(x)
```

Co jest sprzeczne.
