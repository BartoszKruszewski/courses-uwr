#### Modyfikacja procesora

Procesor wykorzystujący tylko jedną jednostkę pamięci na dane oraz instrukcje. Hazard Strukturalny występuje, kiedy faza Fetch będzie wykonywana jednocześnie z fazą Memory, ponieważ nie możliwy jest jednoczesny dostęp do dwóch różnych komórek pamięci w jednym cyklu. Rozwiązaniem jest wstrzymanie potoku, poprzez Stalling.

#### Program

```
*(s3 + 12) = s5
s5 = *(s3 + 8)
s4 = s2 - s1
if s4 == 0 goto Label
s2 = s0 + s1
s2 = s6 - s1
```

#### Diagram wykonania

Dla uproszczenia zakładamy, że wykorzystujemy statyczną predykcję always not taken, a warunek skoku nie jest spełniony (czyli ignorujemy efekty działania beq).

Bez tych założeń w przypadku skoku, nastąpił hazard, ale dla instrukcji, które i tak nie mają znaczenia dla programu.

```
1:      2:      3:      4:      5:      6:      7:      8:      9:      10:     11:     12:
F sw    D s3 12 E s3 12 M       W
        F lw    D s3 8  E s3 8  M s5    W
                F -     D s2 s1 E       M s4    W
                        F beq   F beq   F beq   D s4 0  E       M       W //stalling x2
                                                F +     D s0 s1 E       M s2    W
                                                        F -     D s6 s1 E       M s2    W
```

#### Czy zmiana kolejnośći instrukcji z zachowaniem semantyki pomoże?

Tak, jeżeli przeniesiemy instrukcje wykorzystujące pamięć danych na koniec programu, gdzie nie będą miały następujących po nich instrukcji do wykonania.

#### Zmodyfikowany program

Ciężko określić czy ta zmiana wpływa na semantykę, jest to zależne od etykiety Label.

```
s4 = s2 - s1
s2 = s0 + s1
s2 = s6 - s1
if s4 == 0 goto Label
*(s3 + 12) = s5
s5 = *(s3 + 8)
```

#### Diagram wykonania zmodyfikowanego programu

```
1:      2:      3:      4:      5:      6:      7:      8:      9:      10:
F -     D s2 s1 E       M s4    W
        F +     D s0 s1 E       M s2    W
                F -     D s6 s1 E       M s2    W
                        F beq   D s4 0  E       M       W
                                F sw    D s3 12 E s3 12 M       W
                                        F lw    D s3 8  E s3 8  M s5    W
```

#### Czy wstawianie nop rozwiązuje problem?

NOP jest pobierany z pamięci, a to właśnie dostęp do pamięci powoduje hazard, więc NOP spowoduje identyczny problem jak dowolna inna instrukcja.
