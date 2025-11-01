#### Algorytm

```java
public class HWQueue<T> {
    AtomicReference<T>[] items;
    AtomicInteger tail;
    static final int CAPACITY = Integer.MAX_VALUE;

    public HWQueue() {
        items = (AtomicReference<T>[]) Array.newInstance(AtomicReference.class, CAPACITY);
        for (int i = 0; i < items.length; i++) {
            items[i] = new AtomicReference<T>(null);
        }
        tail = new AtomicInteger(0);
    }
    public void enq(T x) {
        int i = tail.getAndIncrement(); // oznaczamy jako OP1
        items[i].set(x); // oznaczamy jako OP2
    }
    public T deq() {
        while (true) {
            int range = tail.get();
            for (int i = 0; i < range; i++) {
                T value = items[i].getAndSet(null);
                if (value != null) {
                    return value;
                }
            }
        }
    }
}
```

#### Intuicja

`enq()` najpierw rezerwuje indeks przez `tail.getAndIncrement()`, a następnie zapisuje element przez `items[i].set(x)`.

`deq()` skanuje od `0` do `tail.get()-1` i zwraca pierwszy nienullowy wpis poprzez `getAndSet(null)`.

#### Pierwsza operacja: `int i = tail.getAndIncrement()`

```
         OP1             OP2
A: -- [        enq(x)        ] ->
B: -- [ enq(y) ] -- [ deq(x) ] ->
      OP1    OP2
```

Spodziewamy się, że `deq()` zwróci `x`.

Jednak w momencie wykonania `deq()` w kolejce nie ma `x`, ale jest `y` i on zostanie zwrócony.

#### Druga operacja: `items[i].set(x)`

```
         OP1    OP2
A: -- [        enq(x)        ] ->
B: -- [ enq(y) ] -- [ deq(x) ] ->
      OP1    OP2
```

Spodziewamy się, że `deq()` zwróci `y`

Jednak miejsce, do którego przypiszemy `x` zostało wybrane wcześniej niż miejsce, do którego przypiszemy `y`, więc `deq()` zwróci `x`.

#### Czy z tego wynika, że `enq()` nie jest linearyzowalna?

Nie. Punkt linearyzacji występuje, gdy `getAndSet()` zwróci nienullową wartość. Obiekt jako całość pozostaje linearyzowalny mimo braku lokalnego punktu w `enq()`.
