#### Co powoduje wstrzymanie potoku?

Wstrzymanie potoku powodują instrukcje wykorzystujące pamięć danych, umieszone wcześniej niż jako 3 ostatnie instrukcje. Instrukcje te stanowią razem 36% całego programu, więc możemy założyć, że jedna z 3 ostatnich instrukcji będzie taką instrukcją. Jedna instrukcja zwiększa ilość wstrzymanych cykli o 1.

#### Obliczenia

Oznaczamy liczbę instrukcji jako $N$.
Liczba wstrzymanych cykli to $0.36N - 1$
