#### 1. Konstrukcja

```java
public Boolean decide(Boolean value) {
    stickyBit.write(value);
    return stickyBit.read();
}
```

#### 1. Poprawność

Najszybszy wątek ustawi swoją wartość w `stickyBit`, a następne nic nie zmienią.

`write()` występuje przed `read()`, więc wartość w momecie `read()` zawsze jakaś będzie.

Wszystkie wątki zwrócą wartość ze StickyBit, która się nie zmienia, więc będzie taka sama.

#### 2. Konstrukcja

*Działa przy założeniu, że M jest potęgą 2*

```java
Integer proposed[N];
T values[M];

public T decide(T value) {
    value_id = values.index(value);
    proposed[Thread.getId()] = value_id;

    Boolean binary[] = to_bin(value_id);

    for (int i = 0; i < binary.length; i++) {
        stickyBits[i].write(binary[i]);
    }

    Boolean decision[];

    for (int i = 0; i < binary.length; i++) {
        decision[i] = stickyBits[i].read();
    }

    return proposed[to_dec(decision)];
}
```

#### 2. Intuicja

Trzymamy wszystkie możliwe wartości w rejestrach (jest ich M dowolnych), natomiast będzie operować na ich indekach (liczby od 0 do M).

Najpierw ustalamy jaki indeks ma wartość jaką proponuje wątek.

Zamieniamy indeks na system binarny, a następnie zapisujemy po kolei bity.

Następnie StickyBits są odczytywane i zamieniane na system dziesiętny, co pozwala ustalić wspólny indeks tablicy values.

#### 2. Poprawność

StickyBits są odczytywane tak samo dla każdego wątku.

Zostają odczytane dopiero po zakończeniu zapisu, więc mamy pewność, że zwrócą jakiś zapis.

Każdy zapis odpowiada wartości jakiegoś wątku, więc wartość będzie taka sama dla wszystkich wątków i będzie jedną z wartości proponowanych przez nie.
