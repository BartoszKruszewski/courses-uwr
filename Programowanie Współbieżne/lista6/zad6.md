#### Algorytm

```java
public class RegMRSWRegister implements Register{
    RegBoolMRSWRegister[M] bit;

    public void write(int x) {
        this.bit[x].write(true);
        for (int i=x-1; i>=0; i--)
            this.bit[i].write(false);
    }
    public int read() {
        for (int i=0; i < M; i++)
            if (this.bit[i].read())
                return i;
    }
}
```

#### M‑wartościowość

Przy konstrukcji tego rejestru wartość `x` kodujemy jako `bit[x]=true`, zerując niższe bity.

Pozwala to zapisać tyle różnych wartości ile bitów `RegBoolMRSWRegister` ma rejestr (czyli `M`).

#### Lemat: `read()` zawsze zwraca wartość ustawioną przez pewne `write()`

Jeśli czytelnik odczytuje `bit[j]`, to istnieje `k >= j` z `bit[k] = true`, ustawione przez zapis.

Gdy czytelnik przechodzi z `j` do `j + 1`, oznacza to, że `bit[j] = false`, zatem `bit[k] = true` z `k > j`.

Zapis może wyzerować `bit[k]` tylko po ustawieniu wyższego `bit[l] = true`, gdzie `l > k`.

Zatem `read()` zawsze napotyka bit ustawiony przez `write()`.

#### Regularność

Niech `x` to wartość zapisana przez ostatnie zakończone `write()`.

Wtedy `bit[x] = true`, a dla `i < x`, `bit[i] = false`.

Jeśli `read()` zwraca inną wartość `j != x`, to `bit[j] = true` zostało ustawione w trakcie równoczesnego zapisu.

Odczyt zwraca wartość starą lub nową, czyli jest regularny.
