# Zadanie 9

**Cechy:** 4 wersy po 8 sylab, rymy AABB, proste słowa.

**Algorytm:** beam search z kilkoma wierszykami w prefiksie.
- Wers 1 i 3: maska usuwa tokeny przekraczające 8 sylab.
- Wers 2 i 4: wybieramy najbardziej prawdopodobne słowa rymujące się (słownik końcówek) i wypełniamy początek do 8 sylab.
- Na końcu wybieramy wierszyk o najlepszym średnim log-prob.
