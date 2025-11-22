#### Konstrukcja

Mamy trzy rejestry w których trzymamy krotki:

- R1 (Środek): przechowuje (wartość, timestamp, właściciel).

- R0, R2 (Boki): Przechowują (wartość, timestamp).

R1 jest wspólny, R0 i R2 są przypisane do wątków.

Dodatkowo mamy tablice MRMR do ogłaszania wartości przed wykonaniem CAS (gwarancja odczytu w przypadku opóźnień).​

Zapis: 

1. Ogłaszenie wartości w Proposal
2. Próba wykonania CAS na rejestrze R1, podbijając timestamp
3. Po sukcesie aktualizacja rejestru bocznego

Odczyt:

1. Pobranie stanu R1.
2. Sprawdzenie timestampu rejestrów bocznych.
3. Jeśli timestamp boku jest mniejszy niż środka, oznacza to "brudny odczyt" – wtedy pobiera wartość z tablicy Proposal.
