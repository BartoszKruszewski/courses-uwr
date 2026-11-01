# Zadanie 6

**Algorytm:** przed wyborem każdego tokenu:
1. Liczymy `hash(poprzedni token)` i używamy go jako ziarna generatora losowego.
2. Generator dzieli słownik na listę zieloną (ułamek γ, np. połowa) i czerwoną. Po tym samym tokenie podział jest zawsze taki sam.
3. Do logitów tokenów zielonych dodajemy `δ`, więc model częściej je wybiera.

Tekst mało na tym traci: gdy jeden token jest prawie pewny, wygra nawet jako czerwony, a gdy pasuje wiele tokenów, zwykle któryś jest zielony.

**Detekcja:** idziemy po tekście, dla każdego tokenu odtwarzamy podział z tokenu poprzedniego i sprawdzamy kolor. Dla `g` zielonych z `T` tokenów:

`z = (g − γT) / √(Tγ(1−γ))`

Duże `z` (np. powyżej 4) oznacza znak wodny.

**Dlaczego działa dla długich tekstów:** człowiek nie zna podziału, więc jego token jest zielony z szansą γ, jak w rzucie monetą. Model ma stale więcej zielonych, a przewaga rośnie szybciej niż szum (`z` rośnie jak `√T`). Przykład dla γ = 0.5 i 60% zielonych u modelu:

| `T` | Zielone | `z` | Wniosek |
|---|---|---|---|
| 25 | 15 | 1.0 | Mogło się zdarzyć przypadkiem |
| 1000 | 600 | 6.3 | Praktycznie niemożliwe przypadkiem |
