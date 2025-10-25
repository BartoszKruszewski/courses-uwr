#### Algorytm

```java
public void lock () {
    flag[i] = true;
    label[i] = counter++;
    while (∃k flag[k] && (label[i], i) > (label[k], k));
}
public void unlock () {
    flag[i] = false;
}
```

#### Operacja counter++


W rzeczywistości operacja `counter++` języka wysokopoziomowego rozbija się na polecenia:

```
counter++:

r = counter
r = r + 1
counter = r

```




#### Wzajemne wykluczenie (niezachodzi)

Kontrprzykład

Mamy 3 wątki A, B i C, które chcą wykonać `label[i] = counter++;`. Załóżmy, że `counter = 0`
```
r_A = counter
r_B = counter
r_B = r_B + 1
counter = r_B + 1 // counter = 1;
label[B]= counter //1
r_C = counter
r_C = r_C + 1
counter = r_C + 1 // counter = 2;
label[C] = counter //2
r_A = r_A + 1
counter = r_A // counter = 1;
label[A] = counter // 1
```
W sekcji krytycznej mamy wątki C i A.

#### Niezakleszczenie

Jest spełnione, ponieważ nawet igorując counter i ustawiając wszystkim wątkom taką samą wartość, wątki rozdzielane są względem indeksów, więc zawsze istnieje wątek o najmniejszym indeksie.

#### Niezagłoszenie 

Rozważmy przypadki:

1. Wartości counter są równe - wtedy nie ma głodzenia bo rozdzielamy względem wątków
2. Wartości counter zachowują się "zgodnie z intuicją" (zwięszkają się) - wtedy również nie ma głodzenia jak w przypadku klasycznego algorytmu piekarni
3. Wartości counter uklegają "zmiejszeniu" (jak w kontrprzykładzie do wzajemnego wykluczenia):
    
    Zauważmy, że żeby zmiejszenie wystąpiło muszą wystąpić pełne wywołania `counter++`.
    
    Wtedy dla jakiegoś wątku wartość counter zostanie zwiększona (niekoniecznie dla wszystkich jak podpowiada intuicja), ale nie dla wątku który już ma zwiększoną wartość.
    
    W rezultacie po jakimś czasie wartości counter zostaną wyrównane względem potencjalnie głodzonego wątku.
    
    Czyli głodzenie również nie zachodzi