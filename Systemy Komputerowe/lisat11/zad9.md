#### Założenia

- indeksowanie, za pomocą stron pamięci fizycznej zamiast wirtualnej
- procesy współdzielą tablicę stron (wpisy mają identyfikatory procesu)

#### Translacja adresów

1. Hashowanie adresu przez funkcję hashującą (może być skomplikowana).
2. Wyszukiwanie hasha w tablicy hashy (zawiera wszystkie możliwe hashe odpowiadające pamięci, do jednego hasha może być przydzielone łacuchowo max 8 wpisów)
3. Wyszkujemy numer strony w pamięci spośród trafionych wpisów

#### Zalety

- skalowanie liniowe wraz z pamięcią fizyczną.
- mniej odwołań do pamięci

#### Wady

- duże rozmiary wpisów
- gorsze współdzielenie pamięci
- uzależnienie od funkcji hashującej
