#### Czasy działania analizowanych instrukcji

- **$x = *(y+ imm)$** : $1075ps$
- **$*(x + imm):= y$** : $1075ps$
- **$if \; x \; relop \; y \; goto \; L$** : $675ps$
- **$x = y \; binop \; z$** : $825ps$

#### Czas działania procesora z zadania 6.

Maksymalna cyklu dla procesora z poprzedniej listy wynosiła $1075ps$. Więc, jeżeli wszystkie cykle mają stały czas to musi on wynosić przynajmniej $1075ps$.

#### Obliczenia

Oznaczmy jako $N$ liczbę wszystkich intrukcji w programie.
Wtedy czas działania programu dla procesora z zadania 6. wynosi $N * 1075ps$.

Mając do dyspozycji procesor obsługujący różne długości dla każdej instrukcji,
otrzymujemy czas działania równy:

```
N * (0.25 * 1075ps + 0.11 * 1075ps + 0.12 * 675ps + 0.52 * 825ps) =
N * (268,75 + 118,25 + 81 + 429) =
N * 897
```

Policzmy stosunek tych wartości:

```
N * 1075 - N * 897 = N * 178
(N * 178) / (N * 1075) = 0.17
```

#### Przyśpieszenie

Wykonując identyczny program na procesorze o możliwych różnych długościach cyklu uzyskamy przyśpieszenie rzędu $17\%$.
