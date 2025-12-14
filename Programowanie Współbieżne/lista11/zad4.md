#### `add()` i `remove()` sa **lock-free**

Metody pozostają w pętli while(true) wyłącznie wtedy, gdy lista ulega modyfikacji.

Ponieważ mimo zapętlenia zawartość listy faktycznie się zmienia, oznacza to, że przynajmniej jeden z wątków wykonuje postęp.

Z tego względu obie metody spełniają definicję algorytmów **lock-free**.

#### `contains()` jest **wait-free**

Metoda przechodzi po elementach listy do momentu, gdy natrafi na wartość większą od poszukiwanej.

Ponieważ lista ma skończoną długość, gwarantuje to zakończenie działania w skończonym czasie, a więc metoda jest **wait-free**.
