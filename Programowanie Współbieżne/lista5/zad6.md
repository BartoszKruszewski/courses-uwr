#### Algorytm

```java
class IQueue<T> {
    AtomicInteger head = new AtomicInteger(0);
    AtomicInteger tail = new AtomicInteger(0);
    T[] items = (T[]) new Object[Integer.MAX_VALUE];

    public void enq(T x) {
        int slot;
        do {
            slot = tail.get();
        } while (!tail.compareAndSet(slot, slot+1));
        items[slot] = x;
    }
    public T deq() throws EmptyException {
        T value;
        int slot;
        do {
            slot = head.get();
            value = items[slot];
            if (value == null) throw new EmptyException();
        } while (!head.compareAndSet(slot, slot+1));
        return value;
    }
}
```

#### Dowodzenie niepoprawności

Żeby udowodnić niepoprawność, wystarczy pokazać nielinearność.

Sprowadza się to do znalezienia kontrprzykładu z nielinearną historią.

#### Intuicja

`enq` rezerwuje indeks w `tail` atomowo, ale zapisuje element do items[slot] już nieatomowo.

W tym oknie `deq` może odczytać `null` i zgłosić `EmptyException` mimo, że wcześniej zaszło `enq`

Nie daje się wtedy to ułożyć w poprawną historię sekwencyjną FIFO zachowującą porządek wywołań między wątkami.

#### Kontrprzykład

```  
A: -- [        Enq(x)        ] -->
B: -- [ Enq(y) ] -- [ Deq() ] -->
```

G:

```
A Enq(x)  // tail.compareAndSet(slot, slot+1)
B Enq(y)
B void
B Deq()
B EmptyException
A void    // items[slot] = x
```

S:
```
...
B q.enq(y)
B q: void
...
B q.deq()
B q: throws EmptyException
...
```

Jeżeli historia miałaby być linearyzowalna to powinno dać się wstawić w miejsce `...`:

```
A Enq(x)
A void
```

Tak, żeby kolejka zachowywała swoje właściwości.

Natomiast niezależnie od miejsca wstawienia punktów linearyzacji ciągle mamy zgłaszany wyjątek spowodowany nieatomowym zachowaniem `enq`.
