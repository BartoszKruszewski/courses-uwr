#### Algorytm

```java
class FastPath implements Lock {
    private Lock lock;
    private int x, y = -1;

    public void lock() {
        int i = ThreadID.get();
        x = i; // I’m here
        while (y != -1) {} // is the lock free?
        y = i; // me again?
        if (x != i) // Am I still here?
        lock.lock(); // slow path
    }
    public void unlock() {
        y = -1;
        lock.unlock();
    }
}
```


#### Wzajemne wykluczenie

`write_A(x = 0) => read_A(y == -1)`

`write_B(x = 1) => read_B(y == -1)`

Oba wątki przeszły `while`

`write_A(y = 0)`

`write_B(y = 1)`

Aktualny stan to `x = 1, y = 1`

`read_A(x != 0) => CS_A`

`read_B(x == 1) => lock.lock() => CS_B`

Czyli oba wątki weszły naraz do sekcji krytycznej

Czyli wzajemne wykluczenie nie występuje

#### Niezagłodzenia

`write_B(x = 1) => read_B(y == -1)`

`write_B(y = 1)`

`write_A(x = 0) => read_B(y != -1)`

wątek A czeka w `while`

wątek B wchodzi do sekcji krytycznej.

Robi w niej coś. Używa unlock(), wtedy stan zmiennych to `x = 0, y = -1`

Więc może ponowić całą sekwencje i tak w kółko.

Zatem dochodzi do zagłodzenia wątku A.

#### Niezakleszczenie

Załóżmy nie wprost, że doszło do zakleszczenia.

Zakleszczenie mogło wystąpić tylko jeżeli oba wątki są w while, więc dla obu `y != -1`

Stan `y != -1` można zmienić tylko za pętlą while, co jest sprzeczne z tym, że oba są w pętli
