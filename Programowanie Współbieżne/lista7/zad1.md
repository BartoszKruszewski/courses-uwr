#### Konstrukcja

```java
public class SimpleSnapshot<T> implements Snapshot<T> {
    private StampedValue<T>[] a_table;
    
    public SimpleSnapshot(int capacity, T init) {
        a_table = (StampedValue<T>[]) new StampedValue[capacity];
        for (int i = 0; i < capacity; i++) {
            a_table[i] = new StampedValue<T>(init);
        }
    }
    
    public void update(T value) {
        int me = ThreadID.get();
        StampedValue<T> oldValue = a_table[me];
        StampedValue<T> newValue = new StampedValue<T>((oldValue.stamp) + 1, value);
        a_table[me] = newValue;
    }
    
    private StampedValue<T>[] collect() {
        StampedValue<T>[] copy = (StampedValue<T>[]) new StampedValue[a_table.length];
        
        for (int j = 0; j < a_table.length; j++)
            copy[j] = a_table[j];
        
        return copy;
    }
    
    public T[] scan() {
        StampedValue<T>[] oldCopy, newCopy;
        oldCopy = collect();
        
        collect: while (true) {
            newCopy = collect();
            if (! Arrays.equals(oldCopy, newCopy)) {
                oldCopy = newCopy;
                continue collect;
            }
            
            T[] result = (T[]) new Object[a_table.length];
            for (int j = 0; j < a_table.length; j++)
                result[j] = newCopy[j].value;
            
            return result;
        }
    }
}
```

#### Migawka jest poprawna (linearizowalna)

Każdy `update(i, v)` jest liniaryzowany w chwili atomowego zapisu pary `(stamp, value)` do rejestru procesu $i$.

`scan` wykonuje dwie kolejne kolekcje $C_1$ i $C_2$.

Jeśli uzyskane wektory są identyczne, to dla każdego indeksu $j$ między odczytem `a_table[j]` w $C_1$ i odczytem w $C_2$ nie wystąpił żaden `update` (w przeciwnym razie zmieniłby się `stamp`).

Z tego wynika, że dla każdego $j$ istnieje przedział czasu, w którym wartość rejestru jest stała i obejmuje oba odczyty, a przekrój wszystkich tych przedziałów jest niepusty.

Więc istnieje chwila w trakcie `scan`, w której wszystkie rejestry mają dokładnie zwracane wartości, co stanowi punkt liniaryzacji migawki.

#### Scan jest obstruction‑free

Metoda `scan` powtarza `collect()`, dopóki dwie kolejne kopie tablicy znaczników i wartości się różnią, więc przy nieustannych `update` może w teorii wykonywać nieskończoną liczbę iteracji.

Jeśli jednak od pewnego momentu `scan` działa samotnie (pozostałe wątki przestają wykonywać `update`), to stan tablicy stabilizuje się i po skończonej liczbie prób dwie kolejne kolekcje będą identyczne.

Co dokładnie odpowiada własności obstruction‑free.

#### Migawka spełnia warunek lock‑free

`update` jest wait‑free, a `scan` czeka tylko podczas kolizji z `update`, więc zawsze migawka robi "postęp", czyli jest lock-free.
