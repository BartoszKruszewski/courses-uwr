#### Algorytm

```java
public void lock() {
    for (int i = 1; i < n; i++) { // attempt to enter level i
        level[me] = i;
        victim[i] = me;
        while (( ∃ k != me) (level[k] >= i && victim[i] == me)) {};
    }
}

public void unlock() {
    level[me] = 0;
}
```

#### Niezagłodzenie

Indukcja (z najwyzszego poziomu do najniższego)

*Krok bazowy*:

Wątek z poziomu $n - 2$ ostatecznie przejdzie do poziomu $n - 1$.

*Dowód*:

Rozważmy przypadki:

1. Poziom $n - 1$ jest pusty, wtedy wątek po prostu tam wchodzi
2. Jest jakiś wątek na poziomie $n - 1$, wiemy z zad 4. jest tam co najwyżej 1 wątek. Jeżeli opuści on sekcje krytyczną to zanim ponownie by do niej wszedł stanie się on ofiarą na poziomie $n - 2$, odlokowując oczekujący wątek, wtedy oczekujący wątek wejdzie na poziom $n - 1$.

*Krok indukcyjny*:

Załóżmy indukcyjnie, że wątek z poziomu $x$ ostatecznie przejdzie do poziomu $n - 1$.

Udowodnimy, że wątek z poziomu $x - 1$ również ostatecznie przejdzie do poziomu $n - 1$.

Wątek z poziomu $x - 1$ wejdzie na poziom $x$ jeżeli wyższe poziomy będą wolne, albo przestanie być ofiarą.

Wątek, który był z sekcji krytycznej, żeby wejść do niej ponownie musi przejść przez poziom $x - 1$, czyli on zostanie ofiarą, odlokowując oczekujący wątek, wtedy oczekujący wątek wejdzie na poziom $x$.

Z założenia indukcyjnego wiemy, że wątek z poziomu $x$ ostatecznie wejdzie do poziomu $n - 1$.

Więc wątek z poziomu $x - 1$ również ostatecznie przejdzie do poziomu $n - 1$.

## Niezakleszczenie z niezagłodzenia

1. Niezagłodzenie: **każdy** wątek w końcu dostanie zamek
2. Niezakleszczenie: **przynajmniej jeden** wątek w końcu dostanie zamek
3. Jeśli każdy, to na pewno przynajmniej jeden
