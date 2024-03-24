**a) definicja**
Analiza przepływu danych to zbadanie jak dane zmieniają się podczas działania programu (pod kątem przypisania). Pozwala to na optymalizację kodu.

**b) fakt**
*<nr_instrukcji, {<zmienna, miejsce przypisania>, ...}>*

**c) fakty dla przykładu z zadania**
```
1. [x := 10]
    in: {(x, ?), (y: ?), (z: ?)}
    out: {(x, 1), (y: ?), (z: ?)}

2. [y := x + 10]
    in: {(x, 1), (y: ?), (z: ?)}
    out: {(x, 1), (y: 2), (z: ?)}

3. [z := y + x] 
    in: {(x, 1), (y: 2), (z: ?)}
    out: {(x, 1), (y: 2), (z: 3)}
```

**Optymalizacja kodu**
Wartość $x$ jest przypisywana tylko w 1. instrukcji i później się nie zmienia, więc możemy od razu wyliczyć $y$. 

Wartość $y$ też nie jest już później przypisywana ponownie, więc postępujemy tak samo dla $z$.

Optymalizuje to ilość operacji arytmetycznych.
```
[x := 10] [y := 20] [z := 30]
```