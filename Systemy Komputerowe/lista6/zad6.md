#### Oznaczenia i czasy działania

- **IM**: pamięć instrukcji $(250ps)$
- **DM**: pamięć danych $(250ps)$
- **RF**: plik rejestrów $(150ps)$
- **MX**: multiplekser $(25ps)$
- **ALU**: jednostka arytmetyczno logiczna $(200ps)$
- **ADD**: adder do wyliczania BTA $(150ps)$
- **PC**: licznik rozkazów $(50ps)$
- **SE**: rozszerzenie reprezentacji $(50ps)$
- **CU**: jednostka kontrolna $(50ps)$

#### $x = *(y+ imm)$

```
PC -> IM -> max(CU -> MX, SE -> MX, RF) -> ALU -> DM -> MX -> RF

T_c = 50 + 250 + max(50 + 25, 50 + 25, 150) + 200 + 250 + 25 + 150 = 50 + 250 + 150 + 200 + 250 + 25 + 150 = 1075
```

#### $ \*(x + imm):= y $

```
PC -> IM -> max(CU -> MX, SE -> MX, RF) -> ALU -> DM -> MX -> RF

T_c = 50 + 250 + max(50 + 25, 50 + 25, 150) + 200 + 250 + 25 + 150 = 50 + 250 + 150 + 200 + 250 + 25 + 150 = 1075
```

Nie rozrużniamy kosztów $RF_{load}$ i $RF_{save}$, więc koszty $x = *(y+ imm)$ i $ \*(x + imm):= y $ wychodzą identyczne.

#### $ x = y \; binop \; z $

```
PC -> IM -> max(CU -> MX, RF) -> ALU -> MX -> RF

T_c = 50 + 250 + max(50 + 25, 150) + 200 + 25 + 150 = 50 + 250 + 150 + 200 + 25 + 150 = 825
```

#### $ if \; x \; relop \; y \; goto \; L $

```
PC -> IM -> max(max(CU -> MX, RF) -> ALU -> MX, SE -> MX -> ADD)

T_c = 50 + 250 + max(max(50 + 25, 150) + 200 + 25, 50 + 25 + 150) = 50 + 250 + max(375, 225) = 675
```

#### $x = y \; binop \; imm$

```
PC -> IM -> max(CU -> MX, RF, SE -> MX) -> ALU -> MX -> RF

T_c = 50 + 250 + max(50 + 25, 150, 50 + 25) + 200 + 25 + 150 = 50 + 250 + 150 + 200 + 25 + 150 = 825
```

#### $goto \; L$

```
PC -> IM -> CU -> MX

T_c = 50 + 250 + 50 + 25 = 375
```

#### Minimalny cykl

Minimalna długość cyklu występuje dla operacji $goto \; L$ i wynosi $375ps$
