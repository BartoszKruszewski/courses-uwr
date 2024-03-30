#### Przykład

W pierwszym przypadku zmienne silne zywe nie róznią się od zwyklych zywych.
Natomiast w drugim przykladzie widzimy ze x jest uzywany tylko do zdefioniowania y,
wiec jest zywy (bo jest wykorzystywany do przypisania), ale nie jest silnie zywy, 
poniewaz y jest martwy.

#### Definicje $kill$ oraz $gen$:

Oznaczmy $SL(l)$ jako zbiór zmiennych silnie
zywych w dla $OUT(l)$

$kill([x := a]) = \{x\}$ \
$kill([skip]) = \emptyset$ \
$kill([b]) = \emptyset$

$gen([x := a]) = {a' | a' \in FV(a) \land x \in SL(l)}$ \
$gen([skip]) = \emptyset$ \
$gen([b]) = FV(b)$

Róznica pomiedzy standardowymi zmiennymi zywymi polega na tym, ze sprawdzamy, w momencie dodawania nowej zmiennej do zbioru, czy przypisywana jest ona zmiennej zywej, czyli takiej którą wybraliśmy wcześniej.

#### Równania przepływu

$OUT(l) = \cup {IN(l')}$\
$IN(l) = OUT(l) \setminus kill(l) \cup gen(l)$

Analiza jest typu $may$ bo używamy sumy zbiorów do łączneia wyników z różnych ścieżek, oraz typu $backward$, ponieważ "cofamy się" w przepływie sterowania.
