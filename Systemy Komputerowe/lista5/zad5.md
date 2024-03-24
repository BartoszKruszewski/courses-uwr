### Definicje $kill$ oraz $gen$:

#### Równania przepływu

$OUT(l) = \cup {IN(l')}$\
$IN(l) = OUT(l) \setminus kill(l) \cup gen(l)$

Analiza jest typu $may$ bo używamy sumy zbiorów do łączneia wyników z różnych ścieżek, oraz typu $backward$, ponieważ "cofamy się" w przepływie sterowania.
