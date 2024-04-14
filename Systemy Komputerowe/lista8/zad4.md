#### Program

```
r3 = r1 * r2
r5 = r4 + r3
r6 = r4 + r1
r7 = r8 * r9
r4 = r3 + r7
r10 = r5 * r6
```

#### Procesor a

Liczba cykli: $23$

```
FD123456W
 FD.....D123456W
  FD123456W
   FD123456W
    FD.....D123456W
     FD........D123456W
```

#### Procesor b

Liczba cykli: $21$

```
FD123456W
 FD.....D1234W
  FD1234W
   FD123456W
    FD.....D1234W
     FD......D123456W
```

Faza W kolejnych instrukcji nie zachowuje kolejności programu.

#### Procesor c

Liczba cykli: $20$

```
FD123456RW
 FD.....1234RW <- obliczamy szybciej w buforze
  FD1234R     W <- obliczamy szybciej w buforze, ale zapisujemy później
   FD123456R   W
    FD.....1234RW
     FD.....123456RW
```

Faza W kolejnych instrukcji zachowuje kolejność programu.
Jest trochę szybciej bo pomijamy czekanie na zapis do rejestru, ale kosztem operacji na buforze.
