#### Intuicja

Algorytm Tomasulo działa podobnie do reorder buffer, ale zachowuje osobne buforowanie dla każdej jednostki ALU.

#### Register Renaming

Register Renaming rozwiązuje hazardy danych poprzez przypisywanie rejestrom Tagów, w celu ich dodatkowego rozróżnienia względem kolejności występowania w programie.

#### Struktury danych

Algorytm ma główną rejestr, który opisuje adresy stacji rezerwacyjnych. Stacje rezerwacyjne są osobne dla każdego ALU i pamiętają kolejne instrukcje, które ALU ma wykonać

Stacje rezerwacyjne:

- **Value**: wartość
- **Valid**: mówi czy dane są aktualne
- **Tag**: mówi skąd wziąć wartość

Rejestr główny:

- **Value**: wartość
- **Valid**: mówi, czy wartość jest aktualna
- **Tag**: jeżeli Valid jest równy 0 to mówi, która operacja liczy wartość

#### Algorytm

1. odczytanie instrukcji
2. nadanie wolnego pierwszego wolnego miejsca w rejestrze głównym (przypisanie do odpowiedniej stacji rezerwacyjnej)
3. jeżeli argumenty są VALID w rejestrze głównym to wykonujemy instrukcje, jeżeli nie to przepisujemy dane z rejestru głównego do stacji rezerwacyjnej
4. wykonywane są instrukcje, które są Valid oraz aktulizowane wartości Valid dla pozostałych instrukcji

#### Rozwiązania hazardów

**RAW**: zapisujemy instrukcje w kolejności programu
**WAR**: nadawanie tagów
**WAW**: tagi są kodowane zgodnie z kolejnością programu

#### Porównanie z Reorder Buffer

Algorytm jest szybszy, ponieważ pozwala na równoległe buforowanie wielu jenostek ALU, co powoduje eliminacje sytuacji w których buforowane instrukcje czekają niepotrzebnie.
