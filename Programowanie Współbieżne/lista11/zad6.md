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

#### Ujemny size

`size` początkowo jest równy $0$

Wątek A wykonuje `enque()`:
- ...
- `tail.next = e`
- *idzie spać*

Wątek B wykonuje `deque()`:
- ...
- `while (head.next == null)` nie zatrzyma się
- `size.getAndDecrement()`

wtedy `size` jest równy $-1$
