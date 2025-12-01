Zadanie 2 jest prawdziwe.

Załóżmy nie wprost, że istnieje protokół konsensusu używający obiektu `QuasiConsensus` dla 2 wątków.

Taki protokół musi mieć stan krytyczny.

BSO, jeśli wątek A wykona się jako pierwszy, to przejdziemy do stanu 0-walentnego, a jeśli B, to przejdziemy do stanu 1-walentnego.

Rozważmy przypadki:
- A i B proponują tę samą wartość 
    
    Funkcja `decide()` zwróci tą wartość.
    
    Wtedy nie ma znaczenia, który wątek wykonał się jako pierwszy.

    Otrzymujemy więc różne stany, a taką samą sytuację końcową - sprzeczność.

- A i B proponują różne wartości

    Funkcja `decide()` albo uzgodni wartość (analogiczna sytaucja do pierwszego przypadku) albo zwróci 1 dla A oraz 0 dla B.
    
    Stany będą identyczne, niezależnie od kolejności wykonania.
    
    Otrzymujemy więc różne stany, a taką samą sytuację końcową - sprzeczność.

`QuasiConsensus` nie ma poziomu konsensusu równego lub wyższego od 2, więc jest równy 1.
