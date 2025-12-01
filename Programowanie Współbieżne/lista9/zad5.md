#### Algorytm

```java
class CLHLock implements Lock {
    AtomicReference<QNode> tail;
    ThreadLocal<QNode> myNode = new QNode();

    public void lock() {
        QNode pred = tail.getAndSet(myNode);
        while (pred.locked) {}
    }

    public void unlock() {
        myNode.locked.set(false);
        myNode = pred;
    }
}
```


#### Intuicja

Każdy wątek posiada własny węzeł i wskaźnik na węzeł swojego poprzednika.

Globalny wskaźnik Tail wskazuje na ostatni wątek w kolejce.

Wątek dodaje swój węzeł na koniec kolejki, atomowo podmieniając Tail. Następnie obserwuje (spinuje na) zmiennej locked w węźle poprzednika.

Wątek czeka, aż poprzednik zwolni zamek (ustawi locked = false).

#### Zalety

Wątki spinują na lokalnych zmiennych różnych węzłów, co redukuje ruch w cache procesora (mniej nietrafień pamięci podręcznej) w porównaniu do zwykłych zamków typu TAS/TTAS.

#### Ograniczenie alokacji węzłów

Aby uniknąć ciągłego tworzenia nowych obiektów węzłów przy każdym wywołaniu `lock()`, stosuje się mechanizm recyklingu.

Wątek wchodząc do sekcji krytycznej "trzyma" w ręku wskaźnik na węzeł, na którym spinował (węzeł poprzednika).

Węzeł ten jest już zwolniony i niepotrzebny nikomu innemu.

Przy wychodzeniu z `unlock()`, wątek zamiast wyrzucać ten stary węzeł poprzednika, przejmuje go na własność.

Przy następnym wywołaniu `lock()`, wątek używa tego przejętego węzła jako swojego "nowego" węzła.

Każdy wątek alokuje węzeł tylko raz w całym swoim cyklu życia. Następnie dynamicznie wymienia się węzłami z poprzednikami, eliminując narzut alokacji pamięci.