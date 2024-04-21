#### Motywacja

Podstawowe predykatory lokalne nie uwzględniają zależności pomiędzy insturkcjami skoku w programie. Predykatory korelujące pamiętają historię skoków, gdzie czemu pozwalają na dokładniejsze szacowanie prawdopodobienśtwa skoku.

#### Przykład

```
(1) if (a == x) a = y
(2) if (b == x) b = y
(3) if (a != b) ...
```

Mamy takie przypadki:

- skoki (1) i (2) wykonają się, wtedy (3) się nie wykona
- skoki (1) lub (2) wykonają się, wtedy (3) się wykona
- skoki (1) i (2) nie wykonają się, wtedy (3) się nie wykona

Jak widać lokalny predykator skoków, ma losową szansę na wykonanie skoku poprawnie, co nie jest dobrą predykcją.

#### Budowa

Korelujące predykatory skoków, wykorzystują lokalne predykatory w połączeniu z rejestrem historii skoków. Całość jest połączona bramkami XOR. Taki układ wylicza hash, który zostaje użyty jako indeks tablicy predykcji.
