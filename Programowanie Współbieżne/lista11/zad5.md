#### Algorytm

```java
class Window {
	public Node pred, curr;
	Window(Node myPred, Node myCurr) {
		pred = myPred; curr = myCurr;
	}
}
	
public Window find(Node head, int key) {
	Node pred = null, curr = null, succ = null;
	boolean[] marked = {false};
	boolean snip;
	retry: while (true) {
		pred = head;
		curr = pred.next.getReference();
		while (true) {
			succ = curr.next.get(marked);
			while (marked[0]) {
				snip = pred.next.compareAndSet(curr, succ, false, false);
				if (!snip) continue retry;
				curr = succ;
				succ = curr.next.get(marked);
			}
			
			
			if (curr.key >= key)
				return new Window(pred, curr);
			pred = curr;
			curr = succ;
		}
	}
}

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

public boolean remove(T item) {
	int key = item.hashCode();
	boolean snip;
	while (true) {
		Window window = find(head, key);
		Node pred = window.pred, curr = window.curr;
		if (curr.key != key) {
			return false;
		} else {
			Node succ = curr.next.getReference();
			snip = curr.next.attemptMark(succ, true);
			if (!snip)
				continue;
			pred.next.compareAndSet(curr, succ, false, false);
			return true;
		}
	}
}

public boolean contains(T item) {
	boolean[] marked = false{};
	int key = item.hashCode();
	Node curr = head;
	while (curr.key < key) {
		curr = curr.next;
		Node succ = curr.next.get(marked);
	}
    return (curr.key == key && !marked[0]) 
}
```

#### `add(T item)`

**Udane**

Moment wstawienia węzła `pred.next.compareAndSet(curr, node, false, false)`

**Nieudane**

Odczyt `curr.key == key` po udanej walidacji okna w `find()` (oznacza obecność)

​
#### `remove(T item)`

**Udane**

`curr.next.attemptMark(succ, true)` – moment logical removal (mark=true)

**Nieudane**

odczyt `curr.key != key` po udanej walidacji okna w `find()`

#### `contains(T item)`

**Udane**

odczyt `!marked[0]` dla `curr.key == key`

**Nieudane**

odczyt węzła z `curr.key > key` lub marked z `curr.key == key` w pętli `while(curr.key < key)`
