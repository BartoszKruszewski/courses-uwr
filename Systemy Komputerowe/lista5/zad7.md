#### Przekształcenie wyrażenia

$x = a*a*a + 4*a*a*b + 4*a*b*b + b*b*b = (a + b)^3 + a*a*b + a*b*b = (a + b)^3 + a*b*(a + b)$

#### Program optymalny w kodzie trójkowym

```
t1 := a + b     # t1 = a + b
t2 := t1        # t2 = a + b
t2 := t2 * t1   # t2 = (a + b) ^ 2
t2 := t2 * t1   # t2 = (a + b) ^ 3
t1 := t1 * a    # t1 = (a + b) * a
t1 := t1 * b    # t1 = (a + b) * a * b
t1 := t1 + t2   # t1 = (a + b) * a * b + (a + b) ^ 3
```

#### Program bez przekształcenia, ale z wykorzystaniem $mem$

Zdefiniujmy:\
$x := a[i]$ jest tym samym co $t := a + i; x := *t$\
$a[i] := x$ jest tym samym co $t := a + i; *t := x$

```
# wyliczenie wartośći i zapisanie ich w tablicy
t := a * a
t := t * a
mem[0] := t
t := 4 * a
t := t * a
t := t * b
mem[1] := t
t := 4 * a
t := t * b
t := t * b
mem[2] := t
t := b * b
t := t * b
mem[3] := t

# odczytanie wartości i dodanie ich
r := mem[0]
t := r
r := mem[1]
t := t + r
r := mem[2]
t := t + r
r := mem[3]
t := t + r
```
