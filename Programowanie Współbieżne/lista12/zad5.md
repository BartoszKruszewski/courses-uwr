#### Algorytm

```java
public class DualStack<T> {
    private class Slot {
        boolean full = false;
        volatile T value = null;
    }

    Slot[] stack;
    int capacity;
    private AtomicInteger top = new AtomicInteger(0); // indeks tablicy

    public DualStack(int myCapacity) {
        capacity = myCapacity;
        stack = (Slot[]) new Object[capacity];
        for (int i = 0; i < capacity; i++) {
            stack[i] = new Slot();
        }
    }

    public void push(T value) throws FullException {
        while (true) {
            int i = top.getAndIncrement();
            if (i > capacity - 1) { // czy stos pełny?
                throw new FullException();
            } else if (i > 0) { // indeks w zakresie, slot zarezerwowany
                stack[i].value = value;
                stack[i].full = true;  // włożenie zakończone
                return;
            }
        }
    }

    public T pop() throws EmptyException {
        while (true) {
            int i = top.getAndDecrement();
            if (i < 0) { // czy stos pusty?
                throw new EmptyException();
            } else if (i < capacity - 1) {
                while (!stack[i].full) {};
                T value = stack[i].value;
                stack[i].full = false;
                return value; // zdjęcie zakończone
            }
        }
    }
}
```

#### Intuicja

Klasa `DualStack<T>` dzieli metody `push()` i `pop()` na dwa kroki: reservation i fulfillment.

Dla `push()`:
- reservation polega na wywołaniu `getAndIncrement()` i sprawdzeniu czy indeks mieści się w w przedziale `0 ... capacity - 1`. Jeśli tak nie jest to powtarza się, albo zgłasza wyjątek przepełnienia.
- fulfillment zapisuje wartość w `stack[i]` i ustawia flagę `full = true`.

Metoda `pop()` działa symetrycznie. Używa `getAndDecrement()` oraz czeka na flage.

#### Treść zadania

Co jest nie tak z tym algorytmem?

Czy problem jest wynika z natury równoległości, czy da się znaleźć sposób, by to poprawić?

#### Problem

Sytuacja, w której pop zarezerwował slot (zmniejszył licznik), ale jeszcze nie odczytał danych, a push natychmiast ten slot "odzyskał" (zwiększył licznik) i nadpisał:

Stan początkowy: top = 5, w stack[4] są dane, flaga full = true.

Pop: Wywołuje top.getAndDecrement().

- Zwraca 5 (lub 4 zależnie od konwencji), top zmienia się na 4.

- Wątek pop ma teraz prawo do odczytu ze slotu (powiedzmy indeksu i = 4).

- Wątek zostaje wywłaszczony przed odczytaniem wartości.

Push (wchodzi w tym momencie): Wywołuje top.getAndIncrement().

- Odczytuje 4, top zmienia się z powrotem na 5.

- Wątek push uznaje, że zarezerwował slot i = 4 na nową daną.

Konflikt:

- Wątek push nie sprawdza, czy slot jest wolny. Natychmiast wykonuje: stack[4].value = nowaWartosc.

- Wątek pop wznawia działanie. Czyta stack[4].value.

Błąd: pop zwraca nowa wartosc, zamiast starej wartości, która tam była.

Z punktu widzenia logiki stosu, stara wartość "wyparowała", a nowa została zwrócona w złej kolejności.

#### Rozwiązanie

Aby algorytm był poprawny, protokół musi być symetryczny:

Pop: Czeka, aż full == true (dane są gotowe), odczytuje, a potem ustawia full = false.

Push: Musi czekać, aż full == false (slot jest zwolniony przez pop), zapisuje, a potem ustawia full = true.

Bez pętli `while(stack[i].full) {}` w metodzie push, producent (push) działa szybciej niż konsument (pop) i zamazuje dane, które konsument zdążył zarezerwować, ale nie zdążył jeszcze wyjąć.