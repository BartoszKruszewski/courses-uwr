#### Implementacja z książki

```java
public class Balancer {
    Boolean toggle = true;

    public synchronized int traverse(t) {
        try {
            if (toggle) {
                return 0;
            } else {
                return 1;
            }
        } 
        finally {
            toggle = !toggle;
        }
    }
}
```

Podana implementacja używa `synchornized`, więc nie jest **wait-free**

#### Efektywna implementacja **wait-free**

```java
public class Balancer {
    private AtomicInteger counter;

    public int traverse() {
        return counter.getAndIncrement() % 2;
    }
}
```
