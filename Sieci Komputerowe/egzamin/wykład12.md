# Bezpieczeństwo sieci – Notatka z wykładu

## CAM i przepełnienie pamięci CAM
CAM (Content Addressable Memory) to pamięć przełącznika służąca do mapowania adresów MAC na porty. Przepełnienie CAM polega na wysyłaniu wielu ramek z losowymi adresami MAC, co powoduje, że przełącznik przechodzi w tryb „nasłuchu” (jak hub) i przesyła wszystkie ramki do wszystkich portów – umożliwia to podsłuchiwanie.

## Atak ARP Spoofing
Atakujący zatruwa pamięć ARP, wysyłając fałszywe odpowiedzi ARP z własnym adresem MAC przypisanym do IP innego hosta. W efekcie ruch sieciowy trafia do atakującego.

## IP Spoofing i Ingress Filtering
IP Spoofing polega na fałszowaniu adresu źródłowego IP. Ingress filtering to metoda weryfikacji poprawności pakietów – routery odrzucają pakiety przychodzące z niedozwolonymi adresami źródłowymi (spoza danego zakresu).

## RIP Spoofing
Atak polega na rozgłaszaniu fałszywych tras w protokole RIP, który w wersji 1 nie ma uwierzytelniania. Pozwala to przejąć ruch sieciowy.

## Zatruwanie cache DNS
Polega na wprowadzeniu fałszywych wpisów do pamięci cache resolvera DNS. Nowoczesne ataki wykorzystują wysyłanie wielu odpowiedzi UDP z różnymi ID, by trafić na prawidłowy identyfikator zapytania.

## Uwierzytelnianie serwera SSH
Klient przy pierwszym połączeniu otrzymuje klucz publiczny serwera i może zaakceptować jego odcisk palca (fingerprint). Klucz jest potem zapisywany lokalnie.

## Uwierzytelnianie użytkownika w SSH za pomocą RSA
Serwer zna klucz publiczny użytkownika. Użytkownik podpisuje dane kluczem prywatnym, a serwer weryfikuje podpis przy użyciu klucza publicznego.

## Tunelowanie – przykłady
- IPv6 przez IPv4
- OpenVPN/WireGuard: pakiety IP przez UDP
- SSH: przekierowanie portów (np. `ssh -L`)

## VPN
VPN (Virtual Private Network) to technologia łącząca zaufane sieci przez niezaufany Internet, zapewniająca tunelowanie i szyfrowanie transmisji.

## Porównanie filtrów pakietów
- **Proste** – szybkie, tylko nagłówki IP, mało precyzyjne.
- **Stanowe** – uwzględniają stan połączenia TCP.
- **Aplikacyjne** – analizują zawartość pakietów (np. FTP), wolniejsze, dokładniejsze.

## Moduły Netfilter/nftables
- **INPUT** – pakiety do lokalnego hosta.
- **OUTPUT** – pakiety wychodzące z lokalnego hosta.
- **FORWARD** – pakiety przechodzące przez host.

## NAT – łańcuchy
- **SNAT (źródłowy)** – w `POSTROUTING`.
- **DNAT (docelowy)** – w `PREROUTING`.

## Ataki przez brak weryfikacji danych
- **Przepełnienie bufora** – np. `scanf()` do zbyt małej tablicy.
- **Atak ../** – odczyt plików poza katalogiem WWW.
- **SQL injection** – np. `x' OR '1'='1`.
- **Heartbleed** – przesyłanie fragmentów RAM.

## Robak internetowy, botnet
- **Robak** – samopowielający się złośliwy kod.
- **Botnet** – sieć komputerów zainfekowanych przez robaka, sterowanych zdalnie.

## Phishing
Podszywanie się pod zaufaną stronę, by wyłudzić dane. Może mieć prawidłowy certyfikat HTTPS, ale domenę podobną do oryginału.

## Skanowanie portów
Technika wykrywania otwartych portów (np. `nmap`). Pozwala ocenić, jakie usługi są dostępne.

## Ataki DoS i DDoS
- **DoS** – blokowanie dostępu do usług (np. zalewanie pakietami ICMP).
- **DDoS** – atak z wielu komputerów (botnetu), trudniejszy do zablokowania.

## Atak odbity DoS (reflected)
Fałszowane zapytania do serwerów (np. DNS) z adresem ofiary jako źródłowym. Serwery odpowiadają na adres ofiary, co może ją przeciążyć. Wariantem jest **smurf attack** (ICMP na broadcast).
