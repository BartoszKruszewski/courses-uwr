#### Metoda `add()`

```java
public boolean add(T item) {
	int key = item.hashCode();

	while (true) {
		Window window = find(head, key);
		Node pred = window.pred, curr = window.curr;

		if (curr.key == key) {
			return false;
		} else {
			Node node = new Node(item);
			node.next = new AtomicMarkableReference(curr, false); 

			if (pred.next.compareAndSet(curr, node, false, false)) {
				return true;
			}
		}
	}
}
```

#### Czy przy drugim nieudanym `CAS` przeglądanie listy od początku jest konieczne?

Nie musimy sprawdzać całej listy, ponieważ element pred nadal istnieje (jego wskaźnik mark nie został zmieniony).

W związku z tym wystarczy przejrzeć część listy, zaczynając od pred aż do końca. Lista jest posortowana, a więc wcześniej ustaliliśmy, że `pred.key < key`, natomiast `curr.key >= key`.
