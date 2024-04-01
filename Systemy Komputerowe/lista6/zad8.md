#### Znaczenie operacji $x = *(y + z)$

Operacja polega na odczytaniu z pamięci wartości pod adresem $(y + z)$ i wpisanie jej do rejestru $x$.

#### Modyfikacje procesora

Instrukcja jest bardzo podobna do wcześniej omawianej $x = *(y + imm)$.
Różnica polega, że do A2 w rejestrze plików, będziemy podawać $z$ zamiast $imm$, więc w rezultacie otrzymamy wartość $z$ na wyjściu $RD2$. W **ControlUnit** należy przestawić wartość dla **ALUSrc** na odczytywanie $RD2$.

Pozostałe układy działają identycznie.
