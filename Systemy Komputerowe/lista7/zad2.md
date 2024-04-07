#### Forwarding

Forwarding, polega na wykorzystywaniu obliczonych wartości, we wcześniejszych fazach niż Writeback, np w fazie Execute. Porządane wartości są wtedy bezpośrednio przekazywane do ALU. Forwarding działa podobnie do "analizy dostępnych wyrażeń".

#### Stalling

Stalling polega na powieleniu wykonania, którejś fazy działania instukcji, w celu wyrównania opóźnienia dla odycztu poprawnych wartości. Ponawianie wykonania fazy, skutkuje również dłużym wykorzystywaniem podzespołu procesora, przez co nie może on być używany przez kolejne instrukcje. W rezultacie ponowienie fazy jednej instrukcji, ponawia aktualne fazy wszystkich aktualnie wykonywanych instrukcji. Wykorzystanie, uzwględniając przesunięcie w czasie (w tył), zachodzi aż do fazy Fetch, więc wstrzymywane jest również przyjmowanie kolejnych instrukcji.

#### Program A

```
s1 = s2 + 5
t0 = t1 - t2
t3 = *(s1 + 15)
*(t0 + 72) = t5
t2 = s4 & s5
```

#### Diagram wykonania dla programu A

```
1:      2:      3:      4:      5:      6:      7:      8:      9:
F +     D s2 5  E       M s1    W
        F -     D t1 t2 E       M t0    W
                F lw    D s1 15 E s1 15 M t3    W // forwarding
                        F sw    D t0 72 E t0 72 M t5    W // forwarding
                                F &     D s4 s5 E       M t2    W
```

#### Program B

```
s0 = t0 + t1
s1 = t2 - t3
s2 = s0 & s1
s3 = t4 | t5
s4 = s2 + s3
```

#### Diagram wykonania dla programu B

```
1:      2:      3:      4:      5:      6:      7:      8:      9:      10:     11:
F +     D t0 t1 E       M s0    W
        F -     D t2 t3 E       M s1    W
                F &     D s0 s1 D s0 s1 E       M s2    W // stalling i forwarding
                        F |     F |     D t4 t5 E       M s3    W
                                        F +     D s2 s3 D s2 s3 E       M s4    W // stalling i forwarding
```

#### Program C

```
t0 = s0 + s1
t0 = t0 - s2
t1 = *(t0 + 60)
t2 = t1 & t0
```

#### Diagram wykonania dla programu C

```
1:      2:      3:      4:      5:      6:      7:      8:      9:      10:
F +     D s0 s1 E       M t0    W
        F -     D t0 s2 D t0 s2 E       M t0    W //stalling i forwarding
                F lw    F lw    D t0 60 E t0 60 M t1    W //forwarding
                                F &     D t1 t0 D t1 t0 E       M t2    W //stalling i forwarding
```

#### Program D

```
t0 = s0 + s1
t1 = *(s2 + 60)
t2 = t0 - t3
t3 = t1 & t0
```

#### Diagram wykonania dla programu D

```
1:      2:      3:      4:      5:      6:      7:      8:      9:      10:
F +     D s0 s1 E       M t0    W
        F lw    D s2 60 E s2 60 M t1    W
                F -     D t0 t3 E       M t2    W //forwarding
                        F &     D t1 t0 E       M t3    W //forwarding
```
