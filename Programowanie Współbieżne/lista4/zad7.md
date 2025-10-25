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

#### Algorytm Petersona jest FCFS

A pierwszy wykonał sekcję wejściową.

Załóżmy nie wprost, że B pierwszy wszedł do sekcji krytycznej.

Jeśli B jako drugi wykonał sekcję wejściową, to ustawił zmienną `victim` na samego siebie.

Więc musiał potem czekać w sekcji oczekiwania do wykonania przez A sekcji krytycznej.

W związku z tym B nie mógł wykonać sekcji krytycznej przed A.

#### Sekcja wejściowa jako pierwsza instrukcja

Wtedy definicja nie obejmuje `victim = i;` co jest kluczowe w dowodzie.

#### Czy istnieje algorytm który jest FCFS dla zmodyfikowanej definicji?

*Przypadek a*

Oba wątki odczytają to samo niezależnie od kolejności.

Nie da się rozróżnić wątków.

*Przypadek b*

Jeżeli komórki są różne to niezależnie od kolejności obie będą zapisane.

Nie da się rozróżnić wątków.

*Przypadek c*

Jeżeli jest jedna komórka, to drugi wątek całkowicie usuwa ślad pierwszego.

Nie da się rozróżnić czy są dwa wątki czy jeden.

#### Czy definicja ma sens?

Nie, bo nic jej nie spełnia
