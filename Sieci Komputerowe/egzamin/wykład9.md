# Notatka z wykładu – Warstwa aplikacji cz. 2

## DNS

- **Cel systemu DNS**: Umożliwia tłumaczenie nazw domenowych (łatwych do zapamiętania dla ludzi) na adresy IP, niezależnie od zmian tych adresów.

- **Plik /etc/hosts**: Historyczny plik lokalny zawierający mapowanie nazw domen na adresy IP, używany zanim powstał DNS. Nadal obecny w systemach operacyjnych.

- **TLD (Top Level Domains)**: Domeny najwyższego poziomu, np. `.pl`, `.com`, `.edu`, `.uk`.

- **Strefy i delegacje DNS**:
  - *Strefa*: fragment drzewa domen, zarządzany przez określony serwer nazw.
  - *Delegacja*: wpis w nadrzędnej strefie wskazujący, który serwer obsługuje daną strefę.

- **Iteracyjne vs rekurencyjne odpytywanie DNS**:
  - *Iteracyjne*: klient sam odpytuje kolejne serwery.
  - *Rekurencyjne*: resolver DNS odpytuje kolejne serwery w imieniu klienta.

- **Odwrotny DNS**: Zamiana adresu IP na nazwę domeny, używa rekordu `PTR` oraz specjalnej domeny `in-addr.arpa`.

- **Typy rekordów DNS**:
  - `A` – IPv4
  - `AAAA` – IPv6
  - `NS` – wskazuje serwer nazw
  - `MX` – wskazuje serwer poczty
  - `CNAME` – alias innej domeny (kanoniczna nazwa)

## Poczta elektroniczna

- **SMTP vs IMAP**:
  - *SMTP* – protokół do wysyłania maili (port 25/587).
  - *IMAP* – protokół do pobierania i zarządzania mailami na serwerze.

- **Przekaźniki SMTP (relays)**: Serwery pośredniczące w przekazywaniu wiadomości między serwerami nadawcy i odbiorcy.

- **Rekord DNS sprawdzany przed wysłaniem poczty**: `MX` – wskazuje serwer odpowiedzialny za przyjmowanie poczty dla danej domeny.

- **Popularne pola nagłówka maila**:
  - `Received` – ślad trasy wiadomości przez serwery
  - `Bcc` – ukryta kopia wiadomości

- **Standard MIME**: Pozwala przesyłać różne typy danych (tekst, HTML, załączniki), definiuje m.in. `Content-Type`.

- **Spam i metody walki**:
  - Uczenie maszynowe, blokowanie IP, spowalnianie połączeń, SPF, podpisy cyfrowe

- **SPF**: Rekord TXT w DNS określający, które adresy IP mają prawo wysyłać pocztę w imieniu danej domeny.

## Sieci peer-to-peer (P2P)

- **Rola trackera w BitTorrent**: Utrzymuje listę użytkowników i udostępnia listę peerów chcących pobrać dany plik.

- **Funkcje skrótu w .torrent**: Pozwalają na weryfikację poprawności fragmentów pliku.

- **Seeder vs leecher**:
  - *Seeder* – posiada cały plik i udostępnia go innym.
  - *Leecher* – pobiera fragmenty, udostępniając przy tym innym te, które już ma.

## NAT i aplikacje

- **Połączenia odwrócone**: Gdy klient za NAT nie może odebrać połączenia, zewnętrzny serwer pośredniczy i klient inicjuje połączenie.

- **FTP i NAT**:
  - Tryb aktywny FTP nie działa za NAT.
  - Tryb pasywny FTP pozwala serwerowi inicjować połączenie odbioru danych, co działa za NAT.

- **NAT cone vs symetryczny**:
  - *Full cone NAT*: przekazuje pakiety z dowolnego źródła.
  - *Restricted cone NAT*: przekazuje tylko jeśli wcześniej nastąpiła komunikacja.
  - *Symetryczny NAT*: przypisania zależą od pary nadawca-odbiorca, przez co trudny do przejścia.

- **Hole punching**: Technika obejścia NAT polegająca na inicjacji połączenia do znanego portu z pomocą serwera pośredniczącego, pozwalająca na bezpośrednią komunikację.

