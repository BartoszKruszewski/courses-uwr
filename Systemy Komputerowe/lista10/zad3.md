#### Rezultaty odwołań

- **hit**: trafienie
- **compulsory miss**: pusta komórka pamięci
- **conflict miss**: inna wartość niż potrzebna

#### Odwołania

| Adres | Bity 11 - 0    | Trafienie?      |
| ----- | -------------- | --------------- |
| 0     | 00 00000 00000 | compulsory miss |
| 4     | 00 00000 00100 | hit             |
| 16    | 00 00000 10000 | hit             |
| 132   | 00 00100 00100 | compulsory miss |
| 232   | 00 00111 01000 | compulsory miss |
| 160   | 00 00101 00000 | compulsory miss |
| 1024  | 01 00000 00000 | conflict miss   |
| 28    | 00 00000 11100 | conflict miss   |
| 140   | 00 00100 01100 | hit             |
| 3100  | 11 00000 11100 | conflict miss   |
| 180   | 00 00101 10100 | hit             |
| 2180  | 10 00100 00100 | conflict miss   |

- Liczba zastąpionych bloków: $8$
- Efektywność: $4 / 12 = 33%$

Zawartość pamięci po wykonaniu odwołań:

```
tag, index, ...
11,  000,   ...
10,  100,   ...
0,   101,   ...
0,   111,   ...
```
