#### Definicja

Historia jest **sekwencyjnie spójna**, zachowuje porządek programowy dla każdego procesu (lokalnie), niekoniecznie musi być linearyzowalna (czyli zachowywać porządek programowy globalnie).

#### Przykład 1: Rejestr FIFO

Sekwecyjnie spójny, ale nie linearyzowalny

```
W(x, 1) ------- R(x) - 2
------- W(x, 2) ------->
```

NIE linearyzowalna, ponieważ (W1 zakończył się przed W2, ale R1 czyta 2)

#### Przykład 2: Kolejka z Opóźnionymi Odczytami

Zwykła kolejka, ale od wywołania Deq() do otrzymania wartości upływa jakiś czas (może być różny dla każdego wątku).

Sekwecyjnie spójny, ale nie linearyzowalny

```
Enq(A) ------------ Deq() - B ->
------ Enq(B) ----------------->
------------- Deq() ---------- A
```

NIE linearyzowalna, ponieważ (Enq1(A) zakończył się przed Enq2(B) a Deq1() czyta B)

#### Przykład 3: Rejestr FIFO (z cyklem zależności)

Nie jest spójna sekwencyjnie

```
W(x, 1) - R(y) - 1
W(y, 1) - R(x) - 0
```

```
R1(y) -> 1 wymaga: W2(y,1) < R1(y)
Porządek P1: W1(x,1) < R1(y)
R2(x) -> 0 wymaga: R2(x) < W1(x,1)
Porządek P2: W2(y,1) < R2(x)
```

stad

```
W1(x,1) < W2(y,1) < R1(y)
W2(y,1) < R2(x) < W1(x,1)
```

co jest sprzeczne


#### Przykład 4: Stos (z cyklem zależności)

```
Push(A) - Pop() - B
Push(B) - Pop() - A
```

```
Pop2()->A wymaga Pop1() < Pop2()
Pop1()->B wymaga Pop2() < Pop1()
```

co jest sprzeczne
