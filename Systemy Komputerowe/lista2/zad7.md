Działa jak układ z poprzedniej listy,\
ale dodatkowo zapamiętuje przeniesienia,\
oraz "zawraca" je do sumatora w kolejnym cyklu.

Jest to poprawne, poniewaz w kazdym cyklu\
robimy przesuniecie bitowe wyniku,\
a zapamietany bit wstawiamy na zwolnione miejsce.

Rozpoczynamy poprzez załadowanie sumy P i przeniesienia zerami.\
Wykonujemy pierwszą operację arytmetyczną.\
Przenosimy najmniej znaczący bit sumy P do A\
oraz przesuwamy rejestr A w celu zwolnienia miejsca na kolejny bit.\
Nie musimy przenosic n-1 pozostałych, ponieważ w kolejnej iteracji\
bity sumy są przeniesione do kolejnego addera.\ 
Dodawanie działa niezależnie od siebie, ponieważ nie przenosimy\
między nimi reszty. Zwiększa to znacznie prędkość procesu.

Po wykonaniu mnożenia, P to suma i przeniesienie.\
W celu otrzymania wyniku, dodajemy je.
