#### Algorytm LockFreeQueue

```java
public void enq(T value) 
{
    Node node = new Node(value);
    while (true) 
    {
        Node last = tail.get();
        Node next = last.next.get(); 
        if (last == tail.get()) 
        {
            if (next == null) 
            {
                if (last.next.compareAndSet(next, node)) 
                {
                    tail.compareAndSet(last,node);
                    return; 
                }

            } 
            else 
            {
                tail.compareAndSet(last, next);
            } 
        }
    }
}

public T deq() throws EmptyException 
{ 
    while (true) 
    {
        Node first = head.get();
        Node last = tail.get();
        Node next = first.next.get(); 
        if (first == head.get()) 
        {
            if (first == last) 
            { 
                if (next == null) 
                {
                    throw new EmptyException(); 
                }
                tail.compareAndSet(last, next); 
            } 
            else 
            {
                T value = next.value;
                if (head.compareAndSet(first, next))
                    return value;
            }
        }
    }
}
```

#### Odczytanie wartości z węzła jako punkt linearyzacji `deq()` odnoszącego sukces



Dla `deq()` odnoszącego sukces zwracamy wartość.

```java
T value = next.value;
if (head.compareAndSet(first, next))
    return value; 
```

Jeżeli zwróciliśmy wartość to wcześniej CAS musiał również mieć sukces.
Więc `deq()` odnosi sukces wtw CAS odnosi sukces.

Stąd może być to punkt linearyzacji.

#### Aktualizacja pola tail jako punkt linearyzacji `enq()` odnoszącego sukces (być może wykonywane przez inny wątek)

`enq()` jet dwuetapowe, najpierw (logicznie) przepinany wskaźnik `last.next`, a następnie (fizycznie) aktualizujemy `tail`.

Nawet jeśli wstawienie fizyczne się nie uda, ale wstawimy element logicznie to wszystkie przyszłe operacje najpierw naprawią listę a dopiero potem wykonają swoją operację.

Więc zanim zostaną wykonane inne zmiany `tail` zostanie zaktualizowany (przez dowolony wątek).

Stąd aktualizacja pola `tail` może być punktem linearyzacji.
