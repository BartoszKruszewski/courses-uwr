# Zadanie 9 (wybór permutacji wyrazów)

**Zachłannie:** budujemy zdanie słowo po słowie od lewej.
1. Zaczynamy od pustego prefiksu.
2. Dla każdego niewykorzystanego słowa liczymy P(prefiks + słowo) modelem językowym.
3. Doklejamy słowo o najwyższym prawdopodobieństwie.
4. Powtarzamy, aż wykorzystamy wszystkie słowa.

Koszt to ~n²/2 ocen zamiast n!, więc działa też dla długich tekstów.
