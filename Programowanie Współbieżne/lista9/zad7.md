#### Problem

W klasycznym CLH wątki tworzą kolejkę, gdzie każdy wątek obserwuje (spinuje na) węźle swojego poprzednika.

Jeśli jednak wątek zrezygnuje z czekania (timeout), powstaje "dziura" w kolejce, którą inni muszą ominąć.

#### Algorytm

```java
public class TOLock implements Lock{
    static QNode AVAILABLE = new QNode();
    AtomicReference<QNode> tail;
    ThreadLocal<QNode> myNode;

    public TOLock() {
        tail = new AtomicReference<QNode>(null);
        myNode = new ThreadLocal<QNode>() {
            protected QNode initialValue() {
                return new QNode();
            }
        };
    }

    static class QNode {
        public volatile QNode pred = null;
    }

    public boolean tryLock(long time, TimeUnit unit) throws InterruptedException {
        long startTime = System.currentTimeMillis();
        long patience = TimeUnit.MILLISECONDS.convert(time, unit);

    	QNode qnode = new QNode();
    	myNode.set(qnode);
    	qnode.pred = null;
    
    	QNode myPred = tail.getAndSet(qnode);

    	if (myPred == null || myPred.pred == AVAILABLE) {
            return true;
        }

        while (System.currentTimeMillis() - startTime < patience) {
            QNode predPred = myPred.pred;
            if (predPred == AVAILABLE) {
        	    return true;
            } else if (predPred != null) {
        	    myPred = predPred;
            }
        }

        if (!tail.compareAndSet(qnode, myPred)) {
            qnode.pred = myPred;
            return false;
        }

    }

    public void unlock() {
    	QNode qnode = myNode.get();
    	if (!tail.compareAndSet(qnode, null))
    	    qnode.pred = AVAILABLE;
    }
}
```

#### `AVAILABLE`

Jeśli pole pred jakiegoś węzła wskazuje na `AVAILABLE`, oznacza to, że wątek, który był właścicielem tego węzła, zwolnił już zamek.

#### `tryLock()`

Wątek tworzy swój węzeł i ustawia go na końcu kolejki, używając tail.getAndSet(qnode).

Wchodzi do kolejki i pyta wątek przed nim `myPred` czy może wejść.

Jeśli przed nim nikogo nie ma (pusta kolejka) lub wątek przed nim zwolnił miejsce `myPred.pred == AVAILABLE`, wchodzi od razu.

#### Oczekiwanie z Timeoutem

Wątek wchodzi w pętlę while, sprawdzając czas.

Normalne czekanie: Wątek patrzy na `myPred`. Jeśli poprzednik zwolni zamek (ustawi swoje pred na AVAILABLE), wątek wchodzi.

Obsługa "Dziur": Wątek patrzy na pole pred swojego poprzednika `predPred`.

- Jeśli poprzednik zrezygnował (zrobił timeout), jego węzeł zostaje w kolejce, ale staje się martwy.

- Wtedy wątek przeskakuje tego martwego poprzednika i zaczyna obserwować osobę, która stała przed nim `myPred = predPred`.

Intuicja: Jeśli osoba przed Tobą w kolejce znudziła się i poszła do domu, nie czekasz na nią. Pytasz, kto stał przed nią, i zaczynasz obserwować tę osobę.

#### Rezygnacja (Timeout) – "Wychodzę z kolejki"

Jeśli czas minie `System.currentTimeMillis() - startTime >= patience`, wątek próbuje wycofać się z kolejki.

- Optymistyczne wyjście: Jeśli wątek jest ostatni w kolejce (tail wskazuje na niego), próbuje po prostu usunąć się z ogona (compareAndSet).

- Pozostawienie śladu: Jeśli nie jest ostatni, wątek nie może po prostu zniknąć, bo przerwałby łańcuch. Zamiast tego oznacza swój węzeł w taki sposób, aby następca wiedział, że ma go przeskoczyć, czyli `qnode.pred = myPred`.Następca zauważy to w swojej pętli (jako `predPred != null` ale nie `AVAILABLE`) i przeskoczy ten węzeł.
