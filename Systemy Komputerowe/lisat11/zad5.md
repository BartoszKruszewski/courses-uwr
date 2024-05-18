#### Podpunkt a

Mamy 32-bitowe adresy, które pokrywają $2^32$ adresów wirtualnych.
Rozmiar strony to $4KiB = 2^12B$, więc nasza tablica stron musi pomieścić $2^32B / 2^12B = 2^20$ stron. Rozmiar strony to $4B = 2^2B$, więc rozmiat tablicy stron to $2^20 * 2^2B = 2^22B$

#### Podpunkt b

Poziom drugi ma $1024 = 2^10$ wpisów. Każdy wpis wskazuje na stronę pamięci pierwszego poziomu o rozmiarze $2^12B$, czyli strona drugiego poziomu pokrywa $2^10 * 2^12B = 2^22B$. Musimy pokryć proces, który zużywa $1GiB = 2^30B$ przestrzeni adresowej, więc potrzebujemy $2^30 / 2^22 = 2^8$ stron drugiego poziomu.

Minimalny rozmiar tablicy stron będzie wynosił $(1 + 2^8) * 4KiB = 1028KiB$ (strona 1 poziomu oraz strony drugiego poziomu, 2^8 to wystarczające pokrycie strony pierwszego poziomu).

Maksymalny rozmiar tablicy stron będzie wynosił $(1 + 2^10) * 4KiB = 4100KiB$ (2^10 to pełne pokrycie strony pierwszego poziomu).
