```java
public boolean add(T item) {
  int key = item.hashCode();
  while (true) {
    value = Counter.get(); // dodajemy counter
    Node pred = head;
    Node curr = pred.next;
    while (curr.key < key) {
      pred = curr; curr = curr.next;
    }
    pred.lock();
    try {
      curr.lock();
      try {
        // if (validate(pred, curr))
        if (value == Counter.get()) { // zamiana validate na sprawdzenie countera
          if (curr.key == key) {
            return false;
          } else {
            Node node = new Node(item);
            Counter.increment(); // zwiekszenie licznika
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
    value = Counter.get(); // dodajemy licznik
    Node pred = head;
    Node curr = pred.next;
    while (curr.key < key) {
      pred = curr; curr = curr.next;
    }
    pred.lock();
    try {
      curr.lock();
      try {
        // if (validate(pred, curr)) 
        if (value == Counter.get()) { // zamiana validate na sprawdzenie countera
          if (curr.key == key) {
            Counter.increment(); // zwiekszenie licznika
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


```