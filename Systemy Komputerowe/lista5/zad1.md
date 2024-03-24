#### Definicja

Analiza "use-definition" pozwala na ustalenie,
skąd pochodzi wartość zmiennej, oraz jak jest wykorzystywana.
Pozwala to na optymalizację, poprzez usunięcie zbędnych obliczeń,
oraz optymalizację pamięciową poprzez zwolnienie zmiennych,
które nie będą już używane.

#### Definicja formalna

$def(x, l)$ - blok $l$ przypisuje wartość do zmiennej $x$\
$clear(x, l, l')$ - żaden z bloków na ścieżce z $l$ do $l'$ nie przypisuje wartości do zmiennej $x$, ale $l'$ odwołuje się do $x$ (bez przypisywania $x$ wartości).

$ud(x, l') = \{l | def(x, l) \land \exists l'':(l,l'')\in flow(S) \in clear(x, l'', l')\}\cup \{?|clear(x, init(S),l')\}$

#### Definicja alternatywna

$ud(x, l') = \{l' | (x, l') \in RD_{entry}(l)\} if x \in gen(B^l)$

#### Zbiory $RD_\circ$

```
1. {(x,?), (y,?), (z,?), (i,?), (t,?)}
2. {(x,1), (y,?), (z,?), (i,?), (t,?)}
3. {(x,1), (y,2), (z,?), (i,?), (t,?)}
4. {(x,1), (x,6), (y,2), (y,7), (z,?), (i,3), (i,8), (t,5)}
5. {(x,1), (x,6), (y,2), (y,7), (z,?), (i,3), (i,8), (t,5)}
6. {(x,1), (x,6), (y,2), (y,7), (z,?), (i,3), (i,8), (t,5)}
7. {(x,6), (y,2), (y,7), (z,?), (i,3), (i,8), (t,5)}
8. {(x,6), (y,7), (z,?), (i,3), (i,8), (t,5)}
9. {(x,1), (x,6), (y,2), (y,7), (z,?), (i,3), (i,8), (t,5)}
```

#### Intuicja

jeżeli intrukcja o etykiecie l odwołuje się do $x$ (bez przypisywanie wartości $x$) to $ud(x, l)$ to zbiór etykiet intruckji, które ostanie przypisywały wartość $x$. Zbiór może mieć więcej niż jedną etykietę, jeżeli nastąpiło "rozgałęzienie" w przepływie sterowania. Znak ? przypisujemy jeżeli x nie zostało wcześniej przypisane.

#### Wynik

```
   x      y      z   t   i
1. 0      0      0   0   0
2. 0      0      0   0   0
3. 0      0      0   0   0
4. 0      0      {?} 0   {3}
5. {1, 6} {2, 7} 0   0   0
6. 0      {2, 7} 0   0   0
7. 0      0      0   {5} 0
8. 0      0      0   0   {3, 8}
9. {1, 6} 0      0   0   0
```
