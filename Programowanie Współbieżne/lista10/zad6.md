#### Algorytm

```java
public boolean remove(T item) {
    int key = item.hashCode();
    while (true) {
        Node pred = head;
        Node curr = head.next;
        while (curr.key < key) {
            pred = curr; curr = curr.next;
        }
        pred.lock();
        try {
            curr.lock();
            try {
                if (validate(pred, curr)) {
                    if (curr.key == key) {
                        curr.marked = true;
                        pred.next = curr.next;
                        return true;
                    } else {
                        return false;
                    }
                }
            } finally {
                curr.unlock();
            }
        } finally {
            pred.unlock();
        }
    }
}

public boolean contains(T item) {
	int key = item.hashCode();
	Node curr = head;
	while (curr.key < key)
		curr = curr.next;
	if (curr.key == key && !curr.marked){
		return true;
	} else {
		return false;
	}
	
}
private boolean validate(Node pred, Node curr) {
	if (!pred.marked && !curr.marked && pred.next == curr){
		return true;
	} else {
		return false;
	}
}
```

#### Intuicja

W strukturze LazyList usuwanie dzieli się na etap logiczny (ustawienie flagi marked) i fizyczny (przepięcie wskaźników), co pozwala na realizację metody contains bez blokad.

#### Redukcja do jednego zamka

Próba zredukowania metody `remove()` do jednego zamka przy zachowaniu fizycznego usuwania prowadzi do niespójności:

**Blokowanie tylko usuwanego węzła (curr):**

Nie daje wyłączności na modyfikację poprzednika.

Przy usuwaniu sąsiadów ($a \rightarrow b$), wyścig wątków może doprowadzić do błędnego przepięcia wskaźników, pozostawiając węzeł $b$ w liście mimo usunięcia $a$.

**Blokowanie tylko poprzednika (pred):**

Nie chroni przed zmianami w samym węźle usuwanym.

Przy równoległym usuwaniu $a$ i $b$, jeden wątek może „wyciąć” $b$, a drugi nieświadomie przywrócić go do listy, nadpisując wskaźnik next węzła poprzedzającego.
