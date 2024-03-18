Oznaczmy $RD_\circ$ jako $IN$ oraz $RD_\bullet$ jako $OUT$

```
OUT(1) = IN(1) \ {(x, l) | l ∈ L } U {(x, 1)}
OUT(2) = IN(2) \ {(y, l) | l ∈ L } U {(y, 2)}
OUT(3) = IN(3) \ {(i, l) | l ∈ L } U {(i, 3)}
OUT(4) = IN(4)
OUT(5) = IN(5) \ {(t, l) | l ∈ L } U {(t, 5)}
OUT(6) = IN(6) \ {(x, l) | l ∈ L } U {(x, 6)}
OUT(7) = IN(7) \ {(y, l) | l ∈ L } U {(y, 7)}
OUT(8) = IN(8) \ {(i, l) | l ∈ L } U {(i, 8)}
OUT(9) = IN(9) \ {(y, l) | l ∈ L } U {(y, 9)}

IN(1) = {(x, ?), (y, ?), (i, ?), (t, ?)}
IN(2) = OUT(1)
IN(3) = OUT(2)
IN(4) = OUT(3) U OUT(8)
IN(5) = OUT(4)
IN(6) = OUT(5)
IN(7) = OUT(6)
IN(8) = OUT(7)
IN(9) = OUT(8)
```

Algorytm:

Oznaczmy lewe strony równań jako $SL$ i prawe jako $SR$\

```
while SL != SR:
    SL(i) = SR(i)
    i = (i + 1) % n
```
