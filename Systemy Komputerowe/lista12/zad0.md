#### Optymalny

Wymienia stronę, która nie będzie używana przez najdłuższy czas w przyszłości.

Teoretycznie wymaga idealnej wiedzy o przyszłych odwołaniach do pamięci, co jest niemożliwe do zrealizowania w rzeczywistości. W praktyce, algorytm ten jest używany jako punkt odniesienia do oceny innych algorytmów.

#### NRU (Not Recently Used)

Strony są klasyfikowane na podstawie dwóch bitów: "referenced" i "dirty". Wybiera się stronę z najniższą klasą priorytetu (np. referenced = 0 i dirty = 0).

Wymaga bitów "referenced" oraz "dirty" dla każdej strony.

#### FIFO (First-in First-out)

Wymienia stronę, która była najdłużej w pamięci.
Wymaga kolejeki FIFO do śledzenia kolejności ładowania stron.

#### Drugiej szansy

Modyfikacja FIFO. Gdy strona ma być wymieniona, sprawdza się bit "referenced". Jeśli jest ustawiony, bit jest kasowany i strona dostaje "drugą szansę", ale zostaje przesunięta na koniec kolejki.

Wymaga kolejki FIFO bitu "referenced" dla każdej strony.

#### Zegarowy

Jest to wariant algorytmu drugiej szansy, w którym strony są zorganizowane w okrągłą listę. Wskaźnik zegara przesuwa się po kole, dając każdej stronie "drugą szansę".

Wymaga bitu "referenced" dla każdej strony.

#### LRU (Last Recently Used)

Wymienia stronę, która była najdawniej używana.

Wymaga wsparcia do śledzenia kolejności użycia stron.
