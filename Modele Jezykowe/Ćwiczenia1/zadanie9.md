# Zadanie 9 (wybór permutacji wyrazów)

**Beam search po kolejności słów:** budujemy zdanie od lewej. W stanie mamy prefiks i pulę niewykorzystanych słów. Każdy stan rozszerzamy o każde pozostałe słowo, oceniamy przez log P(prefiks + słowo) z LM (KV cache, jedno wywołanie na stan, batchowanie kandydatów) i zostawiamy **k najlepszych**. Koszt to ~k·n² ocen zamiast n!.

Usprawnienia:
- pierwsze słowo z wielką literą, a słowo z kropką na końcu;
- na końcu ocena całego zdania z normalizacją długości;
- **długie teksty:** heurystyka lokalna. Startujemy z wyniku beam search, potem zamieniamy/przesuwamy pojedyncze słowa (hill climbing / simulated annealing), dopóki rośnie P(zdania). Ewentualnie najpierw dzielimy na fragmenty (frazy, interpunkcja), a potem układamy fragmenty.
