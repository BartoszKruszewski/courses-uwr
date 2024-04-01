#### Operacja $x = y \; binop \; imm$

Wystarczy zmodyfikować wartości przesyłane przez **Control Unit**, dla instrukcji $x = y binop z$ z zadania 3.

Wartość dla multipleksera **ALUSrc** ustawiamy na $1$.
_Reszta indetycznie jak dla $x = y binop z$._

#### Operacja $goto \; L$

W przypadku, w którym skok ma się odbyć do intrukcji o indeksie L, wystarczy przemnożyć wartość stałej L przez 4, czyli wykonacać przesunięcie bitowe w lewo o 2. (Mnożymy przez 4 ponieważ instrukcje zajmują równo 4 bajty i są zapisane po kolei obok siebie). Następnie ustawiamy licznik rozkazów na obliczoną wartość.

W przypadku tej instrukcji pomijamy użycie prawie wszystkich pozostałych elementów procesora, więc należu ustawić wartości odpowiadające naszej instrukcji w **ControlUnit** na "wyłączające" wykorzystanie innych układów.

Nie musimy kodować innych adresów poza $L$, także w przypadku tej instrukcji ograniczenia zasięgu skoku są znacznie mniejsze niż w przypadku $ if \; x \; relop \; y \; goto \; L $.
