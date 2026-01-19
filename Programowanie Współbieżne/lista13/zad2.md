#### Algorytm

```java
public class EliminationBackoffStack<T> extends LockFreeStack<T> {
    static final int capacity = ...;
    EliminationArray<T> eliminationArray = new EliminationArray<T>(capacity);
    static ThreadLocal<RangePolicy> policy = new ThreadLocal<RangePolicy>() {
        return new RangePolicy();
    }
    
    public void push(T value) {
        RangePolicy rangePolicy = policy.get();
        Node node = new Node(value);
        while (true) {
            if (tryPush(node)) {
                return;
            } else try {
                T otherValue = eliminationArray.visit(value, rangePolicy.getRange());
                if (otherValue == null) {
                    rangePolicy.recordEliminationSuccess();
                    return; // exchanged with pop
                }
            } catch (TimeoutException ex) {
                rangePolicy.recordEliminationTimeout();
            }
        }
    }
    
    public T pop() throws EmptyException {
        RangePolicy rangePolicy = policy.get();
        while (true) {
            Node returnNode = tryPop();
            if (returnNode != null) {
                return returnNode.value;
            } else try {
                T otherValue = eliminationArray.visit(null, rangePolicy.getRange());
                if (otherValue != null) {
                    rangePolicy.recordEliminationSuccess();
                    return otherValue;
                }
            } catch (TimeoutException ex) {
                rangePolicy.recordEliminationTimeout();
            }
        }
    }
}
```

#### Działanie `EliminationBackoffStack`

Jest to rozszerzenie `LockFreeStack` o mechanizm aktywnego czekania zamiast biernego. Gdy `tryPush()` lub `tryPop()` na głównym stosie nie powiodą się z powodu rywalizacji o zasoby, wątek nie przechodzi w stan uśpienia. Zamiast tego kieruje się do `EliminationArray`, czyli pomocniczej tablicy obiektów typu `LockFreeExchanger`. Tam wątek losuje slot w obrębie wyznaczonego zakresu i próbuje wymienić się wartością z wątkiem wykonującym przeciwstawną operację, co pozwala im obu zakończyć działanie bez dotykania głównego licznika stosu.​

#### Rola `RangePolicy`

Klasa `RangePolicy` pełni rolę regulatora obciążenia. Odpowiada za dynamiczne dostosowywanie wielkości fragmentu tablicy (zakresu), z którego losują wątki.​

Przy niskiej rywalizacji (mało wątków) klasa zawęża zakres, by „zagęścić” ruch i zwiększyć szansę, że para wątków trafi na ten sam slot.​

Przy wysokiej kontencji (dużo wątków) klasa poszerza zakres, aby rozładować tłok i uniknąć sytuacji, w której wątki zbyt często trafiają na zajęte sloty (stan BUSY).​

#### Punkty linearyzacji

Moment, w którym operacja staje się widoczna dla systemu, zależy od ścieżki wykonania:

Ścieżka standardowa (przez stos):
Punktem linearyzacji dla obu metod (push i pop) jest udana instrukcja atomowa CAS na wskaźniku wierzchołka stosu (top), która fizycznie dodaje lub usuwa węzeł.​

Ścieżka eliminacji (przez EliminationArray):
Punktem linearyzacji dla pary wymieniających się wątków jest moment udanego połączenia w parę. Następuje to, gdy drugi z przybyłych wątków wykonuje udany CAS na wybranym slocie, zmieniając jego stan z WAITING na BUSY. To jedno zdarzenie linearyzuje jednocześnie operację wstawiania i zdejmowania elementu.​
