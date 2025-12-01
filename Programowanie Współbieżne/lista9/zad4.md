#### Licznik z zamkiem TTAS

Każdy wątek wykonuje inwalidację cache'u przy inkrementacji licznika.

Wątki czekające na warunek `licznik == n` są wielokrotnie zmuszane do odświeżania swojej linii cache po każdej zmianie licznika przez inny wątek.

Tragiczna dla dużego $n$.

#### Bariera tablicowa

Lokalne wirowanie: W fazie 1 każdy wątek czeka na swoją prywatną zmienną b[i-1].

Ustawienie jej przez poprzednika powoduje ruch tylko między dwoma procesorami, nie angażując całej magistrali.

Sygnał przechodzi szeregowo przez łańcuch wątków, co przy bardzo dużym $n$ może trwać dłużej niż równoległa aktualizacja licznika (ale nie zapycha magistrali).

#### Podsumowanie

Wariant tablicowy oszczędza przepustowość szyny, co w systemach wieloprocesorowych jest kluczowe dla ogólnej wydajności systemu.

Dla systemu z $n$ wątkami i wspólną szyną danych, implementacja tablicowa jest znacznie lepsza, pod warunkiem zastosowania paddingu.
