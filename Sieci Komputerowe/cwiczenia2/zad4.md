$M(x) = a_0 + a_1 x + \dots + a_n x^n \in \mathbb{F}_2[x]$

$x + 1 \mid M(x) \;\Leftrightarrow\; M(1) = 0 \;\Leftrightarrow\; \sum_{i=0}^{n} a_i \equiv 0 \pmod{2}$

Więc $x + 1 \mid M(x)$ wtedy i tylko wtedy, gdy suma współczynników jest parzysta

Stąd sprawdzanie sprawdzanie parzystości liczby zapalonych bitów w wiadomości jest równoważne z dzieleniem przez $x + 1$

Dla $G(x) = x + 1 \Rightarrow r = 1$, więc dopisujemy tylko jeden bit jak w przypadku metody bitu parzystości.

Podsumowując:
- dopisywanie bitu jest identyczne w przypadku obu metod, ponieważ dopisany bit oznacza parzystość zapalonych bitów.
- weryfikacja przekłamań jest identyczna, ponieważ w obu przypadkach działania sprowadzają się do sprawdzenia parzystości otrzymanych bitów
