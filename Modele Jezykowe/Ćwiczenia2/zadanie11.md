# Zadanie 11

- **Igła w stogu siana (NIAH):** w długim tekście ukryto zdanie z liczbą, a model ma ją podać.
- **S-NIAH:** wariant z jedną igłą.
- **CWE:** podanie 10 najczęstszych słów z długiej listy.

## Poziom popularny

Badacze sprawdzili, jak modele AI radzą sobie z bardzo długimi tekstami w 26 językach. Polski wypadł najlepiej (88%), angielski był szósty (83,9%), chiński czwarty od końca (62,1%). Wynik dotyczy prostego wyszukiwania w długich tekstach, a nie rozmów z AI w ogóle.

## Poziom wyższy

**Benchmark:** ONERULER, 26 języków, kontekst 8K–128K tokenów, 5 wariantów szukania igły w stogu siana (NIAH) i 2 zadania liczenia częstych słów (CWE).

**Wyniki:**
- Luka między językami o dużych i małych zasobach rośnie z 11% (8K) do 34% (128K).
- Opcja „odpowiedz none” obniża wynik S-NIAH o 32% (o3-mini-high, angielski, 128K).
- CWE-hard: poniżej 1% dla wszystkich modeli.
- Język instrukcji zmienia wynik nawet o 20%.

**Ograniczenia:** zadania są syntetyczne, tokenizery liczą ten sam tekst bardzo różnie, a przewaga polskiego pozostaje niewyjaśniona.
