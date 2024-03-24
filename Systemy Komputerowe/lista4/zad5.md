### Definicja

Zmienna jest **żywa**, jeśli bedzie wykorzystywana pozniej w programie.

Przykład:
```
x := 1
x := 2
```

Zmienna $x$ jest **martwa** na początku programu,
poniewaz pozniej w programie nigdzie nie wykorzystujemy jej przypisania,
a dalej jest jeszcze zmieniona.

### Definicje $kill$ oraz $gen$:

$kill([x := a]) = \{a\}$ \
$kill([skip]) = \emptyset$ \
$kill([b]) = \emptyset$

$gen([x := a]) = FV(a)$ \
$gen([skip]) = \emptyset$ \
$gen([b]) = FV(b)$

### Równania dla programu z zadania 1:

```
IN(1) = OUT(1) \ {x}
IN(2) = OUT(2) \ {y}
IN(3) = OUT(3) \ {i}
IN(4) = OUT(4) U {i, z}
IN(5) = OUT(5) \ {t} U {x, y}
IN(6) = OUT(6) \ {x} U {y}
IN(7) = OUT(7) \ {y} U {t}
IN(8) = OUT(8) \ {i} U {i}
IN(9) = OUT(9) \ {y} U {x}

OUT(1) = IN(2)
OUT(2) = IN(3)
OUT(3) = IN(4)
OUT(4) = IN(5)
OUT(5) = IN(6)
OUT(6) = IN(7)
OUT(7) = IN(8)
OUT(8) = IN(9)
OUT(9) = {}
```

### Rozwiazanie:

```
OUT(9) = {}
IN(9) = OUT(9) \ {y} U {x} = {x}
OUT(8) = IN(9) = {x}
IN(8) = OUT(8) \ {i} U {i} = {x, i}
OUT(7) = IN(8) = {x, i}
IN(7) = OUT(7) \ {y} U {t} = {x, i, t}
OUT(6) = IN(7) = {x, i, t}
IN(6) = OUT(6) \ {x} U {y} = {i, t, y}
OUT(5) = IN(6) = {i, t, y}
IN(5) = OUT(5) \ {t} U {x, y} = {i, x, y}
OUT(4) = IN(5) = {i, x, y}
IN(4) = OUT(4) U {i, z} = {i, x, y, z}
OUT(3) = IN(4) = {i, x, y, z}
IN(3) = OUT(3) \ {i} = {x, y, z}
OUT(2) = IN(3) = {x, y, z}
IN(2) = OUT(2) \ {y} = {x, z}
OUT(1) = IN(2) = {x, z}
IN(1) = OUT(1) \ {x} = {z}
```