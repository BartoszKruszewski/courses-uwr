#### Konstrukcja

```java
private BinaryConsensus cons[M];
private AtomicRegister<T> propose[M];

public T decide(T value) {
    propose[id] = value;
    cons[id].decide(true);
        
    for(int i = 0; i < M; i++)
        decision = cons[i].decide(false);
        if(decision) return propose[i];
}
```

#### Intuicja

Używamy tyle obiektów binarnego konsensusu ile jest wątków (a więc i wartości).

Dodatkowo dla każdego takiego obiketu mamy skojarzony z nim rejestr atomowy.

Każdy wątek wpisuje do swojego rejestru swoją wartość, oraz proponuje dla skojarzonego z nim obiektu konsensusu wartość `true`.

Następnie wszystkie wątki sprawdzają po kolei obiekty konsensusu.

Wszystkie obiekty mają w nich taka samą decyzję, więc jeżeli trafią na pierwszy rejestr który ma `true` to wszystkie na nim zakończą.

#### Poprawność

Zanim odbywa się jakiekolwiek sprawdzanie, to musiała się odbyć przynajmniej jedna propozycaja `true`, więc jakiś wątek się na niej zatrzyma.

Obiekty spełniają binarny konsensus, więc mamy pewność, że wszystkie wątki odczytają te samą wartość.

Kolejność sprawdzania jest taka sama dla wszystkich wątków, więc wszystkie zatrzymają się na pierwszym `true` i zwrócą tą samą wartość.

