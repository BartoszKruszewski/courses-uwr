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
