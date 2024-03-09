Zasada działania:\
Jak w CLA dzrzewowym przechodzimy z liczeniem propagacji\
od prawego górnego rogu do lewego dolnego i wracamy.\
Róznicą są moduły A. Tutaj zastępujemy je sumatorami RCA.

Czas działania:\
k - ilosc bitów na jedno RCA\
log(n/k) + (przejscie w dół z liczeniem propagacji)\
log(n/k) + (przejscie w górę z liczeniem propagacji)\
k (czas działania ostatniego sumatora)\
= 2log(n/k) + k

Rozmiar:\
n (RCA) +\
n/k (bloki C) +\
log(n/k) (bloki B) +\ 
= n + n/k + log(n/k) 
