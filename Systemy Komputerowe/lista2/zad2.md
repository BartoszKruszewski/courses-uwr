Czas działania: \
3 * logn (poziomy wyliczania przeniesienia) +\
2 * 1 (górne dodawanie równolegle) +\
2 * 1 (dolne dodawanie równolegle)\
= 2logn + 4

Liczba bramek:\
$n \cdot logn - (1 + 2 + 4 +...+ 2^{n-1}) = (n-1) \cdot 2^n+1$ - (bramki przeniesień) +\
2 * n (górne bramki) +\
2 * n (dolne bramki)\
= 3logn + 4n