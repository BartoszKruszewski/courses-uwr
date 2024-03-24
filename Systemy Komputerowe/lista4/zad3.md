Oznaczmy $RD_\circ$ jako $IN$ oraz $RD_\bullet$ jako $OUT$

```
OUT(1) = IN(1) \ {(x, l) | l ∈ L } U {(x, 1)}
OUT(2) = IN(2)
OUT(3) = IN(3) \ {(y, l) | l ∈ L } U {(y, 3)}
OUT(4) = IN(4) \ {(y, l) | l ∈ L } U {(y, 4)}
OUT(5) = IN(5) \ {(t, l) | l ∈ L } U {(z, 5)}

IN(1) = {(x, ?), (y, ?), (z, ?)}§
IN(2) = OUT(1)
IN(3) = OUT(2)
IN(4) = OUT(2)
IN(5) = OUT(3) U OUT(4)
```

1. Wyrazenia, zawierające zbiory do usunięca z rozwiązania to $kill$,
a wyrazenia dodające nowe zbiory to $gen$.

2. $kill([read(x)]^l) = \{(x,l') | l' \in L\}$\
   $gen([read(x)]^l) = \{(x,l)\}$

3. Stosujemy wstępny algorytm
    ```
    dla kazdej operacji:
        - dodaj do zbioru równań równanie 
        "IN = suma zbiorów OUT operacji wchodzących do aktualnej"
        - dodaj do zbioru równań równanie
        "OUT = IN / kill(aktualna operacja) U gen(aktualna operacja)"
    ```
    A następnie na otrzymanym zbiorze równań
    stosujemy algorytm stałopunktowy.