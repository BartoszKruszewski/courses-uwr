```java
public class MCSLock implements Lock {
    AtomicReference<QNode> tail;
    ThreadLocal<QNode> myNode;

    public MCSLock() {
        queue = new AtomicReference<QNode>(null);
        myNode = new ThreadLocal<QNode>() {
            protected QNode initialValue() {
                return new QNode();
            }
        };
    }

    class QNode {
        boolean locked = false;
        QNode next = null;
    }

    public void lock() {
        QNode qnode = myNode.get();
        QNode pred = tail.getAndSet(qnode);
        if (pred != null) {
            qnode.locked = true;
            pred.next = qnode;
            // wait until predecessor gives up the lock
            while (qnode.locked) {}
        }
    }

    public void unlock() {
        QNode qnode = myNode.get();
        if (qnode.next == null) {
            if (tail.compareAndSet(qnode, null)) return;
            // wait until predecessor fills in its next field
            while (qnode.next == null) {}
        }
        qnode.next.locked = false;
        qnode.next = null;
    }
}
```

#### Intuicja

Algorytm MCS opiera się na strukturze listy powiązanej, gdzie każdy wątek wiruje na własnej, lokalnej zmiennej, zamiast na wspólnej globalnej.

`lock()`:
Wątek umieszcza swój węzeł na końcu kolejki (zmienna tail). Jeśli kolejka nie była pusta (istnieje poprzednik), wątek:

Ustawia wskaźnik next swojego poprzednika tak, aby wskazywał na jego węzeł.

Rozpoczyna wirowanie (aktywne oczekiwanie) na własnej zmiennej, czekając, aż jej wartość zmieni się na false (co oznacza przekazanie zamka).

`unlock()`:
Wątek posiadający zamek sprawdza, czy ma następcę (czy wskaźnik next jest różny od null).

Brak następcy: Wątek próbuje (CAS) ustawić wskaźnik tail na null. Jeśli się to uda, oznacza to, że kolejka jest pusta i proces kończy się.

Konflikt: Jeśli CAS się nie uda (oznacza to, że inny wątek właśnie dołączył do kolejki, ale jeszcze nie zaktualizował wskaźnika next), wątek zwalniający czeka w pętli while, aż połączenie zostanie ustanowione.

Przekazanie: Gdy następca jest już podłączony, wątek zwalniający ustawia jego lokalną zmienną na false, tym samym przekazując mu zamek.

#### Przewaga MCS nad CLH w systemach NUMA

Wydajność MCS w systemach o architekturze NUMA (Non-Uniform Memory Access) wynika ze sposobu lokalizacji zmiennych, na których odbywa się oczekiwanie.

Problem w CLH: W zamku CLH wątek wiruje na zmiennej należącej do swojego poprzednika. W systemach NUMA bez wspólnej pamięci podręcznej (lub gdy jest ona nieefektywna), oznacza to ciągłe odwoływanie się do pamięci innego węzła procesorowego. Generuje to duży ruch na magistrali i znaczne opóźnienia.

Zaleta MCS: Wątki w algorytmie MCS wirują wyłącznie na własnych, lokalnych polach węzła. Dzięki temu odwołania do pamięci są lokalne dla danego procesora, co drastycznie redukuje ruch w sieci połączeń międzyprocesorowych i zwiększa wydajność, nawet przy braku współdzielonej pamięci podręcznej.
