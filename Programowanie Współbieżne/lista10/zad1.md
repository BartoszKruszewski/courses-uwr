#### Algorytm

```java
public class CoarseList<T> {
    private Node head;
    private Lock lock = new ReentrantLock();

    public CoarseList() {
        head = new Node(Integer.MIN_VALUE);
        head.next = new Node(Integer.MAX_VALUE);
    }

    public boolean add(T item) {
        Node pred, curr;
        int key = item.hashCode();
        lock.lock();
        try {
            pred = head;
            curr = pred.next;
            while (curr.key < key) {
                pred = curr;
                curr = curr.next;
            }
            if (key == curr.key) {
                return false;
            } else {
                Node node = new Node(item);
                node.next = curr;
                pred.next = node;
                return true;
            }
        } finally {
            lock.unlock();
        }
    }

    public boolean remove(T item) {
        Node pred, curr;
        int key = item.hashCode();
        lock.lock();
        try {
            pred = head;
            curr = pred.next;
            while (curr.key < key) {
                pred = curr;
                curr = curr.next;
            }
            if (key == curr.key) {
                pred.next = curr.next;
                return true;
            } else {
                return false;
            }
        } finally {
            lock.unlock();
        }
    }
}
```

#### Niezmiennik reprezentacji

Warunki, które fizyczna lista musi zawsze spełniać.

Dla `CoarseList`:

- lista jest posortowana
- brak cykli
- obecność wartowników head/tail

#### Mapa abstrakcji

Funkcja tłumacząca fizyczną listę na abstrakcyjny zbiór matematyczny.

Dla `CoarseList` (z polecenia, błędne):

*zbiór zawiera te liczby, które znajdują się w węzłach, do których można dojść wskaźnikami od `head`.*

#### Punkty linearyzacji dla standardowej mapy

Aby mapa "element w zbiorze $\iff$ osiągalny z head" była poprawna, metody muszą być linearyzowane w momencie **fizycznej zmiany w pamięci**:

- `add(x):` moment przepięcia wskaźnika (`pred.next = node`).
- `remove(x):` moment przepięcia wskaźnika omijającego węzeł (`pred.next = curr.next`).
- `contains(x):` moment odczytania węzła.

#### Problem z linearyzacją na zamku

Jeśli punktem linearyzacji jest **zajęcie zamka**, to abstrakcyjnie element "już jest" w zbiorze w momencie blokady.

Jednak fizycznie wątek dopiero zaczyna pracę i nie dodał jeszcze węzła do listy.

Standardowa mapa abstrakcji ("tylko to, co osiągalne") nie widzi tego elementu, więc zachodzi sprzeczność między modelem a rzeczywistością.

#### Poprawiona mapa abstrakcji

Dla linearyzacji na zamku mapa musi uwzględniać stan zamka:

$$
S = \{ \text{element osiągalny z head} \} \cup \{ \text{element dodawany przez właściciela zamka} \} \setminus \{ \text{element usuwany przez właściciela zamka} \}
$$

Dzięki temu, w chwili zajęcia zamka, operacja jest widoczna w abstrakcyjnym zbiorze, zanim fizycznie zmieni się lista.
