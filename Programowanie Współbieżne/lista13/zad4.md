#### Dlaczego `precombine()` i `combine()` czekają na `locked == false`?

Aby nie wchodzić w drogę wątkom, które właśnie przetwarzają poprzednią falę operacji. Nowe wątki muszą czekać, aż węzeł będzie "czysty" i gotowy na nową parę.
​
#### Dlaczego `op()` i `distribute()` nie czekają?

Ponieważ wykonują je wątki, które już "trzymają" ten węzeł. To one są odpowiedzialne za trwającą operację, więc nie muszą czekać na samych siebie.
​
#### Wpływ przypisania locked na inne wątki:

- Włączenie (true) w precombine/combine: Blokuje wejście dla "spóźnialskich" wątków z dołu, zmuszając je do czekania w kolejce na następny cykl.
​
- Wyłączenie (false) w op/distribute: Sygnał "koniec pracy" – budzi czekającego partnera (wątek pasywny) lub otwiera węzeł dla zupełnie nowych wątków.
​