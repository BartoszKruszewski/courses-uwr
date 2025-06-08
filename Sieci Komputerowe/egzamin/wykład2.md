# Notatka z wykładu 2 – Routing: Adresowanie

## Z czego wynika hierarchia adresów IP? Jaki ma wpływ na konstrukcję tablic routingu?
Hierarchia wynika z potrzeby uproszczenia trasowania – adresy IP mają wspólne prefiksy opisujące całe sieci. Dzięki temu router nie musi znać każdej trasy osobno, tylko reguły dla większych bloków adresów. Upraszcza to tablice routingu i przyspiesza decyzje trasowania.

## Notacja CIDR
CIDR (Classless Inter-Domain Routing) zapisuje zakresy adresów jako: `adres_ip/długość_prefiksu`, np. `156.17.4.32/28`. Pozwala elastycznie dzielić sieci, niezależnie od dawnych klas adresów.

## Co to jest adres rozgłoszeniowy?
To ostatni adres w sieci CIDR, używany do wysyłania pakietów do wszystkich urządzeń w tej sieci. Np. w `156.17.4.32/28` adresem rozgłoszeniowym jest `156.17.4.47`.

## Co to jest maska podsieci?
To długość prefiksu sieci określająca liczbę bitów opisujących sieć. Może być zapisana np. jako `/28` lub w postaci binarnej `255.255.255.240`.

## Opisz sieci IP klasy A, B i C.
Podział historyczny:
- Klasa A: adresy zaczynające się od `0`, maska `/8`
- Klasa B: zaczynają się od `10`, maska `/16`
- Klasa C: zaczynają się od `110`, maska `/24`

## Co to jest pętla lokalna (loopback)?
Sieć `127.0.0.0/8`, najczęściej `127.0.0.1`, używana do połączeń z lokalnym komputerem, np. testowania aplikacji sieciowych.

## Do czego służy pole TTL w pakiecie IP? Do czego służy pole protokół?
- **TTL (Time To Live):** ogranicza liczbę przeskoków pakietu. Każdy router zmniejsza TTL o 1. Gdy osiągnie 0, pakiet jest odrzucany.
- **Protokół:** informuje, jaki protokół znajduje się w danych pakietu (np. TCP=6, UDP=17, ICMP=1).

## Jakie reguły zawierają tablice routingu?
Reguły postaci: „jeśli adres zaczyna się od prefiksu X, wyślij pakiet do Y (interfejs/router)”.

## Na czym polega reguła najdłuższego pasującego prefiksu?
Gdy więcej niż jedna reguła pasuje do adresu, wybierana jest ta z najdłuższym (najbardziej szczegółowym) prefiksem.

## Co to jest trasa domyślna?
Reguła `0.0.0.0/0` – pasuje do każdego adresu. Używana, gdy brak innej, bardziej szczegółowej reguły.

## Do czego służy protokół ICMP? Jakie znasz typy komunikatów ICMP?
ICMP to pomocniczy protokół IP używany do diagnostyki (np. błędy, ping). Typy:
- 0 – Echo reply
- 3 – Destination unreachable
- 8 – Echo request
- 11 – Time exceeded

## Jak działa polecenie ping?
Wysyła ICMP echo request (typ 8). Odbiorca odsyła echo reply (typ 0), co pozwala zmierzyć czas odpowiedzi.

## Jak działa polecenie traceroute?
Wysyła pakiety z rosnącym TTL. Każdy router odsyła „Time Exceeded” (typ 11). Pozwala ustalić trasę do celu.

## Dlaczego do tworzenia gniazd surowych wymagane są uprawnienia administratora?
Gniazda surowe dają dostęp do niskopoziomowych pakietów (np. ICMP), co może być wykorzystywane do ataków sieciowych – dlatego wymagane są uprawnienia roota.

## Co to jest sieciowa kolejność bajtów?
To „big endian” – najpierw najbardziej znaczący bajt. Wszystkie liczby w nagłówkach IP muszą być w tej kolejności. Do konwersji służą `htons`, `htonl`, `ntohs`, `ntohl`.

## Co robią funkcje socket(), recvfrom() i sendto()?
- `socket()` – tworzy gniazdo
- `recvfrom()` – odbiera pakiet z gniazda
- `sendto()` – wysyła pakiet przez gniazdo

## Jakie informacje zawiera struktura adresowa sockaddr_in?
- Typ rodziny adresowej (`AF_INET`)
- Port (`sin_port`)
- Adres IP (`sin_addr`)
- Pole na zera

## Co to jest tryb blokujący i nieblokujący? Co to jest aktywne czekanie?
- **Blokujący:** `recvfrom()` czeka na pakiet.
- **Nieblokujący:** `recvfrom()` zwraca od razu, nawet jeśli nie ma pakietu.
- **Aktywne czekanie:** ciągłe wywoływanie `recvfrom()` w pętli – zużywa 100% CPU.

## Jakie jest działanie funkcji select()?
Funkcja `select()` (lub `poll()`) pozwala monitorować wiele deskryptorów (np. gniazd) i czekać na gotowość do odczytu bez aktywnego czekania.
