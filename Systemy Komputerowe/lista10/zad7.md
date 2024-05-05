#### Co chcemy osiągnąć?

Naszym celem jest realizacja za pomocą struktury o $log_2(4!)$ bitach polityki LRU. Zadanie sprowadza się do przechowywania w strukturze informacji o kolejności bloków, względem czasu modyfikacji.

#### Struktura

$log_2(4!) \approx 5$
Musimy oznaczyć 4 bloki.

Podzielmy nasze $5$ bitów na trzy częśći:

- 2 bity na numer najstarszego bloku
- 2 bity na numer drugiego najstarszego bloku
- 1 bit mówiący, czy najbardziej lewy z pozostałych bloków (najnowszy lub drugi najnowszy) jest najnowszy

Taka reprezentacja pozwala uzyskać jednoznaczne przedstawienie kolejności bloków.

#### Realizacja zastąpienia

Wybór bloku do zastąpienia realizujemy, patrząc na dwa pierwsze bity (numer najstarszego bloku).

Strukturę aktualizujemy następująco:

1. Przepisujemy bity 3 i 4 do 1 i 2
2. Sprawdzamy, który z pozostałych bloków był drugi najmłodszy (patrzymy na ostatni bit struktury) i wpisujemy jego numer do bitów 3 i 4
3. Jeżeli poprzednio najstarszy blok, którego dokonaliśmy zastąpienia jest przed poprzednio najmłodszym blokiem (jest to ostatni pozostały blok) to na ostatni bit wpisujemy 1, wpp 0
