### Dowód górnego ograniczenia

Załóżmy, że istnieje protokół konsensusu dla $m > n$ wątków używający n-ograniczonej funkcji `compareAndSet()`.

W stanie krytycznym maksymalnie $n$ wątków mogło już wykonać operację `compareAndSet()` na rejestrze, ponieważ funkcja działa poprawnie tylko dla pierwszych $n$ wywołań.

Ponieważ $m > n$, istnieje co najmniej jeden wątek, który jeszcze nie wywołał `compareAndSet()`.

Jeśli ten wątek spróbuje wywołać `compareAndSet()`, otrzyma wartość stan wadliwy, co uniemożliwia mu podjęcie prawidłowej decyzji zgodnej z właściwościami konsensusu.

### Dowód dolnego ograniczenia (konstrukcja)

```java
public Object decide(Object value) {
    propose(value);
    int i = ThreadID.get();
    if (r.compareAndSet(FIRST, i))
        return proposed[i];
    else
        return proposed[r.get()];
}
```

Każdy z $n$ wątków:

1. Ogłasza swoją propozycję w publicznej tablicy `proposed[]`
2. Próbuje atomowo ustawić rejestr wspólny za pomocą `compareAndSet()`
3. Wątek, którego `compareAndSet()` zostanie zlinearyzowany jako pierwszy, ustawi swój identyfikator jako zwycięzcę
4. Pozostałe wątki odczytują identyfikator zwycięzcy i zwracają jego propozycję

Ponieważ mamy dokładnie $n$ wątków i $n$ dozwolonych wywołań `compareAndSet()`, wszystkie wątki mogą wykonać operację bez otrzymania stanu wadliwego, co gwarantuje poprawność protokołu konsensusu.
