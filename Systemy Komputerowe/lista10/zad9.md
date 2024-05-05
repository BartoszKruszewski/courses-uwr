Mapowanie bezpośrednie oznacza, że każdy zbiór ma jeden blok.
Blok ma wielkość 8 bajtów, więc może pomieścić 8 zmiennych char, czyli dwie struct pixel.
Rozmiar pamieci to 32KB, natomiast rozmiat tablicy buffer to $480 * 640 * 4 = 1 228 800$ bajtów.

Zauważmy, że blok może efektywnie zadziałać dla 8 wartości char będących obok siebie.
W każdej iteracji pętli mamy 4 modyfikacje wartości, natomiast kolejne iteracje są mocno oddalone od siebie, ponieważ wewnętrzna pętla jest po i zamiast po j. 32KB pamięci pomieszczą $480 * 8 = 3840$ bajtów, więc co drugą iterację mamy 4 trafienia.
Łącznie na każde dwie iteracje mamy 1 **compulsory miss** (lub **conflict miss** jeżeli pamięć zapełni się) oraz 7 trafień.

Stąd miss rate: $1/8 = 12.5%$.
