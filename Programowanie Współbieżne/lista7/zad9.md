#### Konstrukcja 

```java
public T decide(T value) {
    values[id] = value;
    Q.enq(id);
    return values[Q.peek()]
}
```

#### Poprawność

Nie ma czekania, więc "wait-free".

Zawsze zostanie zwrócona wartość proponowana przez jakiś wątek, ponieważ `enq()` występuje przed `peek()`.

Dla każdego wątku wartość ta będzie taka sama, ponieważ nie używamy nigdzie `deq()`.

W tym problemie konsensusu może być dowolna liczbą wątków, więc poziom konsensusu tej kolejki to $\infty$
