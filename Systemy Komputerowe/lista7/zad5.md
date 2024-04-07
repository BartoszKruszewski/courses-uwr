#### Definicja

Early brach prediction polega na tym, że decyzja o wykonaniu skoku zamiast w fazie Execution odbywa się w fazie Decode (jedna faza szybciej). Uzyskiwane jest to dzięki dodatkowemu układowi, który porównuje czy wartośći na wyjściu z pliku rejestrów są identyczne. Jeżeli warunek zostanie spełniony to zostaje podjęta szybsza decyzja o skoku.

#### Program

```
LOOP: s0 = *s3
      s1 = *(s3 + 8)
      s2 = s0 + s1
      s3 = s3 - 16
      if s2 != 0 goto LOOP
```

#### Ulepszenie

Względem rozwiązania z zadania 4, w przypadku zastosowania Early Branch Prediction wykonujemy jedną niepotrzebną instrukcję zamiast dwóch.

#### Diagram wykonania (always not taken)

```
1:      2:      3:      4:      5:      6:      7:      8:      9:      10:     11:     12:     13:     14:     15:     16:     17:     18:
F lw    D s3    E s3    M s0    W
        F lw    D s3 8  E s3 8  M s1    W
                F +     D s0 s1 D s0 s1 E       M s2    W //stalling i forwarding
                        F -     F -     D s3 16 E       M s3    W
                                        F beq   D s2 0  E       M       W //forwarding
                                                ...
                                                        F lw    D s3    E       M s0    W
                                                                F lw    D s3 8  E s3 8  M s1    W
                                                                        F +     D s0 s1 D s0 s1 E       M s2    W //stalling i forwarding
                                                                                F -     F -     D s3 16 E       M s3    W
                                                                                                F beq   D s2 0  E       M       W
```

#### Przykład Data Hazard

```
    Początkowe wartości:
    s0 = 0

    Instrukcje:
    s0 = 1
    if s0 == 0 goto L
    ...
L:  ...
```

Tutaj w momencie wykonania szybkiego skoku wartość 1 nie zostanie jeszcze zapisana w s0, więc skok się wykona, a nie powinien.
Żeby pozbyć się hazardu
