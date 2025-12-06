#### Algorytm

```java
public boolean add(T item) {
    int key = item.hashCode();
    
    while (true) {
        Node pred = head;
        Node curr = pred.next;
        
        while (curr.key < key) {
            pred = curr; 
            curr = curr.next;
        }
        
        pred.lock();
        try {
            curr.lock();
            try {
                if (validate(pred, curr)) {
                    if (curr.key == key) {
                        return false;
                    } else {
                        Node node = new Node(item);
                        node.next = curr;
                        pred.next = node;
                        return true;
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

public boolean remove(T item) {
    int key = item.hashCode();
    
    while (true) {
        Node pred = head;
        Node curr = pred.next;
        
        while (curr.key < key) {
            pred = curr; 
            curr = curr.next;
        }
        pred.lock();
        try {
            curr.lock();
            try {
                if (validate(pred, curr)) {
                    if (curr.key == key) {
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
    while (true) {
        Node pred = head;
        Node curr = pred.next;
        
        while (curr.key < key) {
            pred = curr; curr = curr.next;
        }
        
        pred.lock();
        try {
            curr.lock();
            try {
                if (validate(pred, curr)) {
                    return (curr.key == key);
                }
            } finally {
                curr.unlock();
            }
        } finally {
            pred.unlock();
        }
    }
}

private boolean validate(Node pred, Node curr) {
    Node node = head;
    while (node.key <= pred.key) {
        if (node == pred)
            return pred.next == curr;
        
        node = node.next;
    }
    
    return false;
}
```



#### Deadlock podczas `remove()`

- wątek A zatrzymuje się przed zajęciem zamków na $pred_A$ i $curr_A$
- wątek B dodaje węzeł `w` pomiędzy $pred_A$ i $curr_A$
- wątek A kontynuuje i metoda `validate` zwraca fałsz
- dowolny inny wątek usuwa węzeł `w`

i tak w kółko