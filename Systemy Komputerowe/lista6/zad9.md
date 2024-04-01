Jeżeli chcielibyśmy wykonać instrukcję $swap x y$ w jednym cyklu procesora to musielibyśmy wykonać następujące działania:

- odczytanie wartości z rejestru $x$
- odczytanie wartości z rejestru $y$
- zapisanie wartości z rejestru $x$ do $y$
- zapisanie wartości z rejestru $y$ do $x$

W dotychczasowo omawianym modelu procesora **plik rejestrów** umożliwia odczytanie dwóch wartości w jednym cyklu, natomiast możemy wykonać zapis tylko do jednego rejestru.

Stąd modyfikacja jaką należałoby wykonać obejmowałaby **plik rejestrów** i dodanie wejść A4, WD4, WE4.

Dodatkowo nie musielibyśmy wykonywać żadnych operacji w ALU ani w pamięci danych, więc można połączyć wyjścia RD1 i RD2 odpowiednio z wejściami WD3, WD4. Na wejścia WE3 oraz WE4 trzeba skierować w **ControlUnit** wartość 1.

Całość powinna zachowywać kompatybilność wsteczną z innymi instrukcjami, więc dla wyjść RD1 i RD2 należałoby podłączyć stosowne multipleksery.
