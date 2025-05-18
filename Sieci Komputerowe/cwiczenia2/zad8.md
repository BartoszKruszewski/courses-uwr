Z definicji kodu Hamminga(7, 4)

Bity parzystości w pozycjach potęg dwójki: 1, 2, 4

Bity danych: 3, 5, 6, 7

| pozycja | 1  | 2  | 3  | 4  | 5  | 6  | 7  |
|---------|----|----|----|----|----|----|----|
| rola    | p1 | p2 | d1 | p3 | d2 | d3 | d4 |

Macierz kontroli parzystości

$H=\begin{bmatrix}
1 & 0 & 1 & 0 & 1 & 0 & 1\\
0 & 1 & 1 & 0 & 0 & 1 & 1\\
0 & 0 & 0 & 1 & 1 & 1 & 1
\end{bmatrix}$

Mnożąc macierz przez wektor bitowy otrzymanej ramki otrzymany binarny zapis pozycji przekłamanego bitu.

Minimalna odległość kodowa pomiędzy dwoma kodami (odległość Hamminga) to $3$ (3 niezależne bity parzystości), więc możemy skorygować do $(3-1)/2 = 1$ bitów.