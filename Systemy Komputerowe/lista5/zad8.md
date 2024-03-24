### Sortowanie bąbelkowe w pseudokodzie

```
for i = 0 ... n:
    for j = 0 ... n:
        if t[i] > t[j]:
            swap(t[i], t[j])
```

### Sortowanie bąbelkowe w kodzie trójkowym

Zdefiniujmy:\
$x := a[i]$ jest tym samym co $t := a + i; x := *t$\
$a[i] := x$ jest tym samym co $t := a + i; *t := x$

```
n - rozmiar tablicy
i, j - zmienne do iteracji
r - zmienna tymczasowa dla przesuniecia indeksu o 1
t1, t2 - zmienne tymczasowe dla porownywanych elementow tablicy

S, E - początek i koniec zewnętrznej pętli
A, B - początek i koniec wewnętrznej pętli
I - skok ifa, jeżeli nie należy zamienić elementów

   i := 0
S: if i >= n - 1 goto E
   j = 0
A: if j >= n - 1 goto B
   r = j + 1
   t1 = t[j]
   t2 = t[r]
   if t1 > t2 goto I
   t[j] = t2
   t[r] = t1
I: j = j + 1
   goto A
B: i = i + 1
   goto S
E:
```
