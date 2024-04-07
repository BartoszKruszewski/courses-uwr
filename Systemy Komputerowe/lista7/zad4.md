#### Program

```
LOOP: s0 = *s3
      s1 = *(s3 + 8)
      s2 = s0 + s1
      s3 = s3 - 16
      if s2 != 0 goto LOOP
```

#### Always taken i not taken

Always taken zakłada, że zawsze warunek skoku zostanie spełniony, więc po fazie Fetch instrukcji beq wykonuje instrukcje z miejsca potencjalnego skoku. Natomiast Always not taken zakłada, że zawsze warunek skoku będzie fałszywy i wykonuje instukcje następujące po beq.

Always taken lepiej sprawdza się dla programów, gdzie występują pętle, z dużą liczbą iteracji.

W zależnośći od tego, czy zgadniemy prawdziwość warunku skoku to dla dwóch iteracji programu z tego zadania lepsza będzie jedna z tych dwóch metod.

#### Diagram wykonania (always taken)

```
1:      2:      3:      4:      5:      6:      7:      8:      9:      10:     11:     12:     13:     14:     15:     16:     17:     18:
F lw    D s3    E s3    M s0    W
        F lw    D s3 8  E s3 8  M s1    W
                F +     D s0 s1 D s0 s1 E       M s2    W //stalling i forwarding
                        F -     F -     D s3 16 E       M s3    W
                                        F beq   D s2 0  E       M       W //forwarding
                                                F lw    D s3    E       M s0    W //forwarding
                                                        F lw    D s3 8  E s3 8  M s1    W
                                                                F +     D s0 s1 D s0 s1 E       M s2    W //stalling i forwarding
                                                                        F -     F -     D s3 16 E       M s3    W
                                                                                        F beq   D s2 0  E       M       W
```

#### Diagram wykonania (always not taken)

```
1:      2:      3:      4:      5:      6:      7:      8:      9:      10:     11:     12:     13:     14:     15:     16:     17:     18:
F lw    D s3    E s3    M s0    W
        F lw    D s3 8  E s3 8  M s1    W
                F +     D s0 s1 D s0 s1 E       M s2    W //stalling i forwarding
                        F -     F -     D s3 16 E       M s3    W
                                        F beq   D s2 0  E       M       W //forwarding
                                                ...
                                                        ...
                                                                F lw    D s3    E       M s0    W
                                                                        F lw    D s3 8  E s3 8  M s1    W
                                                                                F +     D s0 s1 D s0 s1 E       M s2    W //stalling i forwarding
                                                                                        F -     F -     D s3 16 E       M s3    W
                                                                                                        F beq   D s2 0  E       M       W
```
