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

#### Intuicja

Algorytm działa jak seria **poczekalni**. Każdy wątek musi przejść przez $(n-1)$ poziomów, żeby dostać się do sekcji krytycznej. Na każdym poziomie co najmniej jeden wątek zostaje zablokowany, jeśli kilka wątków próbuje przejść dalej.

Dzięki temu na każdym poziomie **co najmniej 1 wątek zostaje odfiltrowany** (stąd nazwa "Filter").

#### Lemat

Na poziomie $n - i$ znajduje się jednocześnie co najwyżej $i$ wątków.

#### Dowód indukcyjny

*Przypadek bazowy*:

Na poziomie $n-1$ jest co najwyżej 1 wątek.

*Dowód (nie wprost)*:

Załóżmy, że 2 wątki $A$ i $B$ są na poziomie $n - 1$.

Oba wyszły z pętli `while`, więc warunek pętli jest dla nich fałszywy.

Ale **ostatni**, który ustawił `victim[n-1]` (np. wątek $A$) widzi drugi wątek $B$ na poziomie $n-1$.

Czyli zachodzi `level[B] >= n-1 && victim[n-1] == A`, co jest sprzeczne z tym, że wyszedł z pętli

*Krok indukcyjny*:

Załóżmy, że na poziomie $n-j$ jest co najwyżej $j$ wątków.

Udowodnimy, że na poziomie $n-(j+1)$ jest co najwyżej $j+1$ wątków.

*Dowód (nie wprost):*

Załóżmy, że $j+2$ wątki przeszły poziom $n-(j+1)$ .

Wszystkie te $j+2$ wątki wyszły z pętli `while` dla poziomu $n-(j+1)$

Rozważmy **ostatni** wątek $V$, który ustawił `victim[n-(j+1)] = V`.

Mamy $j+2$ wątki, które przeszły poziom $n-(j+1)$.

Z założenia indukcyjnego maksymalnie $j$ z nich może być na poziomie $n-j$ lub wyżej.

Więc co najmniej $(j+2) - j = 2$ wątki muszą zostać na poziomie $n-(j+1)$ lub między poziomami.

Czyli warunek `(∃k != V) (level[k] >= n-(j+1) && victim[n-(j+1)] == V)` jest **prawdziwy**

Co jest sprzeczne z tym, że V wyszedł z pętli.

#### Wzajemne wykluczanie

Wątek wchodzi w sekcję krytyczną, gdy znajduje się na $(n-1)$-szym poziomie. Z lematu wiemy, że jest to co najwyżej 1 wątek.


