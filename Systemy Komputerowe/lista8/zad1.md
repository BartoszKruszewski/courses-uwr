#### Definicje hazardów

- **sterowania**: złe przewidywanie skoku w programie
- **strukturalny**: jednoczesne dostęp do pamięci dwóch instrukcji
- **RAW**: _read after write_ instrukcja odczytuje niezaktualizowany rejestr
- **WAR**: _write after read_
- **WAW**: _write after write_

#### Procesor jednocyklowy

W procesorze jednocyklowym nie występują hazardy, ponieważ żadne instrukcje nie są wykonywane równolegle.

#### Procesor potokowy z jednym ALU

W procesorze potokowym z pojedyńczym ALU występują hazardy:

**sterowania**

```
loop: ...
if t0 == t1 goto loop <- nie wiadomo jaki będzie wynik
... <- czyli nie wiadomo czy wykonywac ta instrukcje
```

**strukturalne** _jeżeli mamy współdzieloną pamięć_

```
*(t0 + 5) = 15
...
...
... <- podczas fetch wystąpi hazard
```

**RAW**

```
t0 = t1 + t2
t3 = t0 + t1 <- t0 nie zostanie jeszcze zaktualizowana
```

**WAR**
Nie wystepuje, ponieważ mając pojedyńcze ALU odczytywanie wartości nie może zostać opóźnione do fazy Writeback kolejnych instukcji.

**WAW**
Nie wystepuje, ponieważ fazy Writeback nie mogą wystąpić równolegle.

#### Procesor potokowy z wieloma ALU

**sterowania, strukturalne, RAW**

Tak jak w procesorze z pojedyńczym ALU.

**WAR**

```
t1 = t2 + t0
t0 = t3 + t4 <- może zostać zmieniona wartość zanim poprzednia instrukcja odczyta t0
```

**WAW**

```
t0 = t1 + t2 <- zapis może wykonać po zapisie z następnej instrukcji
t0 = t3 + t4
```
