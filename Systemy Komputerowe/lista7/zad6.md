#### Ogólne informacje

Intresuja nas instrukcje if x relop y goto L, ponieważ tylko one wywołują skoki. Stanowią one 25% programu, więc reszta instrukcji to 75%.

Early Branch Execution powoduje, że niepoprawne przewidywanie skoku powoduje wykonanie jednego zbędnego cyklu.

CPI będziemy liczyć od nasycenia potoku (program bez hazardów miałby CPI = 1)
N oznacza ilość instrukcji.

##### A

Predykator statyczny always taken ma poprawnośc na poziomie 45%, czyli w 55% przypadków wykonany zostanie zbędny cykl.

```
Ilość cykli:
N * 0.75 + N * 0.25 * 0.45 + N * 0.25 * 0.55 * 2 =
N * (0.75 + 0.1125 + 0.275) =
N * 1.1375

CPI = 1.1375
```

##### B

Predykator statyczny always not taken ma poprawnośc na poziomie 55%, czyli w 45% przypadków wykonany zostanie zbędny cykl.

```
Ilość cykli:
N * 0.75 + N * 0.25 * 0.55 + N * 0.25 * 0.45 * 2 =
N * (0.75 + 0.1375 + 0.225) =
N * 1.1125

CPI = 1.1125
```

##### C

Predykator 2-bitowy ma poprawnośc na poziomie 85%, czyli w 15% przypadków wykonany zostanie zbędny cykl.

```
Ilość cykli:
N * 0.75 + N * 0.25 * 0.85 + N * 0.25 * 0.15 * 2 =
N * (0.75 + 0.2125 + 0.075) =
N * 1.0375

CPI = 1.0375
```

#### D

Ilość skoków zmniejsza się o połowę, czyli do 12,5%, reszta instrukcji stanowi wtedy 87,5%.
Szanse na poprawność skoków nie zmieniają się.

Predykator statyczny always taken:

```
Ilość cykli:
N * 0.875 + N * 0.125 * 0.45 + N * 0.125 * 0.55 * 2 =
N * (0.875 + 0.05625 + 0.1375) =
N * 1.06875

CPI = 1.06875
```

Predykator statyczny not always taken:

```
Ilość cykli:
N * 0.875 + N * 0.125 * 0.55 + N * 0.125 * 0.45 * 2 =
N * (0.875 + 0.06875 + 0.1125) =
N * 1.05625

CPI = 1.05625
```

Predykator 2-bitowy:

```
Ilość cykli:
N * 0.875 + N * 0.125 * 0.85 + N * 0.125 * 0.15 * 2 =
N * (0.875 + 0.10625 + 0.0375) =
N * 1.01875

CPI = 1.01875
```

Przyśpieszenie:

```
always taken: (1.1375 - 1.06875) / 1.1375 = 6%
not always taken: (1.1125 - 1.05625) / 1.1125 = 5%
2-bitowy: (1.0375 - 1.01875) / 1.0375 = 2%
```
