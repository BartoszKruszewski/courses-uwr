#### Podział adresu

Adres ma 12 bitów z czego 8 bitów od lewej to tag, kolejne dwa to indeks, a ostatnie dwa to offset. W systemie szestnastkowym dwie pierwsze cyfry oznaczają tag a ostatnia indeks oraz offset.

#### Wyszukiwanie

1. Szukamy zbioru o odpowiednim **indeksie**
2. Sprawdzamy, czy zawiera odpowiedni **tag**
3. Sprawdzamy, czy znaleziony tag jest **valid**
4. Odczytujemy wartość przesuniętą o **offset**

Jeżeli, na którymś etapie nie możemy dopasować wyszukiwania to znaczy, że nie ma trafienia.

#### Interpretacja adresów

```
832
tag: 83
(2 = 0010)
indeks: 00 = 0
offset: 10 = 2

835
tag: 83
(5 = 0101)
indeks: 01 = 1
offset: 01 = 1

FFD
tag: FF
(D = 1101)
indeks: 11 = 3
offset: 01 = 1
```

#### Wyniki

| Adres | Trafienie?      | Wartość |
| ----- | --------------- | ------- |
| 832   | Tak             | CC      |
| 835   | Nie (Valid = 0) | ...     |
| FFD   | Tak             | C0      |
