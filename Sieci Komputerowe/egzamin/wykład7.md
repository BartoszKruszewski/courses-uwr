# Notatka z wykładu 7 – TCP

## Co to jest gniazdo?
Gniazdo (ang. socket) to interfejs komunikacyjny pomiędzy aplikacją a warstwą transportową, identyfikowany przez adres IP i numer portu. Pozwala na odbieranie i wysyłanie danych przez sieć.

## Czym różni się gniazdo nasłuchujące od gniazda połączonego? Czy w UDP są gniazda połączone?
- **Gniazdo nasłuchujące (serwera)** – służy tylko do przyjmowania połączeń, nie do przesyłania danych.
- **Gniazdo połączone** – tworzone po zestawieniu połączenia, służy do komunikacji.
- W UDP **nie ma gniazd połączonych**, każde gniazdo działa niezależnie i nie utrzymuje stanu połączenia.

## Co robią funkcje jądra:
- `bind()` – przypisuje gniazdu lokalny adres IP i port.
- `listen()` – przygotowuje gniazdo do nasłuchiwania połączeń (tworzy kolejkę).
- `accept()` – przyjmuje połączenie przychodzące z kolejki, tworząc gniazdo połączone.
- `connect()` – klient nawiązuje połączenie z serwerem.

## Czym różni się komunikacja bezpołączeniowa od połączeniowej?
- **Bezpołączeniowa (UDP)** – brak utrzymywanego stanu, każda wiadomość jest niezależna.
- **Połączeniowa (TCP)** – wymagane nawiązanie i zakończenie połączenia, przesył danych jest bardziej uporządkowany i niezawodny.

## Czym różni się otwarcie bierne od otwarcia aktywnego? Czy serwer może wykonać otwarcie aktywne?
- **Otwarcie bierne** – `listen()`, serwer oczekuje na połączenie.
- **Otwarcie aktywne** – `connect()`, klient inicjuje połączenie.
- Serwer **zwykle nie wykonuje otwarcia aktywnego**, ale technicznie jest to możliwe.

## Do czego służą flagi TCP: SYN, ACK, FIN, RST?
- **SYN** – synchronizacja, inicjuje połączenie.
- **ACK** – potwierdzenie odebrania danych.
- **FIN** – zakończenie połączenia.
- **RST** – reset połączenia w przypadku błędu.

## Trójstopniowe nawiązywanie połączenia TCP:
1. Klient wysyła `SYN`.
2. Serwer odpowiada `SYN-ACK`.
3. Klient wysyła `ACK`.
Każda strona ustala początkowy numer sekwencyjny (losowy).

## Dlaczego numeracja bajtów nie zaczyna się od zera?
Ponieważ początkowy numer sekwencyjny jest losowy – zwiększa bezpieczeństwo i zapobiega podszywaniu się.

## Jakie segmenty są wymieniane podczas zamykania połączenia w TCP?
1. Jedna strona wysyła `FIN`.
2. Druga odpowiada `ACK`.
3. Druga strona wysyła `FIN`.
4. Pierwsza odpowiada `ACK`.

## Co zwraca funkcja `recv()`?
- W trybie **blokującym**: czeka aż pojawią się dane, zwraca liczbę bajtów.
- W trybie **nieblokującym**: zwraca od razu, może zwrócić 0 (brak danych) lub -1 (błąd).

## Po co jest stan TIME_WAIT?
Pozwala upewnić się, że ostatni `ACK` dotarł oraz zapobiega pomyłkom przy szybkim otwarciu nowego połączenia z tymi samymi parametrami (IP + porty).

## Diagram stanów TCP – scenariusze:
- **Nawiązanie połączenia**: `CLOSED` → `SYN_SENT` (klient), `CLOSED` → `LISTEN` → `SYN_RECEIVED` (serwer) → `ESTABLISHED`.
- **Zamknięcie połączenia**: `ESTABLISHED` → `FIN_WAIT_1` → `FIN_WAIT_2` → `TIME_WAIT` → `CLOSED` (klient), `ESTABLISHED` → `CLOSE_WAIT` → `LAST_ACK` → `CLOSED` (serwer).
