#### Program

```
Wartości początkowe:
s0 = 11
s1 = 22

Intrukcje:
s0 = s1 + 5
s2 = s0 + s1
s3 = s0 + 15
s4 = s0 + s0
```

#### Fazy działania procesora

- **F**: Fetch
- **D**: Decode
- **E**: Execute
- **M**: Memory
- **W**: Writeback

**F -> D -> E -> M -> W**

#### Data Hazard

Data hazard występuje, jeżeli odczytujemy wartość, która powinna zostać zmodyfikować poprzednimi instrukcjami, ale jeszcze nie została wykonana jej faza Writeback (W). Zapisywanie wykonuje się w pierwszej połowie cyklu, a odczytywanie w drugiej, więc jeżeli W oraz D występują w tej samej fazie, lub D zostanie wykonane w fazie późniejszej, to wartość zostanie odczytana poprawnie. W przeciwnym przypadku odczytana zostanie ostatnia wartość zapisana w rejestrze (wystąpi data hazard).

#### Diagram wykonania (bez nop)

```
1:      2:      3:      4:      5:      6:      7:      8:
F +     D s1 5  E       M s0    W
        F +     D s0 s1 E       M s2    W
                F +     D s0 15 E       M s3    W
                        F +     D s0 s0 E       M s4    W
```

#### Wyniki działania programu (bez nop)

```
s0 = 27 // nie występują problemy
s1 = 22
s2 = 33 // s0 nie zostało zapisane, więc s0 = 11
s3 = 26 // s0 nie zostało zapisane, więc s0 = 11
s4 = 54 // s0 zostało zaspisane, więc s0 = 27
```

#### Program (uzupełniony o nop)

```
Wartości początkowe:
s0 = 11
s1 = 22

Intrukcje:
s0 = s1 + 5
nop
nop
s2 = s0 + s1
s3 = s0 + 15
s4 = s0 + s0
```

#### Diagram wykonania (z użyciem nop)

```
1:      2:      3:      4:      5:      6:      7:      8:      9:      10:
F       D s1 5  E       M s0    W
        F nop   D       E       M       W
                F nop   D       E       M       W
                        F +     D s0 s1 E       M s2    W
                                F +     D s0 15 E       M s3    W
                                        F +     D s0 s0 E       M s4    W
```

#### Wyniki działania programu (z użyciem nop)

```
s0 = 27 // nie występują problemy
s1 = 22
s2 = 49 // s0 zostało zapisane, więc s0 = 27
s3 = 42 // s0 zostało zapisane, więc s0 = 27
s4 = 54 // s0 zostało zaspisane, więc s0 = 27
```
