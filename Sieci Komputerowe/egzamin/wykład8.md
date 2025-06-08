# Notatka – HTTP (Warstwa aplikacji)

## 1. Budowa adresu URL (http)
Adres URL (Uniform Resource Locator) ma postać:
``schemat://nazwa_serwera[:port]/ścieżka``

Dla `http`:
- schemat: `http` lub `https`
- `//`: separator
- nazwa serwera (np. `example.com`)
- opcjonalnie `:port`
- identyfikator zasobu (np. `/strona/index.html`)

## 2. MIME – typ zawartości
Serwer ustawia typ MIME, aby przeglądarka wiedziała jak obsłużyć plik.
**Przykłady typów MIME:**
- `text/html` – strony internetowe
- `image/jpeg` – obrazki JPG
- `application/pdf` – pliki PDF
- `application/octet-stream` – surowe dane binarne

## 3. Pole `Host` w HTTP/1.1
Wskazuje, do jakiej domeny kierowane jest żądanie. Umożliwia hostowanie wielu stron na jednym adresie IP.

## 4. Pola nagłówka HTTP
- `Accept`: typy MIME akceptowane przez klienta
- `Accept-Language`: preferencje językowe
- `User-Agent`: informacje o przeglądarce/kliencie
- `Server`: dane o oprogramowaniu serwera
- `Content-Length`: długość treści odpowiedzi
- `Content-Type`: typ MIME zawartości odpowiedzi

## 5. Przechowywanie stanu w HTTP
HTTP jest bezstanowe. Stan przechowuje aplikacja, np. poprzez `Set-Cookie` z identyfikatorem sesji (`sID=...`), który klient potem odsyła w `Cookie`.

## 6. Warunkowe zapytanie GET
Używa nagłówka `If-Modified-Since`. Odpowiedź:
- `200 OK` – zmodyfikowano
- `304 Not Modified` – brak zmian

## 7. Kody odpowiedzi HTTP
- `1xx`: informacyjne
- `2xx`: sukces (`200 OK`)
- `3xx`: przekierowania (`301`, `302`)
- `4xx`: błąd klienta (`404 Not Found`)
- `5xx`: błąd serwera (`500 Internal Server Error`)

## 8. Połączenia trwałe w HTTP/1.1
Wiele żądań i odpowiedzi może być przesyłanych jednym połączeniem TCP. `Connection: close` – zamyka połączenie po odpowiedzi.

## 9. Cel metody POST
Umożliwia przesyłanie danych w treści żądania – np. formularzy i plików. Bezpieczniejsze niż GET (nie widać w URL).

## 10. REST (Representational State Transfer)
Styl tworzenia usług webowych wykorzystujący HTTP (metody GET, POST, PUT, DELETE). Umożliwia prostą, czytelną i zautomatyzowaną komunikację.

## 11. Serwery proxy – zastosowanie
Pośredniczą w żądaniach HTTP:
- mogą przechowywać dane w cache,
- zmniejszają obciążenie łącza,
- filtrują lub kontrolują dostęp.

## 12. Odwrotne proxy i CDN
- **Odwrotne proxy**: przed serwerem WWW, rozdzielają ruch.
- **CDN**: sieć serwerów blisko klientów, serwuje statyczne zasoby szybciej.

## 13. Skierowanie klienta do proxy
- Ustawienia przeglądarki lub sieci
- ISP może wymusić użycie proxy
- DNS może kierować na adres proxy

## 14. Nagłówki dodawane przez proxy
- `X-Forwarded-For`: IP klienta
- `Via`: IP proxy

## 15. Anonimowe serwery proxy
Nie dodają identyfikujących nagłówków. Zwykle płatne – zwiększają prywatność.

## 16. QUIC – nowy protokół
Zastępuje TCP + TLS dla HTTP/3:
- Bazuje na UDP
- Zawiera szyfrowanie (TLS 1.3)
- Mniejsza latencja (1 RTT)
- Odporny na opóźnienia jednego strumienia (multiplexing)
