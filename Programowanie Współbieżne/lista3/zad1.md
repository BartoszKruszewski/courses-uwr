#### r-Bounded Waiting

Pojawienie się w sekcji wejściowej gwarantuje wejście do sekcji krytycznej po co najwyżej $r$ innych procesach.

W szczególności dla $ r = 0 $, mówimy o 0-ograniczonym czekaniu, co oznacza, że jeśli wątek wszedł do sekcji wejściowej przed innym, to również wejdzie do sekcji krytycznej przed nim. Jest to równoważne FCFS (First Come First Served).

#### Algorytm Petersona

```java
public void lock() {
    flag[i] = true;
    victim = i;
    while (flag[j] && victim == i) {};
}
public void unlock() {
    flag[i] = false;
}
```

#### Dowód

Załóżmy, że $D_0^j \rightarrow D_1^k$

Wtedy `flag[0]==true`, `flag[1]==true` oraz `victim==1`

Wątek 0 może opuścić swoją sekcję oczekiwania, podczas gdy wątek 1 nie może

Czyli $CS_0^j \rightarrow CS_1^k$

Stąd $r=0$