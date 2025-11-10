#### Algorytm Petersona

```java
public void lock() {
    flag[i] = true;
    victim = i;
    while (flag[j] && victim == i) {};
}
public void unlock() {
    flag[i] = false;
}
```

#### Rejestr regularny

Rejestr regularny gwarantuje jedynie, że odczytana wartośc będzie aktualna albo zapisana poprzednio.

#### Wzajemne wykluczenie

Nie zachodzi, ponieważ oba wątki sprawdzając warunek w `while` mogą odczytać poprzednią wartość `flag` czyli `false`, więc oba wejdą  do sekcji krytycznej

#### Niezagłodzenie

Zachodzi, ponieważ zmienna victim jest dalej atomowa, osłabieniu ulegają jedynie sprawdzenia `flag`, stąd wątki jeszcze częściej będą wchodzic do sekcji krytycznej.
