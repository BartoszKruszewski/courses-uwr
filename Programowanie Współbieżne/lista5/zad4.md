#### Skąd się bierze out-of-order?

Współczesne procesory optymalizują kolejność wykonania instrukcji, tak żeby nie zmieniać działania programu, natomiast uwzględniaja przy tym każdy wątek osobno. Może to prowadzić do zmian działania programu wielowątkowego.

#### Przykład sprzeczności z sekwencyjną spójnością

```
mov 1 b
mov a %eax
```

da identyczny efekt dla pojedyńczego wątku co

```
mov a %eax
mov 1 b
```

natomiast majac drugi watek ktory wykona

```
mov 1 a
mov b %ebx
```

zoptymalizowane do 

```
mov b %ebx
mov 1 a
```

W rezultacie może doprowadzić do sytuacji gdzie po zakończeniu programu `%eax = %ebx = 0` co jest sprzeczne z intuicją i sekwencyjną spójnością.

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

#### Problemy na architekturze out-of-order

Procesor może przestawić `flag[i] = true` z odczytem `flag[j]`, ponieważ dotyczą różnych obszarów pamięci.

Założmy ze poczatkowo `flag[0] = flag[1] = 0`.

Oba wątki wykonają (z powodu out-of-order) najpierw odczyt `flag[0] == 0` oraz `flag[1] == 0`.

Więc oba w konsekwencji nie zatrzymają się na pętli `while` i oba wejdą do sekcji krytycznej.

Łamie to wzajemne wykluczenie.
