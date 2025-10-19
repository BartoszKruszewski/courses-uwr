#### Algorytm

```java
public void lock () {
    flag[i] = true;
    label[i] = counter++;
    while (∃k flag[k] && (label[i], i) > (label[k], k));
}
public void unlock () {
    flag[i] = false;
}
```

#### Wzajemne wykluczenie

Jest spełnione, ponieważ nawet igorując counter i ustawiając wszystkim wątkom taką samą, wątki rozdzielane są względem indeksów.

#### Niezakleszczenie

Jest spełnione, ponieważ nawet igorując counter i ustawiając wszystkim wątkom taką samą, wątki rozdzielane są względem indeksów, więc zawsze istnieje wątek o najmniejszym indeksie.

#### Niezagłoszenie (niezachodzi)

`counter` to int więc może mu się skończyć zakres, a wtedy nowe wątki będą miały bardzo małe wartości. Więc wątek, który dostanie na przykład `Integer.maxValue` będzie wiecznie głodzony.
