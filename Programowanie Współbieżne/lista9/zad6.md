#### Algorytm

```java
public class BadCLHLock implements Lock {
    AtomicReference<Qnode> tail = new AtomicReference<QNode>(new QNode());

    ThreadLocal<Qnode> myNode = new ThreadLocal<QNode> {
        protected QNode initialValue() {
            return new QNode();
        }
    };

    public void lock() {
        Qnode qnode = myNode.get();
        qnode.locked = true; // I’m not done
        // Make me the new tail, and find my predecessor
        Qnode pred = tail.getAndSet(qnode);
        while (pred.locked) {}
    }

    public void unlock() {
        // reuse my node next time
        myNode.get().locked = false;
    }

    static class Qnode { // Queue node inner class
        volatile boolean locked = false;
    }
}
```

#### Dlaczego recykling własnego węzła jest błędem?

- Wątek A wywołuje unlock(), ustawia myNode.get().locked = false.

- Wątek A natychmiast ponownie wywołuje lock().

- Ponieważ myNode jest ThreadLocal i nie został podmieniony, wątek A pobiera ten sam obiekt N_A.

- Wątek A ustawia N_A.locked = true (w metodzie lock()), sygnalizując, że chce zająć zamek.

Skutki błędu

Jeśli wątek B nie zdążył zauważyć, że N_A.locked zmieniło się na false, a wątek A zdążył już nadpisać N_A.locked z powrotem na true to mamy:

- Zakleszczenie: Wątek B może utknąć w nieskończoność, myśląc, że wątek A nadal trzyma zamek, mimo że wątek A uważa, że dopiero co ustawił się w kolejce za kimś innym.

- Brak wzajemnego wykluczenia: Jeśli wątek B odczyta false, wejdzie do sekcji krytycznej, to wątek A nadal może wejść do kolejki
