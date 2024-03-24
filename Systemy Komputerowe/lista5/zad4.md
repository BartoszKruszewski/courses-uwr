#### Definicja

Ta analiza różni się od analizy z poprzedniego tym,
że rozpatrujemy w niej zbiór dostępnych wyrażeń dla każdej zmiennej osobno.

#### Definicja $kill$ i $gen$

$kill([x := a]) = \{(x, a') | a' \in AEXP, x \in FV(a')\}$\
$kill([skip]) = \emptyset$ \
$kill([b]) = \emptyset$

$gen([x := a]) = \{(x, a') | a' \in AEXP(a), x \notin FV(a') \}$ \
$gen([skip]) = \emptyset$ \
$gen([b]) = \emptyset$

#### Postać równań

$IN(l) = \cap OUT(l')$\
$OUT(l) = IN(l) \cup gen(l) \setminus kill(l)$

Analiza jest typu $must$ bo używamy przekroju zbiorów do łączneia wyników z różnych ścieżek, oraz typu $forward$, ponieważ "idziemy do przodu" w przepływie sterowania.

#### Równania

```
OUT(1) = IN(1)
OUT(2) = IN(2)
OUT(3) = IN(3)
OUT(4) = IN(4)
OUT(5) = IN(5) U {(t, x + y)}
OUT(6) = IN(6) \ {(y, x + y), (t, x + y), (i, x + y)}
OUT(7) = IN(7)
OUT(8) = IN(8)
OUT(9) = IN(9)

IN(1) = {}
IN(2) = OUT(1)
IN(3) = OUT(2)
IN(4) = OUT(3) * OUT(8)
IN(5) = OUT(4)
IN(6) = OUT(5)
IN(7) = OUT(6)
IN(8) = OUT(7)
IN(9) = OUT(4)
```

#### Wyniki

```
IN(1) = {}
OUT(1) = IN(1) = {}
IN(2) = OUT(1) = {}
OUT(2) = IN(2) = {}
IN(3) = OUT(2) = {}
OUT(3) = IN(3) = {}
IN(4) = OUT(3) * OUT(8) = {} * OUT(8) = {}
OUT(4) = IN(4) = {}
IN(5) = OUT(4) = {}
OUT(5) = IN(5) U {x + y} = {(t, x + y)}
IN(6) = OUT(5) = {(t, x + y)}
OUT(6) = IN(6) \ {(y, x + y), (t, x + y), (i, x + y)} = {}
IN(7) = OUT(6) = {}
OUT(7) = IN(7) = {}
IN(8) = OUT(7) = {}
OUT(8) = IN(8) = {}
IN(9) = OUT(4) = {}
OUT(9) = IN(9) = {}
```
