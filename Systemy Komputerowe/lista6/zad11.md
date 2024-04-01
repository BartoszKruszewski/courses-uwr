#### Zamiana instrukcji $ x = \*(y+ imm) $

- $t = y + imm$ $(825ps)$

- $x = *t$

```
PC -> IM -> RF -> DM -> MX -> RF

T_c = 50 + 250 + 150 + 250 + 25 + 150 = 875
```

#### Zamiana instrukcji $ \*(x+ imm) = y $

- $t = x + imm$ $(825ps)$

- $*t = y$

```
PC -> IM -> RF -> DM

T_c = 50 + 250 + 150 + 250 = 700
```

#### Nowa długość cyklu

Dokonując powyższej zamiany instrukcji sprawiamy, że maksymalny cykl będzie wynosił $875$ (operacja $x = *t$).

#### Nowe czasy działania

Teraz $ x = \*(y+ imm) $ oraz $ \*(x+ imm) = y $ wymagają użycia dwóch cyklów zamiast jednego.

#### Obliczenia

Czas działania starego procesora: $N * 1075$
Czas działania nowego procesora:

```
N * (2 * 0.25 + 2 * 0.11 + 0.12 + 0.52) * 875 =
= N * 1.36 * 875 = N * 1190
```

Więc stary procesor działa szybciej dla programu o podanej charakterystyce.

Natomiast mając program o innej charaktyce, gdzie operacje korzystające z pamięci występują rzadziej to jego czas działania wynosi:

```
N * (2 * 0.05 + 2 * 0.05 + 0.2 + 0.7) * 875 =
= N * 1.1 * 875 = N * 962.5
```

Wtedy nowy procesor działa szybciej.
