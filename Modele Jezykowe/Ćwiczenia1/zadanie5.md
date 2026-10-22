# Zadanie 5

Generujemy po jednym tokenie i zatrzymujemy się na granicy wyrazu:
1. Pobierz kolejny token.
2. Jeśli kolejny token zaczyna się od **spacji/interpunkcji** albo jest EOS, **stop**: ten token odrzucamy, a wyraz jest gotowy.
3. Inaczej doklejamy token i wracamy do 1.
