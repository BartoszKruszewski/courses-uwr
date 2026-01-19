#### Algorytm

```java
public class LockFreeExchanger<T> {
    static final int EMPTY = ..., WAITING = ..., BUSY = ...;
	AtomicStampedReference<T> slot = new AtomicStampedReference<T>(null, 0);

	public T exchange(T myItem, long timeout, TimeUnit unit)
        throws TimeoutException {
		long nanos = unit.toNanos(timeout);
		long timeBound = System.nanoTime() + nanos;
		int[] stampHolder = {EMPTY};
		while (true) {
			if (System.nanoTime() > timeBound)
				throw new TimeoutException();
			T yrItem = slot.get(stampHolder);
			int stamp = stampHolder[0];
			switch (stamp) {
				case EMPTY:
					if (slot.compareAndSet(yrItem, myItem, EMPTY, WAITING)) {
						while (System.nanoTime() < timeBound) {
							yrItem = slot.get(stampHolder);
							if (stampHolder[0] == BUSY) {
								slot.set(null, EMPTY);
								return yrItem;
							}
						}
						if (slot.compareAndSet(myItem, null, WAITING, EMPTY)) {
							throw new TimeoutException();
						} else {
							yrItem = slot.get(stampHolder);
							slot.set(null, EMPTY);
							return yrItem;
						}
					}
					break;
				case WAITING:
					if (slot.compareAndSet(yrItem, myItem, WAITING, BUSY))
						return yrItem;
					break;
				case BUSY:
					break;
				default: // impossible
					...
			}
		}
	}
}
```

#### Metoda `exchange()`

Metoda opiera się na `AtomicStampedReference` i trzech stanach: `EMPTY`, `WAITING`, `BUSY`.

Wątek A (inicjujący): Zmienia stan z `EMPTY` na `WAITING` i udostępnia swój przedmiot. Czeka w pętli.

Wątek B (parujący): Znajduje `WAITING`, zabiera przedmiot A i wstawia swój, zmieniając stan na `BUSY`. To sygnał dla A, że wymiana się udała.

#### Porażki `compareAndSet()`

1. Porażka przy ofercie (EMPTY → WAITING): Inny wątek zajął slot ułamek sekundy wcześniej.

    *Akcja: Ponowna próba w pętli.*

2. Porażka przy parowaniu (WAITING → BUSY): Wątek oczekujący zrezygnował (timeout) lub inny wątek „ukradł” parę.

    *Akcja: Ponowna próba w pętli.*

3. Porażka przy timeoutcie (WAITING → EMPTY): Wątek chciał zrezygnować, ale w ostatniej chwili ktoś dokonał wymiany (zmienił na BUSY).

    *Akcja: Zamiast błędu timeout, wątek finalizuje sukces – odbiera przedmiot partnera.*

#### Dlaczego `set()` zamiast `compareAndSet()`?

Używa się `set()` tylko wtedy, gdy wątek ma pewność wyłączności.
​
Gdy slot jest w stanie `BUSY`, inne wątki nie próbują go modyfikować (tylko odczytują). Skoro nie ma ryzyka wyścigu (race condition), kosztowny atomowy `CAS` jest zbędny – wystarczy tańszy `set()`, który czyści slot do stanu EMPTY po zakończeniu wymiany.