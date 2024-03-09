Sumator prefiksowy wylicza przeniesienia w czasie logarytmicznym,\
a poźniej oblicz równolegle wartości sumowania dla wszystkich bitów.

Czas działania: \
2 * logn (poziomy wyliczania przeniesienia) +\
1 * 1 (górne dodawanie równolegle) +\
2 * 1 (dolne dodawanie równolegle)\
= 2logn + 3

Liczba bramek:\
3 * logn (bramki przeniesień) +\
2 * n (górne bramki) +\
2 * n (dolne bramki)\
= 3logn + 4n