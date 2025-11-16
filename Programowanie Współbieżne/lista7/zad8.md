#### Konstrukcja

```java
public float decide(float value) {
    reg[id] = value;

    while (true) {
        float low = min(reg[id], reg[1 - id]);
        float high = max(reg[id], reg[1 - id]);
        if (high - low <= e) return reg[id];
        reg[id] = 0.5 * (low + high); // środek
    }
}

```

#### Poziom konsensusu

Alogrytm wykorzystuje same rejestry atomowe.

Wykonuje się w skończonej liczbie kroków (wartości w reg zbiegają do siebie), więc jest "wait-free".

Z tego wynika, że poziom konsensusu tego problemu nie może być wyższy niż poziom samych rejestrów atomowych, więc jest równy 1.