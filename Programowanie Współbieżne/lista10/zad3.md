#### Algorytm

```java
public boolean contains(T item) {
    int key = item.hashCode();
    head.lock();
    Node pred = head;
    try {
        Node curr = pred.next;
        curr.lock();
        try {
            while (curr.key < key) {
                pred.unlock();
                pred = curr;
                curr = curr.next;
                curr.lock();
            }
            if (key == curr.key) {
                return true;
            } else {
                return false;
            }
        } finally {
            curr.unlock();
        }
    } finally {
        pred.unlock();
    }
}
```

#### Intuicja

Zastosowanie techniki blokowania "krok po kroku" (zajmowanie zamków na parze węzłów) zapewnia wyłączność dostępu do lokalnego fragmentu listy, co fizycznie uniemożliwia innym wątkom wstawienie nowego elementu pomiędzy węzeł poprzedni a bieżący w trakcie naszej iteracji.

Opierając się na niezmiennikach struktury FineList:

- brak duplikatów
- ściśle rosnące uporządkowanie kluczy

Możemy mieć pewność, że nie przegapiliśmy poszukiwanej wartości wcześniej. W rezultacie, napotkanie pierwszego węzła, który nie spełnia warunku bycia mniejszym od szukanego klucza `curr.key >= key` jest momentem rozstrzygającym.
