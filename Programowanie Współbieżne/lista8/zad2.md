#### Konstrukcja 

Rejestry RMW trzymają wartości proponowane przez wątki, początkowo ustawione na `-1`

`decide()` bez straty ogolnosci dla wątku A:

Wywołujemy `double_cAS(RAB, RAC, -1, A)`

- dla `true` zwracamy wartość z rejestru A
- dla `false`, przeszukujemy dwa przypisane rejestry RMW w poszukiwaniu wartości różnej od `-1`

#### Wait-free:

Poza operacjami atomowymi nie ma pętli.

#### Ta sama wartość dla wszystkich wątków

Funkcja `decide()` zwraca wartość pierwszego wątku który zapisał do rejestrów.

Operacje RMW są atomowe, więc mamy pewność, że do obu rejestrów zostala zapisana ta sama wartość a trzeci jest zwraca przy sukcesie zapisu.

#### Zwracana wartość jest jedną z propozycji

Zwracana wartość pochodzi z rejestrów atomowych przypisanych do wątków

Zostają one wypełnione przed uruchomieniem funkcji `decide()` i pozostają niezmienne.
