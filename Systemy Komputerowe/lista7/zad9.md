Zastępując instrukcje jak w zadaniu, zmniejszamy liczbę faz do 4, ale zwiększamy liczbę instrukcji w programie.

Zakładając czasy działania podzespołów jak z listy 6:

- **IM**: pamięć instrukcji $(250ps)$
- **DM**: pamięć danych $(250ps)$
- **RF**: plik rejestrów $(150ps)$
- **MX**: multiplekser $(25ps)$
- **ALU**: jednostka arytmetyczno logiczna $(200ps)$
- **ADD**: adder do wyliczania BTA $(150ps)$
- **PC**: licznik rozkazów $(50ps)$
- **SE**: rozszerzenie reprezentacji $(50ps)$
- **CU**: jednostka kontrolna $(50ps)$

Długość faz 5-fazowego procesora będzie wynosić:

- **F**: Fetch (250ps)
- **D**: Decode (150ps + 25ps = 175ps)
- **E**: Execute (200ps)
- **M**: Memory (250ps + 25ps = 275ps)
- **W**: Writeback (150 + 25ps = 175ps)

Długość faz 4-fazowego procesora będzie wynosić:

- **F**: Fetch (250ps)
- **D**: Decode (175ps)
- **E**: Execute/Memory (275ps)
- **W**: Writeback (175ps)

Nowa ilość instrukcji:

```
N * (0.25 * 2 + 0.11 * 2 + 0.12 + 0.52) = N * 1.36
```

Zakładając, że każda instrukcja przechodzi przez wszystkie fazy uzyskujemy czasy wykonania jednej instrukcji:

```
5-fazowy procesor: 250ps + 175ps + 200ps + 275ps + 175ps = 1075ps
4-fazowy procesor: 250ps + 175ps + 275ps + 175ps = 875ps
```

Uwzględniając zmianę ilości instrukcji otrzymujemy czasy wykonania programu:

```
5-fazowy procesor: N * 1075ps
4-fazowy procesor: N * 1.36 * 875ps = 1190ps
```

Więc dla programów o podanej strukturze, 5-fazowy procesor będzie szybszy.
