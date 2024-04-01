#### Znaczenie operacji $*x = y + imm$

Operacja polega na zapisaniu do pamięci wartośći $y + imm$ pod adresem $x$.

#### Modyfikacje procesora

Należałoby poprowadzić ścieżkę z $RD1$ w **pliku rejestrów** do $A$ w **w pamięci danych** oraz z wyjścia **ALU** do $WD$ w **w pamięci danych**. Pozostały przebieg operacji jest bardzy podobny do innych intrukcji operacujących na danych w pamięci, które były prezentowane wcześniej.

W celu zachowania kompatybilności z pozostałymi instrukcjami należałoby dodać odpowiednie multipleksery i wysterować je dla nowego polecenia w **ControlUnit**.
