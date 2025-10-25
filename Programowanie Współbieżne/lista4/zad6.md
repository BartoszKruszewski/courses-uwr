#### Algorytm

```java
public void lock() {
    for (int i = 1; i < n; i++) { // attempt to enter level i
        level[me] = i;
        victim[i] = me;
        while (( ∃ k != me) (level[k] >= i && victim[i] == me)) {};
    }
}

public void unlock() {
    level[me] = 0;
}
```

#### Sekcja doorway

```
level[me] = i;
victim[i] = me;
```

#### Kontrprzykład

Na poziomie 1 mamy A, B i C.

A jest ofiarą.

Wtedy wątki B oraz C przechodzą kolejne poziomy wchodzą do sekcji krytycznej i wracają na poziom 1.

Normalnie A mógłby wejśc na poziom wyżej ponieważ zwolniły się, natomiast był za wolny.

Wtedy ofiarą staje się B, natomiast C przechodzi dalej.

Znowu wchodzi i wychodzi z sekcji krytycznej i wraca na poziom 1.

A dalej jeszcze czeka, natomiast B wchodzi poziom wyżej bo wszystkie wyzsze poziomy są wolne.

Może to się powtarzać w nieskończonośc.

#### r-ograniczenie a niezagłodzenie

Wątki B i C mogą w nieskończoność wyprzedzać A, ale jest to zależne od szybkości wybudzenia A.

Sam nie głodzi wątku A, ponieważ gdyby się wybudził to po jakimś czasie dostanie się do sekcji krytycznej.

Natomiast nie ma gwarancji, że inne wątki będą czekać, żeby nie wyprzedzać A jak ten śpi.
