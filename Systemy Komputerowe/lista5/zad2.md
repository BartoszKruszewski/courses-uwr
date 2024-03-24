#### Definicja

Analiza dostępnych wyrażeń to identyfikacja wyrażeń, które są dostępne (obliczone, nie zmienione) w danym momencie w programie.
Celem analizy jest eliminacja zbędnych obliczeń poprzez ponowne wykorzystanie wyników.

#### Definicja $kill$ i $gen$

$kill([x := a]) = \{a' \in AEXP | x \in FV(a') \}$ \
$kill([skip]) = \emptyset$ \
$kill([b]) = \emptyset$

$gen([x := a]) = \{a' \in AEXP(a) | x \notin FV(a') \}$ \
$gen([skip]) = \emptyset$ \
$gen([b]) = AEXP(b)$

Dla "złączenia ścieżek" bierzemy przekrój zbiorów.\
$IN(l) = OUT(l') \cap OUT(l'')$

#### Równania

```
OUT(1) = IN(1)
OUT(2) = IN(2)
OUT(3) = IN(3)
OUT(4) = IN(4)
OUT(5) = IN(5) U {x + y}
OUT(6) = IN(6) \ {x + y}
OUT(7) = IN(7) \ {x + y}
OUT(8) = IN(8) \ {i + 1}
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
OUT(5) = IN(5) U {x + y} = {x + y}
IN(6) = OUT(5) = {x + y}
OUT(6) = IN(6) \ {x + y} = {}
IN(7) = OUT(6) = {}
OUT(7) = IN(7) \ {x + y} = {}
IN(8) = OUT(7) = {}
OUT(8) = IN(8) \ {i + 1} = {}
IN(9) = OUT(4) = {}
OUT(9) = IN(9) = {}
```
