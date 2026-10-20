# Zadanie 5

Generujemy po jednym tokenie i zatrzymujemy się na granicy wyrazu:
1. Pobierz kolejny token (sampling lub argmax) dla `prefiks + dotychczasowe tokeny`.
2. Jeśli to **pierwszy** token, wymuś, żeby zaczynał się od spacji i litery (tokeny bez spacji lub z interpunkcją maskujemy).
3. Jeśli kolejny token zaczyna się od **spacji/interpunkcji** albo jest EOS, **stop**: ten token odrzucamy, a wyraz jest gotowy.
4. Inaczej doklejamy token i wracamy do 1.

Efektywność: jedno wywołanie modelu na token z cache KV (`past_key_values`), bez generowania dalszego tekstu i bez przycinania po fakcie. Można też ustawić `max_new_tokens` z małym zapasem oraz stopping criterion „token zaczyna się od spacji”.
