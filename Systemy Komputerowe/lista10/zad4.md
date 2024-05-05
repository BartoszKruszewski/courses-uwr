#### LRU

**LRU** - Least Recently Used Value

Taka polityka oznacza, że zamiast zastępowania wartości w cache'u "po kolei", zastępujemy wartość, która została użyta najdawniej.

#### Pamięć sekcyjno-skojarzeniowa

Nasza pamięć jest 3-drożna, czyli każdy zbiór ma 3 bloki.
Liczba bloków to 24, więc mając 3 bloki na zbiór mamy 8 zbiorów.
Liczba indeksów to 8, więc potrzebujemy na nie 3 bity.
Blok ma długość 2 słów czyli 64bity = 8 bajtów, więc potrzebujemy na nie 3 bity.
Na tagi zostaje nam 32 - 3 - 3 = 26 bitów.

| Adres | Bity 11 - 0    | Trafienie?      |
| ----- | -------------- | --------------- |
| 0     | 000000 000 000 | compulsory miss |
| 4     | 000000 000 100 | hit             |
| 16    | 000000 010 000 | compulsory miss |
| 132   | 000010 000 100 | compulsory miss |
| 232   | 000011 101 000 | compulsory miss |
| 160   | 000010 100 000 | compulsory miss |
| 1024  | 010000 000 000 | compulsory miss |
| 28    | 000000 011 100 | compulsory miss |
| 140   | 000010 001 100 | compulsory miss |
| 3100  | 110000 011 100 | compulsory miss |
| 180   | 000010 110 100 | compulsory miss |
| 2180  | 100010 000 100 | conflict miss   |

- Liczba zastąpionych bloków: $11$
- Efektywność: $1 / 12 = 8%$

Zawartość pamięci po wykonaniu odwołań:

| index | tag    |
| ----- | ------ |
| 0     | 100010 |
|       | 10     |
|       | 10000  |
| ----- | ------ |
| 1     | 10     |
|       | -      |
|       | -      |
| ----- | ------ |
| 10    | 0      |
|       | -      |
|       | -      |
| ----- | ------ |
| 11    | 0      |
|       | 110000 |
|       | -      |
| ----- | ------ |
| 100   | 10     |
|       | -      |
|       | -      |
| ----- | ------ |
| 101   | 11     |
|       | -      |
|       | -      |
| ----- | ------ |
| 110   | 10     |
|       | -      |
|       | -      |
| ----- | ------ |
| 111   | -      |
|       | -      |
|       | -      |

#### Pamięć sekcyjno-skojarzeniowa

Nasza pamięć jest 3-drożna, czyli każdy zbiór ma 3 bloki.
Liczba bloków to 24, więc mając 3 bloki na zbiór mamy 8 zbiorów.
Liczba indeksów to 8, więc potrzebujemy na nie 3 bity.
Blok ma długość 2 słów czyli 64bity = 8 bajtów, więc potrzebujemy na nie 3 bity.
Na tagi zostaje nam 32 - 3 - 3 = 26 bitów.

| Adres | Bity 11 - 0    | Trafienie?      |
| ----- | -------------- | --------------- |
| 0     | 000000 000 000 | compulsory miss |
| 4     | 000000 000 100 | hit             |
| 16    | 000000 010 000 | compulsory miss |
| 132   | 000010 000 100 | compulsory miss |
| 232   | 000011 101 000 | compulsory miss |
| 160   | 000010 100 000 | compulsory miss |
| 1024  | 010000 000 000 | compulsory miss |
| 28    | 000000 011 100 | compulsory miss |
| 140   | 000010 001 100 | compulsory miss |
| 3100  | 110000 011 100 | compulsory miss |
| 180   | 000010 110 100 | compulsory miss |
| 2180  | 100010 000 100 | conflict miss   |

- Liczba zastąpionych bloków: $11$
- Efektywność: $1 / 12 = 8%$

Zawartość pamięci po wykonaniu odwołań:

| index |  tag   |
| ----- | ------ |
| 0     | 100010 |
|       | 000010 |
|       | 010000 |
| ----- | ------ |
| 1     | 000010 |
|       | -      |
|       | -      |
| ----- | ------ |
| 10    | 000000 |
|       | -      |
|       | -      |
| ----- | ------ |
| 11    | 000000 |
|       | 110000 |
|       | -      |
| ----- | ------ |
| 100   | 000010 |
|       | -      |
|       | -      |
| ----- | ------ |
| 101   | 000011 |
|       | -      |
|       | -      |
| ----- | ------ |
| 110   | 000010 |
|       | -      |
|       | -      |
| ----- | ------ |
| 111   | -      |
|       | -      |
|       | -      |

#### Pamięc w pełni asocjacyjna

Taka pamięć nie ma podziału na zbiory, więc nie ma bitów na indeks.
Blok ma długość 1 słowa, tzn. 32 bity = 4 bajty, więc potrzebujemy na niego 2 bity.
Na tagi zostaje nam 32 - 2 = 30 bitów.

Nie mamy zbiorów, więc nie występuje **conflict miss**.
Zamiast tego, może wystąpić przekroczenie liczby bloków, czyli **capacity miss**.

| Adres | Bity 11 - 0   | Trafienie?      |
| ----- | ------------- | --------------- |
| 0     | 0000000000 00 | compulsory miss |
| 4     | 0000000001 00 | compulsory miss |
| 16    | 0000000100 00 | compulsory miss |
| 132   | 0000100001 00 | compulsory miss |
| 232   | 0000111010 00 | compulsory miss |
| 160   | 0000101000 00 | compulsory miss |
| 1024  | 0100000000 00 | compulsory miss |
| 28    | 0000000111 00 | compulsory miss |
| 140   | 0000100011 00 | capacity miss   |
| 3100  | 1100000111 00 | capacity miss   |
| 180   | 0000101101 00 | capacity miss   |
| 2180  | 1000100001 00 | capacity miss   |

- Liczba zastąpionych bloków: $12$
- Efektywność: $0 / 12 = 0%$

| index |    tag     |
| ----- | ---------- |
| 0     | 0000100011 |
|       | 1100000111 |
|       | 0000101101 |
|       | 1000100001 |
|       | 0000111011 | 
|       | 0000101000 |
|       | 0100000000 |
|       | 0000000111 |
