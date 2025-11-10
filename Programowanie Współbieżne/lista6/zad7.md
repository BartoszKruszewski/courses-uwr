#### Konstrukcja

Używamy `n x n` rejestrów SRSW atomowych m-value dla `n` czytelników.

Pisarz ustawia (tak jak w SRSW) najpierw wartość potem timestamp, natomiast robi to "po przekątnej", dla każdego czytelnika aktualizując jeden jego rejestr.

Czytelnicy po otrzymaniu wartości z nowym timestampem propagują ją do pozostałych czytelników (każdy czytelnik ma n rejestrów po jednym na każdego innego czytelnika).

Czytelnik uznaje wartość za aktualną dopiero wtedy kiedy wszystkie timestampy są zgodne, jeżeli nie to uznaje poprzednią wartość.

#### Poprawność

Zauważmy, że punkt linearyzacji dla danego czytelnika występuje dopiero po otrzymaniu propagacji od każdego innego czytelnika.

Oznacza to, że wcześniej każdy inny czytelnik musiał otrzymać wartość, którą propaguje od pisarza.

Jeżeli pisarz zapisał wartość dla każdego czytelnika to znaczy, że zakończył pełny zapis, który jest jego punktem linearyzacji.

Czyli nowy odczyt dla każdego czytlenika zawsze wystąpi po zakończeniu zapisu przez pisarza.