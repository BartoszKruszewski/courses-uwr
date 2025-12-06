#### Algorytm

```java
public boolean add(T item) {
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
			if (curr.key == key) {
				return false;
			}
			Node node = new Node(item);
			node.next = curr;
			pred.next = node;
			return true;
		}
		finally {
			curr.unlock();
		}
	}
	finally {
		pred.unlock();
	}
}

public boolean remove(T item) {
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
			if (curr.key == key) {
				pred.next = curr.next;
				return true;
			}
			return false;
		}
		finally {
			curr.unlock();
		}
	}
	finally {
		pred.unlock();
	}
}
```


#### Intuicja

W przeciwieństwie do rozwiązań blokujących całą strukturę jednym zamkiem, klasa FineList implementuje synchronizację drobnoziarnistą,przypisując osobny zamek do każdego węzła.

Wątki poruszają się po liście techniką „ręka za ręką” (hand-over-hand locking). Oznacza to, że wątek zawsze trzyma blokady na dwóch sąsiednich węzłach jednocześnie: zwalnia blokadę poprzednika dopiero po pomyślnym zablokowaniu węzła bieżącego. Dzięki temu wiele wątków może bezpiecznie operować na rozłącznych fragmentach listy w tym samym czasie, co zwiększa przepustowość systemu.

#### Linearyzowalność `add()`

**Sukces:**

Moment modyfikacji wskaźnika w węźle poprzedzającym (pred.next), tak aby wskazywał na nowo utworzony węzeł. To wtedy element staje się osiągalny.

**Porażka (duplikat):**

Moment uzyskania blokady na istniejącym już w liście węźle (curr), który posiada taki sam klucz jak element dodawany.

#### Linearyzowalność `remove()`

**Sukces:**

Chwila, w której wskaźnik węzła poprzedzającego (pred.next) zostaje przepięty na następnika węzła usuwanego, fizycznie odcinając usuwany element od reszty listy.

**Porażka (brak elementu):**

Moment zablokowania węzła (curr), którego klucz jest większy od poszukiwanej wartości, co dowodzi, że elementu nie ma w posortowanej liście.
