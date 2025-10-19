```java
public void lock() {
    do {
        flag[i] = true;
        for (int j = 0; j < i; j++) {
            if (flag[j] == true) {
                flag[i] = false;
                while (flag[j] == true) {}
                break;
            }
        }
    } while (flag[i] == false);
    for (int j = i+1; j < n; j++) {
        while (flag[j] == true) {}
    }
}
public void unlock() {
    flag[i] = false;
}
```

### Wzajemne wykluczenie

Załóżmy nie wprost, że wątki A i B weszły do sekcji krytycznej.

Bez straty ogólności niech A będzie pierwszy.

Rozważmy przypadki:

1. A < B:

    Wątek B, wszedł do CS, więc musiał w pierwszej pętli zobaczyć, że `flag[A] == false`.
    
    Możliwe jest to tylko wtedy gdyby wątek A ustawiłby swoja flage pozniej.
    
    Natomiast wtedy wątek A czekałby w drugiej pętli, ponieważ `flag[B] == true`.
    
    Sprzeczność

2. A > B:

    Wątek B, wszedł do CS, więc musiał w drugiej pętli zobaczyć, że `flag[A] == false`.

    Więc sprawdził ją zanim A ustawił ją. 
    
    Wątek A też wszdeł do CS, więc moment wejścia B kiedy `flag[A] == false` odbył się przed `while (flag[j] == true) {}`,

    więc wątek A dalej tam czeka aż B wyjdzie z CS

    sprzeczność

#### Niezakleszczenie

Z pierwszej pętli wyjdzie wątek o najmniejszym indeksie (zawsze taki istnieje).

Z drugiej pętli wychodzi wątek o największym indeksie (też zawsze taki istnieje).

#### Niezagłodzenie (wystepuje)

Podczas oczekiwania `while (flag[j] == true)` w pierwszej pętli zachodzi `flag[i] = false`.

Więc jeżeli podczas tego czekania drugi wątek będzie szybki to zachowa się tak jakby drugi wątek nigdy nie ustawił flagi.
