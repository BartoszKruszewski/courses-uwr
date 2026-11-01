# Zadanie 4

**Pojęcia:**
- **Kodowanie arytmetyczne:** zapis ciągu symboli jako liczby z `[0, 1)`. Każdy symbol zawęża przedział proporcjonalnie do swojego prawdopodobieństwa.
- **Dekodowanie arytmetyczne:** odwrotność, czyli zamiana liczby na ciąg symboli. Losowe bity dają wtedy próbkę z rozkładu.
- **Kwantyzacja:** zaokrąglenie prawdopodobieństw do liczb całkowitych, żeby obie strony miały dokładnie te same wartości.

**Pomysł:** model przy generowaniu potrzebuje losowych liczb. Podajemy mu zamiast nich zaszyfrowaną wiadomość. Tekst jest zwykły, ale wybór tokenów zależy od wiadomości.

**Nadawca:**
1. Szyfruje wiadomość i dodaje nagłówek z długością. Traktuje bity jako ułamek `x`, np. `101` to `x = 0.101₂ = 0.625`.
2. Dzieli `[0, 1)` według rozkładu modelu i bierze token, w którego przedział trafia `x`.
3. W tym przedziale dzieli dalej dla następnego tokenu i powtarza, aż zakoduje wszystkie bity.

Przykład dla prefiksu „Drodzy”:

| Token | Prawdopodobieństwo | Przedział |
|---|---|---|
| ` Towarzysze` | 0.5 | `[0, 0.5)` |
| ` Przyjaciele` | 0.25 | `[0.5, 0.75)` |
| ` Państwo` | 0.25 | `[0.75, 1)` |

`x = 0.625` wpada w drugi przedział, więc list zaczyna się od „Drodzy Przyjaciele”.

**Odbiorca:** ma ten sam model i prefiks, więc liczy te same przedziały. Czytając kolejne tokeny, zawęża przedział tak jak nadawca. Początkowe bity wspólne dla całego przedziału to wiadomość. Długość odczytuje z nagłówka.

**Dlaczego Naczelnik nic nie zauważy:** zaszyfrowane bity wyglądają losowo, więc `x` jest jak losowa liczba. Token o szansie `P` jest wtedy wybierany z szansą `P`, czyli dokładnie tak jak przy zwykłym generowaniu.

**Warunek:** obie strony muszą dostać identyczne rozkłady, stąd CPU i kwantyzacja.
