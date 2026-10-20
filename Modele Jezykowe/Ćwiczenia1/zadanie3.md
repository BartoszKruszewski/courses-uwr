# Zadanie 3

**Idea:** podczas generacji dodajemy bonus +δ do logitów słów zaczynających się na C/S/K. Detekcja: liczymy odsetek takich słów i robimy test statystyczny względem częstości bazowej.

- **Długie teksty:** działa. Odchylenie rośnie jak √n, więc po kilkuset słowach wykrywanie jest pewne, a nadal jest niewidoczne dla człowieka.

- **Krótkie teksty:** nie działa. Przy kilku–kilkunastu słowach wariancja jest za duża i jest dużo fałszywych alarmów i pominięć.

**Problemy:**
- Reguła jest stała i jawna dla każdego
- Psuje jakość tekstu
