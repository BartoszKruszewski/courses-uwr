#### Konstrukcja

Wartości będziemy zapisywać jako ich binarne reprezentacje, stąd dla wartości od 0 do M-1 potrzeba log M rejestrów boolowskich.

Dodatkowo tworzymy "bufor", czyli drugi identyczy ciąg log M rejestrów oraz jeden rejestr boolowski flag, który bedzie wskazywać w jakim rejestrze jest najbardziej aktualna wartość.

`write()` najpierw ustawia flage na przeciwny rejestr a w drugim po kolei modyfikuje bity. Po zakonczeniu zapisu, zmienia znowuy flage na przeciwny rejestr i modyfikuje drugi rejestr.

`read()` czyta po kolei bity z rejestru wskazanego przez flage

#### Wywołanie `read()` która nie jest współbieżne z żadnym wywołaniem `write()` zawsze zwraca wartość umieszczoną tam przez ostatnie wcześniejsze wywołanie `write()`

W takiej sytuacji cały `write()` odbywa się przed `read()`, więc ustawia wszystkie bity, więc wartość jest poprawnie zapisana i dopiero wtedy `read()` ją całą odczytuje.

#### Wywołanie `read()` współbieżne z dokładnie jednym wywołaniem `write()` zwraca wartość zapisaną przez to wywołanie, lub przez ostatnie wcześniejsze wywołanie `write()`

Wtedy mogą wystąpić dwa przypadki:
- `write()` zakończył zapis do jedenego z rejestrów: wtedy odczytana zostanie aktualna wartość
- `write()` jest w trakcie zapisu do pierwszego rejestru: wtedy odczytana zostaje wartość z rejestru zapasowego

#### W przeciwnym przypadku (wywołanie `read()` jest współbieżne z wieloma wywołaniami `write()`) wartość zwracana przez `read()` jest dowolna

Wtedy oba rejestry mogą być modyfikowane na raz, więc wartość odczytana z `read()` będzie jakąś wartością zbudowaną z bitów z rejestru.
