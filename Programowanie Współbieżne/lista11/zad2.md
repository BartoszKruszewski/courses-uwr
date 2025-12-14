#### `find()`

`find()` przeszukuje posortowaną listę, zwracając parę kolejnych węzłów (Window z pred i curr), gdzie pred.next powinno wskazywać na curr, a oba węzły są nieoznaczone (nieusunięte).

Algorytm iteracyjnie przechodzi od głowy listy, fizycznie usuwając oznaczone węzły poprzez CAS na pred.next, aż znajdzie parę pred-curr z `curr.key >= key` i `pred.next == curr` oraz brak oznaczeń.

Jedno wywołanie `compareAndSet()` występuje w pętli: `pred.next.compareAndSet(curr, next, false, false)`.

*To zawiedzie, gdy inny wątek zmieni pred.next między odczytem a próbą zapisu, np. inny wątek fizycznie usunął curr lub dodał węzeł między pred a curr.*

#### `add()`

`add(T item)` najpierw wywołuje `find(key)` uzyskując pred i curr, potem sprawdza czy `curr.key == key` (już istnieje).

Jeśli nie, tworzy nowy węzeł z `node.next = AtomicMarkableReference(curr, false)` i próbuje `pred.next.compareAndSet(curr, node, false, false)`.

*Może zawieść gdy: (1) inny wątek zmienił pred.next (np. usunął/usunął fizycznie między pred-curr), (2) pred zostało oznaczone jako usunięte przez inny wątek. Sukces oznacza atomowe wstawienie nowego węzła w posortowanym miejscu.*
​
#### `remove()`

`remove(T item)` używa find(key) do pred i curr. Jeśli `curr.key == key`, najpierw `snip = curr.next.attemptMark(succ, true)` (logiczne usunięcie), a potem `pred.next.compareAndSet(curr, succ, false, false)` (fizyczne unlink).

*Pierwsze CAS `(attemptMark, wewnętrznie CAS na curr.next z succ->null na succ->marked)` zawiedzie gdy: (1) curr.next ≠ succ (zmienione przez inny wątek), (2) już oznaczone. Drugie CAS zawiedzie gdy: (1) pred.next ≠ curr (już unlinked przez inny), (2) pred.marked.*

​
#### Metoda `contains()`

`contains(T item)` wywołuje find(key) i sprawdza `curr.key == key && !curr.marked`. Brak własnych CAS – polega na świeżości okna z `find()`. Zwraca true tylko jeśli znaleziono nieoznaczony węzeł o pasującym kluczu.

​
#### Drugie CAS w `remove()`

Rezultat drugiego `compareAndSet()` w `remove()` nie jest sprawdzany – zawsze zwraca true niezależnie od sukcesu.

To dlatego, że logiczne usunięcie (snip==true) zapewnia, że curr jest oznaczone i nie będzie użyte przez inne operacje. Fizyczne unlink jest tylko optymalizacją (czyszczenie listy), nie wpływa na poprawność semantyczną zbioru – wielokrotne próby unlink są bezpieczne, a brak nie powoduje błędów logicznych (oznaczony węzeł jest ignorowany). Można je usunąć bez utraty poprawności, zachowując lock-free'owość (gwarantowaną przez pierwsze CAS) i linearizowalność (punkt liniaryzacji to attemptMark), choć lista może rosnąć z "śmieciami"