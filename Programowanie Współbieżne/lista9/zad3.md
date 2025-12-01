#### Konstrukcja

```java
public lock() {
    mySlot = next.getAndIncrement();
    while (!flags[mySlot % n]) {};
    flags[mySlot % n] = false;
}
public unlock() {
    flags[(mySlot+1) % n] = true;
}
```

#### Intuicja

Wątki "kolejkują się", to znaczy, że wirują na swoim slocie w tablicy, natomiast wychodząc z sekcji krytycznej nie zwalniają swojego slotu, a zamiast tego, dają sygnał dla kolejnego wątku "teraz twoja kolej.

#### Zalety względem zamków TAS/TTAS/Backoff

Wydajność zamka Andersona nie zależy od liczby wątków. W zamkach TAS/TTAS przy dużym obciążeniu wydajność drastycznie spada z powodu nasycenia magistrali.

Zamek Andersona gwarantuje dostęp w kolejności FIFO, a . TAS/TTAS/Backoff nie.

Czas oczekiwania jest deterministyczny, podczas gdy w Backoff jest losowy.

Przy zwolnieniu zamka budzi się tylko jeden wątek, a nie wszystkie na raz, jak w TAS/TTAS, gdzie po invalidacji cache następuje wyścig o zapis.

#### Problem "False Sharing"

Jeśli rozmiar linii pamięci podręcznej jest spory, to w jednej linii cache mieści się dużo flag.

Gdy Wątek zapisuje swoją flagę, procesor musi unieważnić całą linię cache.

Jeśli flagi innych wątków leżą na tej samej linii, ich procesory również stracą te dane z cache'u.

Powoduje to zbędny ruch na magistrali, niwecząc główną zaletę zamka Andersona, jaką jest "local spinning".

#### Rozwiązanie

Rozwiązaniem jest padding (wypełnienie).

Każdą flagę w tablicy należy rozszerzyć tak, aby jej rozmiar był równy lub wielokrotnością rozmiaru linii cache.

Dzięki temu każda flaga leży w osobnej linii cache, a modyfikacja jednej nie wpływa na pozostałe.
