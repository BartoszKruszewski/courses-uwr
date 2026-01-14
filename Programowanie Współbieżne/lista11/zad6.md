#### Algorytm

```java
public class BoundedQueue <T> {
    ReentrantLock enqLock, deqLock;
    Condition notEmptyCondition, notFullCondition;
    AtomicInteger size;
    volatile Node head, tail;
    final int capacity;
    public BoundedQueue(int _capacity) {
        capacity = _capacity;
        head = new Node(null);
        tail = head;
        size = new AtomicInteger(0);
        enqLock = new ReentrantLock();
        notFullCondition = enqLock.newCondition();
        deqLock = new ReentrantLock();
        notEmptyCondition = deqLock.newCondition();
    }

    
    public void enq(T x) {
        boolean mustWakeDequeuers = false;
        Node e = new Node(x);
        enqLock.lock();
        try {
            while (size.get() == capacity)
                notFullCondition.await();
            tail.next = e;
            tail = e;
            if (size.getAndIncrement() == 0)
                mustWakeDequeuers = true;
        } finally {
            enqLock.unlock();
        }
        if (mustWakeDequeuers) {
            deqLock.lock();
            try {
                notEmptyCondition.signalAll();
            } finally {
                deqLock.unlock();
            }
        }
    }
    public T deq() {
        T result;
        boolean mustWakeEnqueuers = false;
        deqLock.lock();
        try {
            while (head.next == null)
                notEmptyCondition.await();
            result = head.next.value;
            head = head.next;
            if (size.getAndDecrement() == capacity) {
                mustWakeEnqueuers = true;
            }
        } finally {
            deqLock.unlock();
        }
        if (mustWakeEnqueuers) {
            enqLock.lock();
            try {
                notFullCondition.signalAll();
            } finally {
                enqLock.unlock();
            }
        }
        return result;
    }
}
```

#### Jak działa BoundedQueue?

BoundedQueue to współbieżna kolejka o ograniczonym rozmiarze, w której elementy są wstawiane na koniec (`enq()`) i zdejmowane z początku (`deq()`). Kluczową cechą tej implementacji jest użycie dwóch osobnych zamków: `enqLock` dla operacji wstawiania i `deqLock` dla operacji zdejmowania, co pozwala na jednoczesne wykonywanie obu typów operacji i zwiększa współbieżność.
​
#### Zmienne warunkowe

**`notEmptyCondition`**

Wstrzymuje wykonanie `deq()`, gdy kolejka jest pusta `(head.next == null)`. Wątek wywołujący `deq()` czeka na tej zmiennej `await()` do momentu, gdy `enq()` doda element do kolejki i wyśle sygnał `signalAll()`, informując że można wznowić pobieranie.
​
**`notFullCondition`**

Wstrzymuje wykonanie `enq()`, gdy kolejka osiągnęła maksymalny rozmiar `(size == capacity)`. Wątek wywołujący `enq()` czeka na tej zmiennej `await()` do momentu, gdy `deq()` zdejmie element z kolejki i wyśle sygnał `signalAll()`, informując że można wznowić wstawianie.
​
#### Czy **size** może stać się ujemny?

Zmienne warunkowe `notEmptyCondition` i `notFullCondition` gwarantują, że `deq()`nigdy nie wykona się na pustej kolejce, a `enq()` nigdy nie wykona się na pełnej.
​
Kluczowe właściwości zapewniające poprawność:

- `enq()` tylko zwiększa size: Operacja `size.getAndIncrement()` wykonuje się dopiero po dodaniu elementu do listy

- `deq()` tylko zmniejsza size: `Operacja size.getAndDecrement()` wykonuje się tylko po sprawdzeniu `head.next != null`

Monotoniczne działanie: Jeśli wątek otrzyma "zielone światło" do wykonania deq() (kolejka nie jest pusta), to współbieżne operacje `enq()` tylko dodają elementy, więc nie może stracić tego uprawnienia
​
AtomicInteger zapewnia atomowość operacji inkrementacji i dekrementacji.

Dzięki tej synchronizacji size zawsze pozostaje w przedziale $[0, capacity]$.
