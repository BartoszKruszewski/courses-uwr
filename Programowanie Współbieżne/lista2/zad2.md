#### Algorytm Petersona 

```java
public void lock() {
    flag[i] = true;
    victim = i; // zabezpieczenie przed zakleszczeniem
    while (flag[j] && victim == i) {};
}
public void unlock() {
    flag[i] = false;
}
```

#### Modyfikacja 

```java
public void unlock() {
    int i = ThreadID.get(); /*returns 0 or 1*/
    flag[i] = false;
    int j = 1 - i;
    while (flag[j] == true) {}
}
```

#### Niezakleszczenie

Jeżeli oba wątki są w `lock()`, to zmienna victim przepuści któregoś z nich.

Jeżeli oba wątki są w `unlock()` to ich flagi są ustawione na `false`, zatem `while (flag[j] == true)` nie jest spełniony.

Jeżeli jeden wątek (oznaczamy jako $watek0$) jest w `unlock()` a drugi (oznaczamy jako $watek1$) w `lock()` to 

```
write0(flag[0]=false) =>
write1(flag[1]=true) =>
write1(victim=1) =>
read_1(flag[0]==false) =>
read_1(victim==1) =>
CS1
```

A następnie oba są w `unlock()`.

#### Niezagłodzenie (kontrprzykład)

1. $watek0$ jest w `unlock()`, zatem:
    - `flag[0] = false`
1. $watek1$ wchodzi do `lock()`,
    - `flag[1] = true`
1. $watek1$ wychodzi z sekcji krytycznej i wchodzi do `unlock()`,
    - `flag[1] = false`,
    - nie wchodzi do pętli while,
    - ponownie moze wejsc do `lock()`,

Czyli występuje głodzenie $watek0$