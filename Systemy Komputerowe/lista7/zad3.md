#### Program

```
LOOP: s0 = *s3
      s1 = *(s3 + 8)
      s2 = s0 + s1
      s3 = s3 - 16
      if s2 != 0 goto LOOP
```

#### Diagram wykonania (pierwsze dwie iteracje)

```
1:      2:      3:      4:      5:      6:      7:      8:      9:      10:     11:     12:     13:     14:     15:     16:
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
