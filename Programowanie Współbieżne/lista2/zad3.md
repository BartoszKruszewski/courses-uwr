#### Algorytm

```java
public void lock() {
    int i = ThreadID.get(); /*returns 0 or 1*/
    int j = 1 - i;
    flag[i] = true;
    local[i] = (turn[j] + i) % 2;
    turn[i] = local[i];
    while (flag[j] == true && local[i] == ((turn[j] + i) % 2));
}
public void unlock() {
    int i = ThreadID.get();
    flag[i] = false;
}
```

#### Wzajemne wykluczenie

Dowód niewprost:

Założmy, że oba wątki weszły do sekcji krytycznej czyli spełniły `while`.

Jedyne możliwości wyjścia z pętli to złamanie `local[i] == ((turn[j] + i) % 2)`.

Czyli zaszło jednocześnie:

`local[0] != ((turn[1] + 0) % 2) = turn[1]`

`local[1] != ((turn[0] + 1) % 2) = 1 - turn[0]`

Załóżmy bez straty ogólności, że wątek 0 pierwszy ustawił turn[0].

Wiemy, że `turn[0]` oraz `local[0]` został ustawiony na `(turn[1] + 0) % 2 = turn[1] = x`.

A następnie `turn[1]` oraz `local[1]` został ustawiony na `(turn[0] + 1) % 2 = 1 - turn[0] = 1 - x`.

Sprawdzamy:

`local[0] = x != turn[1] = 1 - x`

`local[1] = 1 - x != 1 - turn[0] = 1 - x`

`1 - x != 1 - x`, wiec mamy sprzeczność.

Dla pozostałych przypadków symetrycznie.

#### Niezagłodzenie (nie zachodzi)

Jeżeli jakiś wątek jest głodzony (bez straty ogólności niech to będzie wątek 0).

To znaczy że czeka na `while` w locku.

Czyli zachodzi `flag[1] == true` oraz `local[0] == ((turn[1] + 0) % 2) = turn[1]`.

Dodatkowo drugi wątek wychodząc z sekcji krytycznej ponownie do niej wszedł.

Czyli zaszło `flag[0] != true` albo `local[1] != ((turn[0] + 1) % 2)`.

`flag[0] != true`, nie zaszło bo głodzony wątek mógł ustawić `flag[0] = true` zanim wszedl do `while`.

Więc musiało zajść `local[1] != ((turn[0] + 1) % 2) = 1 - turn[0]`.

Wątek 1 ponownie musiał wykonać `local[1] = (turn[0] + 1) % 2` oraz `turn[1] = local[1]`.

Więc `local[1] = turn[0]` oraz `turn[1] = local[1] = turn[0]`.

Wiemy, że `local[0] = turn[1] = turn[0] = local[1]`

Co spełnia `local[1] != ((turn[0] + 1) % 2) = 1 - turn[0]`

Czyli taka sytuaja jest możliwa.

#### Niezakleszczenie

Dowód bardzo podobny do dowodu wzajemnego wykluczenia

Założmy, że wystąpiło zakleszczenie, czyli oba wątki spełniają `while`.

Czyli zaszło jednocześnie:

`local[0] == ((turn[1] + 0) % 2) = turn[1]`

`local[1] == ((turn[0] + 1) % 2) = 1 - turn[0]`

Załóżmy bez straty ogólności, że wątek 0 pierwszy ustawił turn[0].

Wiemy, że `turn[0]` oraz `local[0]` został ustawiony na `(turn[1] + 0) % 2 = turn[1] = x`.

A następnie `turn[1]` oraz `local[1]` został ustawiony na `(turn[0] + 1) % 2 = 1 - turn[0] = 1 - x`.

Sprawdzamy:

`local[0] = x == turn[1] = 1 - x`

`local[1] = 1 - x == 1 - turn[0] = 1 - x`

`x != 1 - x`, wiec mamy sprzeczność.

Dla pozostałych przypadków symetrycznie.