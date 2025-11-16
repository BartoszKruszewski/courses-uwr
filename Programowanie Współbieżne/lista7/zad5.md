Przy trzech procesach zawsze znajdzie się konfiguracja, w której dwa z nich (powiedzmy $A$ i $B$) wykonują `dequeue` na **tej samej** kolejce, a trzeci $C$ jeszcze nic nie widział.

- Jeśli najpierw `dequeue` zrobi $A$, a potem $B$, to $A$ dostaje pierwszy element, $B$ drugi.
- Jeśli najpierw `dequeue` zrobi $B$, a potem $A$, to $B$ dostaje pierwszy element, $A$ drugi.

Po obu tych dwóch krokach **stan kolejki jest identyczny** (usunęliśmy dwa elementy).

Proces $C$ W obu wariantach widzi tę samą zawartość wszystkich kolejek.

W jednym porządku dalsze przebiegi muszą kończyć się decyzją 0, a w drugim – 1.

$C$ nie widzi różnicy, więc nie może jednocześnie doprowadzić do 0 i 1.

Stąd sprzeczność.
