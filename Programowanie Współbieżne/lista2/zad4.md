#### Algorytm

```java
class Foo implements Lock {
    private int turn;
    private boolean busy = false;
    public void lock() {
        int me = ThreadID.get(); /*get id of my thread*/
        do {
            do {
                turn = me;
            } while (busy);
            busy = true;
        } while (turn != me);
    }
    public void unlock() {
        busy = false;
    }
}
```

#### Wzajemne wykluczenie

Jakiś wątek po wyjściu z pętli wewnętrznej pierwszy ustawi busy na true, i wtedy każdy inny z niej nie wyjdzie.

Jedynie wątki które mogłyby wyjść w tym samym czasie z pętli wewnętrznej mogłyby potencjalnie razem wejść do sekcji krytycznej.

Natomiast poza pętlą wewnętrzną nie mogą ustawić turn na siebie, a turn może mieć tylko jedną wartośc, więc wejdzie co najwyżej jeden.

#### Zagłodzenie

1. unlock
1. busy == false
1. wątek 0 wykonuje turn = 0
1. busy = true
1. watek nie wchodzi do petli bo turn = 0
1. wchodzi do sekcji krytycznej

#### Zakleszczenie

1. busy == false
1. wątek 0 wykonuje turn = 0
1. busy = true
1. wątek k ustawia turn = k
1. wątek k utknie w pętli wewnętrznej, ponieważ busy jest true.
1. wątek 0, widzi turn != 0
1. wątek 0 ponownie wchodzi do pętli wewnętrznej i się zapętla

Nikt nie wejdzie do sekcji krytycznej, więc też nikt nie wyjdzie i nie ustawi busy na false
