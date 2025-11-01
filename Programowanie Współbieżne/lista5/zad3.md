#### Algorytm

```java
public class WaitFreeQueue {
    int head = 0, tail = 0;
    items = (T[]) new Object[capacity];

    public void enq(Item x) {
        if (tail - head == capacity) throw new FullException();
        items[tail % capacity] = x;
        tail++;
    }
    public Item deq() {
        if (tail == head) throw new EmptyException();
        Item item = items[head % capacity];
        head++;
        return item;
    }
}
```

#### Punkty linearyzacji

Punktami linearyzacji są operacje `tail++` oraz `head++`.

Dzieje się tak, ponieważ mamy sprawdzenia `if (tail - head == capacity)` oraz `if (tail == head)`, które zależą tylko od wartości `tail` oraz `head`. 

Dzięki temu, że dostępy do pamięci są atomowe, to wartość `tail` oraz `head` są zawsze poprawnie odczytywane przez oba wątki, a ify rzucające wyjątki skutecznie blokują zapis zajętych rejestrów samej kolejki.

Ostatecznie gwarantuje nam to, że odpowiadające sobie `enq` i `deq` będą wykonywane w poprawnej kolejności, czyli zachodzi linearyzacja.

#### Prawie pusta kolejka `(tail == head + 1)`

Rozważmy przypadki:
- konsument wykona test pustki przed `tail++`, czyli będzie `(tail == head)` i rzuci wyjątek (linearyzacja: zablokowanie deq przed enq)
- konsument wykona test po `tail++` i odczyta właśnie dostarczony element (linearyzacja: enq przed deq).

W obu przypadkach nie ma błędnego odczytu, bo element staje się widoczny dopiero po `tail++`.

#### Prawie pełna kolejka `tail - head == capacity - 1`

Rozważmy przypadki:
- producent wykona test pełności przed `head++`, czyli będzie `tail - head == capacity ` i rzuci wyjątek
- producent wykona test pełności po `head++`, czyli zapisze element element na ostatnim wolnym miejscu

W obu przypadkach nie ma nadpisywania elemetów z kolejki, bo nadpisanie staje się możliwe dopiero po zwiększeniu `head`, czyli zachodzi linearyzacja.

#### Sekwencyjna spójność

Jeżeli zachodzi linearyzacja to tym bardziej zachodzi sekwencyjna spójność, ponieważ linearyzacja jest silniejszym założeniem.
