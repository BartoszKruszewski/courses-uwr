#### Algorytm

```java
public class SynchronousQueue<T> {
    T item = null;
    boolean enqueuing;
    Lock lock;
    Condition condition;
    ...

    public void enq(T value) {
        lock.lock();
        try {
            while (enqueuing)
                condition.await();
            enqueuing = true;
            item = value;
            condition.signalAll();
            while (item != null)
                condition.await();
            enqueuing = false;
            condition.signalAll();
        } finally {
            lock.unlock();
        }
    }

    public T deq() {
        lock.lock();
        try {
            while (item == null)
                condition.await();
            T t = item;
            item = null;
            condition.signalAll();
            return t;
        } finally {
            lock.unlock();
        }
    }
}
```

#### Synchroniczne stuktury danych

Synchroniczna struktura danych to taka, w której operacje producenta i konsumenta (np. enq/deq albo push/pop) muszą wystąpić jednocześnie i zostają ze sobą sparowane.

#### Spotkanie

Spotkanie to moment, gdy `enq()` i `deq()` działają w tym samym czasie, a producent bezpośrednio przekazuje swój element konsumentowi.

#### Synchronizacja w SynchronousQueue

W SynchronousQueue spotkanie zachodzi dzięki synchronizacji za pomocą Lock i Condition.

**Producent (`enq()`)**

1. Ustawia `enqueuing = true` i `item = value`
2. `signalAll()` budzi czekającego konsumenta
3. Czekanie w pętli `while (item != null)`, blokując się aż deq nie zabierze elementu

**Konsument (`deq()`)**

1. Czekanie na `item != null`
2. Pobiera wartości `(T t = item; item = null)`
3. `signalAll()` budzi enq. To zwalnia producenta.

Przekazanie następuje w pamięci współdzielonej przez pole item.

Obie metody działają pod `lock.lock()`, więc ich wykonanie się przeplata.
