#### Algorytm

```java
public void lock () {
    flag[i] = true;
    label[i] = max(label[i], counter++);
    while (∃k flag[k] && (label[i], i) > (label[k], k));
}
public void unlock () {
    flag[i] = false;
}
```

#### Wzajemne wykluczenie (kontrprzykład)

```
counter = label[A, B, C] = 0

r_A = counter // 0

dla x = {B, C}
r_x = counter
r_x = r_x + 1
counter = r_x

wtedy counter = 2

label[B, C] = max(label[B, C], counter) = 2

r_A = r_A + 1 // 1
counter = r_A // 1
label[A] = max(label[A], counter) = 1

Wtedy A wchodzi do sekcji krytycznej i wychodzi zwlaniając flage
B wchodzi i wychodzi
C wchodzi i zostaje

r_B = counter // 1
r_B = r_B + 1 // 2
counter = r_B // 2
label[B] = max(label[B], counter) = 2 // tutaj mamy max(2, 2) = 2

Wtedy B przechodzi while ponieważ A nie ma ustawionej flagi, a label[C] = 2 = label[B], a B ma niższy indeks

Czyli do sekcji wchodzi B a nadal jest tam C.
```

Czyli dodanie maxa nie rozwiązuje problemu.


#### Niezagłodzenie i niezakleszczenie

Tutaj wszystko pozostaje bez zmian, ponieważ były spełnione, a tutaj mamy dodatkowe ograniczenie zmniejszenia się licznika.