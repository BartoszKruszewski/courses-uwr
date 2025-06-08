# Notatka z wykładu 5 – Niższe warstwy sieci komputerowych

## Zadania warstw
- **Warstwa łącza danych**: komunikacja między sąsiadującymi urządzeniami, wykrywanie błędów transmisji, zawodna usługa ramek.
- **Warstwa fizyczna**: przesyłanie bitów przez medium fizyczne (np. fale radiowe, światłowód, skrętka).

## Koncentrator vs przełącznik
- **Koncentrator (hub)**: przekazuje każdą ramkę do wszystkich portów, brak inteligencji.
- **Przełącznik (switch)**: uczy się adresów MAC i kieruje ramki tylko do odpowiedniego portu.

## Algorytmy ALOHA
- **Rundowy ALOHA**: czas podzielony na rundy, nadawanie z prawdopodobieństwem `p`.
- **Bezrundowy ALOHA**: brak synchronizacji, mniejsze wykorzystanie łącza.

## Algorytm odczekiwania wykładniczego
Po kolizji zwiększamy zakres odczekiwania: losowanie z przedziału `0..2^m - 1`, stosowane w Ethernet i WiFi.

## CSMA/CD vs CSMA/CA
- **CSMA/CD** (Ethernet): wykrywanie kolizji i przerywanie transmisji.
- **CSMA/CA** (WiFi): unikanie kolizji, brak możliwości ich wykrycia.

## Budowa ramki Ethernetowej
- Adres docelowy i źródłowy MAC, typ, dane (46-1500 B), suma kontrolna CRC.
- Minimalna długość ramki: 64 bajty (dla wykrywania kolizji).

## Adres MAC
- 6 bajtów, unikatowy identyfikator karty sieciowej, możliwy do zmiany.

## Tryb nasłuchu (promiscuous mode)
- Karta sieciowa przekazuje wszystkie ramki do systemu operacyjnego.

## Minimalna długość ramki w Ethernecie
- Zapewnia wykrycie kolizji zanim nadawanie zostanie zakończone.

## Protokół ARP i DHCP
- **ARP**: zamiana adresów IP na MAC.
- **DHCP**: dynamiczne przydzielanie adresu IP i innych parametrów sieci.

## Most vs router
- **Most**: działa na warstwie łącza danych, szybszy, nie obsługuje fragmentacji IP.
- **Router**: działa na warstwie sieci, obsługuje IP i routing.

## Rozgłaszanie w warstwie łącza danych
- Ramki wysyłane na MAC `FF:FF:FF:FF:FF:FF` trafiają do wszystkich urządzeń w domenie rozgłoszeniowej.

## Tryb uczenia się przełącznika
- Przełącznik zapamiętuje adresy MAC i porty, aby kierować ruch bez rozgłaszania.

## Algorytm drzewa spinającego (STP)
- Zapobiega cyklom w sieci poprzez tworzenie drzewa spinającego, używa go Ethernet.

## VLAN
- Logiczny podział sieci niezależnie od fizycznego połączenia. Ramki zawierają identyfikator VLAN.

## Zjawisko ukrytej stacji
- Komputer nie wykrywa transmisji innego komputera i powoduje kolizję w punkcie dostępowym.

## RTS i CTS
- **RTS (Request To Send)** i **CTS (Clear To Send)**: rezerwacja kanału w WiFi przed wysłaniem danych.
