#### Algorytm Piekarni

```java
class Bakery implements Lock {
    public void lock() {
        flag[i] = true;
        label[i] = max(label)+1;
        while (∃k flag[k] && (label[i],i) > (label[k], k));
    }
    ...
}
```

#### Wzajemnie wykluczanie

Dowód nie wprost, 

Załóżmy że wątek 0 i wątek 1 znalazły się jednocześnie w sekcji krytycznej.

Rozpatrzmy przypadki:

1. `label[0] > label[1]`

    Warunek w while jest spełniony dla `k = 1`: `(∃k flag[1] && (label[0],0) > (label[1], 1))`

    Co jest sprzeczne z tym, że wątek 0 wszedł do sekcji krytycznej.

2. `label[0] == label[1]`

    Warunek w while jest spełniony dla `k = 0`: `(∃k flag[0] && (label[1],1) > (label[0], 0))`

    Co jest sprzeczne z tym, że wątek 1 wszedł do sekcji krytycznej.

#### Niezakleszczanie

Załóżmy nie wprost, że doszło do zakleszczenia.

Wszystkie zakleszczone wątki mają podniesione flagi i ustawione labele.

Rozważmy przypadki:

1. Są różne labele, to wchodzi ten z najmniejszym; sprzeczność
2. Są takie same labele, to wchodzi ten z najmniejszym id; sprzeczność

#### Niezagłodzenie

Załóżmy że, jakiś wątek jest głodzony.

Każdy innny wątek który był w sekcji krytycznej, musi przed ponownym wejściem odświeżyć label.

Zrobi to później od momentu naszego oczekiwania, więc po jakimś czasie każdy label będzie większy.

Co jest sprzeczne z `∃k flag[k] && (label[i],i) > (label[k], k)`
