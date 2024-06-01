#### Priorytetowe algorytm karuzelowy

Algorytm wykonujemy jak priorytetowy do momentu, kiedy dwa procesy mają ten sam priorytet (albo różnica ich priorytetów jest mniejsza od ustalonej wartości). Wtedy takie procesy wykonujemy karuzelowo.

Dla danych z zadania 3:

P1 oraz P4 mają ten sam priorytet.
Weźmy Q = 1.

```
[P3--------] [P5-----] [P1-] [P4-] [P1-] [P4---] [P2-]
           8        13    14    15    16      19    20
```

#### Efektywność działania algorytmu karuzelowego

- $Q = \infty$: działa identycznie jak FCFS
- $Q > T$: jako, że T to średni czas, to istnieją dłuższe procesy niż T, więc algorytm w ich przypadku zadziała
- $S < Q < T$: złoty środek
- $Q = S$: tracimy połowę czasu na zmiany kontekstu
- $Q \approx 0$: będziemy mieli prawie same zmiany kontekstu zamiast wykonywania procesu
