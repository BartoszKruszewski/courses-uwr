*rysunek został zmodyfikowany ręcznie w programie graficznym, nie jest to rysunek ze slajdów*

#### Intuicja

Jeżeli chcielibyśmy wykonać instrukcję $swap \; x \; y$ w jednym cyklu procesora to musielibyśmy wykonać następujące działania:

- odczytanie wartości z rejestru $x$
- odczytanie wartości z rejestru $y$
- zapisanie wartości z rejestru $x$ do $y$
- zapisanie wartości z rejestru $y$ do $x$

#### Problemy

W dotychczasowo omawianym modelu procesora **plik rejestrów** umożliwia odczytanie dwóch wartości w jednym cyklu, natomiast możemy wykonać zapis tylko do jednego rejestru.

Stąd modyfikacja jaką należałoby wykonać obejmowałaby **plik rejestrów** i dodanie wejść A4, WD4, WE4.

#### Modyfikacje procesora

- dodanie wejścia **A4**
- dodanie wejście **WD4** oraz **WE4**
- połączenie **A1** bezpośrednio z **A4** (**A4** jest używane tylko do ***SWAPA***)
- połączenie **RD1** bezpośrednio z **WD4** (**WD4** jest używane tylko do ***SWAPA***)
- dodanie multipleksera z wejścia z **RD2** oraz z wyjściem z wynikiem obliczeń dla **RD3**, który będzie wybierał wejście do **RD3** (dzięki temu zachowujemy kompatybilność z pozostałymi instrukcjami)

#### Ustawienia Control Unit

- ustawiamy **RegDst** na $0$, wtedy do **A3** trafi wartość z **A2**
- ustawiamy **WD3Src** na $1$, wetdy do **WD3** trafi wartość z **RD2**
- ustawiamy **WE4** na $1$, wtedy wartość z **WD4** zostanie zapisana do rejestru o adresie **A4**

#### Koszt

- $3$ dodatkowe wejśćia w **pliku rejestrów**
- $2$ dodatkowe wyjścia z **ControlUnit**
- $1$ dodatkowy multiplekser
- trochę dodatkowych ścieżek (mogą powodować problemy z rozmieszczeniem elementów i ostatecznie zwiększyć rozmiar procesora)