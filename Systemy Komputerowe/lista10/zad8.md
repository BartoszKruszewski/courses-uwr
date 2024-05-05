#### Analiza kodu

Przy mapowaniu bezpośrednim mamy tylko jeden blok na zbiór, więc mając bloki po 16 bajtów mamy 512/16 = 32 zbiory
Tablica ma 2 części po $128 \* 4$ (zmienna int ma $4$ bajty) bajtów, czyli po $32$ bloki.
Przy każdej iteracji pętli robimy odwołanie do bloków $i/4$ oraz $i/4 + 32$.

#### Przypadek 1

Przy pierwszym pobraniu bloku będzie **compulsory miss**, a potem **hit** do końca bloku, czyli $3$.
Miss rate: $1/4 = 25%$

#### Przypadek 2

Analogicznie jak w pierwszym przypadku. Wielkość pamięci nie wpłynie na działanie tego programu, ponieważ pamiętamy równolegle i je zastępujemy bez dodatkowej straty $2$ bloki. Dodanie pamięci zamienia nam **conflict miss** na **compulsory miss**. Różnica dla tego programu byłaby odczuwalna przy wielokości pamięci nie mogącej pomieścić dwóch bloków, czyli $<32$ bajtów.

#### Przypadek 3

Dla tego programu analogicznie, z przyczyn opisanych w przypadku 2.
Zwiększając rozmiar bloki moglibyśmy trafiać więcej kolejnych wartości, wiec miss rate zmniejszyłby się.
