#### Algorytm

```java
public class HBOLock implements Lock {
	private static final int LOCAL_MIN_DELAY = ...;
	private static final int LOCAL_MAX_DELAY = ...;
	private static final int REMOTE_MIN_DELAY = ...;
	private static final int REMOTE_MAX_DELAY = ...;
	private static final int FREE = -1;
	AtomicInteger state;

	public HBOLock() {
		state = new AtomicInteger(FREE);
	}

	public void lock() {
		int myCluster = ThreadID.getCluster();
		Backoff localBackoff = new Backoff(LOCAL_MIN_DELAY, LOCAL_MAX_DELAY);
		Backoff remoteBackoff = new Backoff(REMOTE_MIN_DELAY, REMOTE_MAX_DELAY);
		while (true) {
			if (state.compareAndSet(FREE, myCluster)) {
				return;
			}
			int lockState = state.get();
			if (lockState == myCluster) {
				localBackoff.backoff();
			} else {
				remoteBackoff.backoff();
			}
		}
	}
	public void unlock() {
		state.set(FREE);
	}
}
```

#### Motywacja

Główną motywacją stojącą za zamkami hierarchicznymi jest architektura NUMA (Non-Uniform Memory Access), w której procesory są zgrupowane w węzły (klastry) posiadające własną, szybką pamięć podręczną i lokalną.

W zamkach takich jak zwykły TASLock czy BackoffLock wszystkie wątki rywalizują o zamek na równych zasadach. Powoduje to dwa problemy:

- Wysoki koszt komunikacji: Gdy zamek jest przekazywany między wątkami z różnych węzłów, linia pamięci podręcznej zawierająca zamek musi migrować przez wolniejszą magistralę międzywęzłową (interconnect). Generuje to duży ruch i opóźnienia.

- Utrata lokalności danych: Wątek, który pozyskał zamek, zazwyczaj operuje na danych chronionych tym zamkiem. Jeśli zamek często "skacze" między węzłami, dane te również muszą migrować, co drastycznie obniża wydajność.

#### Zamki hierarchiczne

Chcemy, aby zamek pozostawał w obrębie jednego węzła tak długo, jak to możliwe, zanim zostanie przekazany do innego węzła. Zwiększa to przepustowość kosztem sprawiedliwości.
​
#### Intuicja HBOLock

Zamek HBOLock realizuje tę strategię poprzez zróżnicowanie czasu wycofania (backoff) w zależności od tego, czy wątek rywalizuje z sąsiadem z tego samego węzła, czy z wątkiem zdalnym.

Zamiast przechowywać jedynie informację "zajęty/wolny", zamek przechowuje identyfikator węzła (Cluster ID), do którego należy wątek będący obecnym właścicielem.

Gdy wątek próbuje zdobyć zamek i zauważa, że jest on zajęty przez wątek z tego samego węzła, stosuje standardowy, krótki czas wycofania (mały backoff). Działa agresywnie, zakładając, że zamek powinien pozostać w klastrze.

Gdy wątek widzi, że zamek jest zajęty przez wątek z innego węzła, stosuje znacznie dłuższy czas wycofania (duży backoff). Wycofuje się, dając szansę wątkom lokalnym (sąsiadom obecnego właściciela) na przejęcie zamka.

#### Skutek działania

Dzięki temu mechanizmowi, gdy zamek trafi do konkretnego węzła, "krąży" on między lokalnymi wątkami, ponieważ mają one krótsze czasy oczekiwania i szybciej ponawiają próby jego zdobycia. Dopiero gdy lokalny popyt wygaśnie (lub losowo uda się wątkowi zdalnemu wstrzelić w okno czasowe), zamek migruje do innego klastra. Minimalizuje to kosztowny ruch na magistrali systemowej
