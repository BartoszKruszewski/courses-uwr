## 1. Dlaczego router ma więcej niż jeden adres IP?

☐ Jeden adres IP jest zawsze zarezerwowany do wysyłania pakietów do bramy domyślnej  
☐ Do każdego wpisu w tablicy routingu konieczny jest osobny adres IP  
☐ Jeden adres służy tylko do przyjmowania pakietów a drugi tylko do ich wysyłania  
☑ Każdy z interfejsów sieciowych routera jest zazwyczaj w odrębnej sieci i tym interfejsom przypisane są adresy z tych sieci  

## 2. Tylko jedna poprawna odpowiedź

☐ Zignoruje tę informację, gdyż jego obecna trasa jest lepsza  
☑ Zaktualizuje swój wpis, zmieniając odległość do routera X na 6  
☐ Zaktualizuje swój wpis, zmieniając odległość do routera X na 8  
☐ Powyższa informacja nie dotrze do A ze względu na mechanizm zatruwania ścieżek  

## 3. Zaznacz prawdziwe zdania o sumach kontrolnych i kodach

☑ Jeśli odległość Hamminga między dowolną parą kodów wynosi co najmniej 4, to takie kodowanie potrafi wykryć 3 błędy pojedynczych bitów  
☑ Sumy kontrolne CRC stosowane są w warstwie łącza danych  
☐ Kody MAC stosowane są do korekcji błędów transmisji  
☐ Jeśli odległość Hamminga między dowolną parą kodów wynosi co najmniej 4, to takie kodowanie potrafi skorygować 2 błędy pojedynczych bitów  

## 4. Zaznacz prawdziwe zdania

☑ Mechanizm Go-Back-N jest szczególnym przypadkiem ogólnego mechanizmu okna przesuwnego, w którym okno odbiorcy jest równe 1.  
☐ Mechanizm Stop-And-Wait jest szczególnym przypadkiem ogólnego mechanizmu okna przesuwnego, w którym okno odbiorcy jest równe 1.  
☑ Mechanizm Stop-And-Wait jest szczególnym przypadkiem ogólnego mechanizmu okna przesuwnego, w którym okno nadawcy jest równe 1.  
☐ Mechanizm Go-Back-N jest szczególnym przypadkiem ogólnego mechanizmu okna przesuwnego, w którym okno nadawcy jest równe 1.  

## 5. Ustawienia po `ip addr add 10.1.1.15/24 dev enp0s0`

☐ Brama domyślna zostanie ustawiona na 10.0.0.1  
☐ Brama domyślna zostanie ustawiona na 10.1.1.1  
☑ Adres rozgłoszeniowy zostanie ustawiony na 10.1.1.255  
☐ Adres rozgłoszeniowy zostanie ustawiony na 10.255.255.255  

## 6. Tylko jedna poprawna odpowiedź (ping w sieci lokalnej)

☑ Nagłówek ramki, nagłówek pakietu IP, nagłówek ICMP, dane ICMP, suma kontrolna CRC  
☐ Nagłówek ramki, nagłówek ICMP, dane ICMP, suma kontrolna CRC  
☐ Nagłówek ramki, nagłówek pakietu IP, dane ICMP, suma kontrolna CRC  
☐ Nagłówek ramki, suma kontrolna CRC, nagłówek pakietu IP, nagłówek ICMP  

## 7. Prawdziwe zdania o TCP

☑ Wykorzystuje algorytm okna przesuwnego  
☐ Otrzymuje strumień danych z warstwy sieciowej i dzieli go na segmenty  
☐ Potrafi dokonywać konwersji pomiędzy różnymi formatami plików  
☑ Umożliwia kontrolę przepływu  

## 8. Na podstawie jakich informacji TCP wybiera gniazdo?

☑ Lokalny port  
☑ Zdalny adres IP  
☐ MTU  
☐ Rozmiar okna  

## 9. Jaka maska podsieci umożliwi wykorzystanie dokładnie 510 adresów IP do adresowania komputerów

☑ 255.255.254.0  
☐ 255.255.252.0  
☐ 255.255.255.0  
☐ 255.255.254.0  

## 10. HTTP – które zdania są prawdziwe?

☐ Wykorzystuje protokół UDP  
☐ Typem MIME dla wysyłanej strony HTML jest `text/plain`  
☑ Serwer korzysta z portu 80  
☐ Pliki do serwera można wysyłać korzystając z metody GET  

## 11. NAT i prywatny adres IP

☑ Router **może być ograniczonym asymetrycznym** (restricted cone) NAT  
☑ Router **może być asymetrycznym ograniczonym portowo** (port-restricted cone) NAT  
☐ Router **może być pełnym asymetrycznym** (full cone) NAT  
☐ Router **może być symetrycznym** NAT  

## 12. Sieci bezprzewodowe 802.11

☑ Dostęp do kanału opiera się na mechanizmie odczekiwania wykładniczego  
☑ Protokół wykorzystuje przeskakiwanie częstotliwości (frequency hopping)  
☐ Jeśli nie słyszymy transmisji, to rozpoczęcie nadawania nie spowoduje interferencji u odbiorcy  
☐ Dostęp do kanału opiera się na wykrywaniu kolizji  

## 13. Protokół UDP – prawdziwe zdania

☑ Otrzymuje strumień danych z warstwy aplikacji i dzieli go na datagramy  
☐ Wysyłane datagramy są potwierdzane  
☐ Wysyłane datagramy zawierają w nagłówku UDP numer sekwencyjny  
☑ Jest protokołem bezpołączeniowym  

## 14. Protokół IP – które zdania są prawdziwe?

☑ Nagłówek protokołu IP zawiera adres MAC karty odbiorcy  
☑ Pakiety IP są enkapsulowane w ramkach warstwy łącza danych  
☐ Umożliwia kontrolę przeciążenia  
☐ Jest połączeniowy  

## 15. Tylko jedna poprawna odpowiedź (HTTP pakiet się gubi)

☐ Przeglądarka WWW wyśle zapytanie ARP  
☐ Przeglądarka WWW ponownie wyśle pakiet  
☑ Warstwa transportowa ponownie wyśle pakiet  
☐ Serwer WWW wyśle żądanie o ponowne przesłanie pakietu  

## 16. Zaznacz prawdziwe zdania

☑ 44.0.0.44/30 jest adresem przypisywanym komputerowi  
☐ 127.127.127.127/25 jest adresem rozgłoszeniowym  
☐ 192.168.1.0/8 jest adresem sieci  
☑ 10.10.10.0/24 jest adresem sieci  

## 17. Czy podany adres może być adresem rozgłoszeniowym?

☐ 192.168.15.223  
☐ 192.168.15.131  
☑ 192.168.15.135  
☐ 192.168.15.255  

## 18. Które zdania dotyczące `traceroute` są prawdziwe?

☑ Traceroute wysyła kolejne pakiety o coraz mniejszych wartościach pola TTL  
☐ Traceroute służy do przypisywania adresów IP  
☐ Traceroute opiera się na technice wykrywania MTU dla ścieżki  
☑ Przy TTL=0 router pośredni odsyła komunikat echo reply  

## 19. Efekt wywołania funkcji `connect()` na gnieździe TCP

☐ Dozwolone tylko w przypadku gniazd UDP  
☐ Wysłanie segmentu z bitem ACK  
☑ Wysłanie segmentu z bitami SYN i ACK  
☐ Wysłanie segmentu z bitem SYN  

## 20. Adres IP 10.0.0.256/23, brama domyślna 10.0.1.0

☑ Komputer będzie mógł komunikować się ze wszystkimi adresami IP z podsieci 10.0.0.0/8  
☐ Komputer nie będzie mógł się komunikować z bramą, bo leży poza podsiecią  
☐ Adres IP jest błędny, gdyż jest adresem rozgłoszeniowym  
☐ Adres IP jest błędny, gdyż jest adresem sieci  

## 21. Techniki routingu dynamicznego zapobiegające cyklom

☐ Certyfikaty SSL  
☑ Wysyłanie informacji o zmianie topologii  
☐ Wykrywanie MTU  
☑ Zatruwanie ścieżki  

## 22. Kontrola przeciążenia w TCP

☐ Wymaga komunikatów od routerów  
☐ Zakłada, że pakiety giną z powodu przepełnienia kolejek  
☑ Zakłada, że pakiety giną przez błędy warstwy fizycznej  
☐ Preferuje transmisję o wyższym czasie RTT  

## 23. Zaznacz prawdziwe zdania

☑ BitTorrent służy do przesyłania plików  
☑ HTTP służy do pobierania stron WWW  
☑ POP3 służy do wysyłania poczty z serwera do klienta  
☐ SMTP służy do pobierania poczty z serwera  

## 24. Suma CRC – które zdania są prawdziwe?

☐ Dowolna zmiana pojedynczego bitu zostanie wykryta  
☑ Do wiadomości zostały dołączone 5 bity sumy kontrolnej  
☐ Dołączono 6 bitów sumy kontrolnej  
☑ Zmiana dwóch dowolnych bitów zostanie wykryta  

## 25. Które zdania dotyczące szyfrowania są prawdziwe?

☐ RSA jest szyfrem monoalfabetycznym  
☑ Algorytmy asymetryczne są wolniejsze niż symetryczne  
☑ One-time pad jest szyfrem monoalfabetycznym  
☑ W szyfrowaniu symetrycznym używamy tego samego klucza  

## 26. Adres 123.5.66.63 – adres rozgłoszeniowy dla maski:

☐ /26  
☐ /24  
☐ /25  
☑ /28  

## 27. W jakich warstwach są używane poniższe mechanizmy?

☑ Nawiązywanie połączenia – warstwa transportowa  
☐ Typ MIME – warstwa sieciowa  
☐ Kontrola przepływu – warstwa sieciowa  
☑ Routing – warstwa łącza danych  

## 28. Informacje w nagłówku TCP

☑ Rozmiar okna nadawczego  
☐ Rozmiar okna odbiorczego  
☑ Port nadawcy  
☑ Numer sekwencyjny  

## 29. Maska podsieci /26 – który adres można przypisać?

☐ 10.3.1.191  
☐ 192.23.1.192  
☑ 10.23.1.32  
☐ 172.13.160.1  

## 30. Tylko jedna poprawna odpowiedź (polecenie wyświetlające routery)

☑ traceroute 10.20.30.40  
☐ ping 10.20.30.40  
☐ ip route 10.20.30.40  
☐ ip link 10.20.30.40  

## 31. Czas transmisji pakietu 500 bajtów przez łącze 1 Mbit, opóźnienie propagacji 2 ms

☐ 2.5 ms  
☐ 4 ms  
☐ 18 ms  
☑ 6 ms  

## 32. Protokół DNS – które zdania są prawdziwe?

☐ DNS służy tylko do zamiany nazw domen na adresy IP  
☑ Jedna domena może mieć przypisanych wiele adresów IP  
☑ Rekord NS umożliwia określenie serwera nazw odpowiedzialnego za daną domenę  
☑ Strefa to zbiór nazw domen  

## 33. Typowa kryptografia asymetryczna

☑ Łatwo złamać klucz, jeśli znamy parę tekst jawny + szyfrogram  
☐ Szyfrujemy kluczem publicznym odbiorcy  
☑ Szyfrujemy wiadomość kluczem prywatnym nadawcy  
☐ Szyfrujemy wiadomość kluczem prywatnym odbiorcy  

## 34. Prawdziwe zdania o systemach autonomicznych

☑ BGP jest protokołem stanu łącza  
☑ OSPF jest protokołem routingu wewnątrz AS  
☑ RIP jest protokołem do routingu między AS-ami  
☐ Każdy system autonomiczny musi mieć co najmniej dwa połączenia  

## 35. Tablica routingu – ile wpisów wystarczy?

☑ Możliwe jest skonstruowanie równoważnej tablicy zawierającej 4 wpisy  
☐ Możliwe jest skonstruowanie równoważnej tablicy zawierającej 7 wpisów  
☐ Możliwe jest skonstruowanie równoważnej tablicy zawierającej 3 wpisy  
☐ Możliwe jest skonstruowanie równoważnej tablicy zawierającej 2 wpisy  

## 36. TCP – połączenie A z B

☑ Komputer A może wysłać dane już po otrzymaniu segmentu z bitem ACK  
☐ Komputer A zaczyna od wysłania segmentu z bitem SYN  
☐ Komputer B może wysłać dane już po otrzymaniu segmentu z bitem RST  
☐ Komputer A wysyła dane dopiero po odebraniu danych od B  

## 37. Co poprawia wydajność HTTP?

☐ Zapytania ARP  
☐ Sender Policy Framework (SPF)  
☑ Sieci CDN  
☑ Połączenia trwałe (wiele komunikatów HTTP w jednym połączeniu TCP)  

## 38. Prawdziwe zdania o CSMA/CD

☐ Jest wykorzystywany w sieciach bezprzewodowych  
☐ Wymaga potwierdzania ramek  
☑ Jeśli wielu nadawców – większe szanse ma ten, który właśnie nadawał  
☑ Wykorzystuje algorytm odczekiwania wykładniczego  

## 39. Zaznacz prawdziwe zdania

☑ W sieci 192.168.0.0/26 dokładnie 60 adresów IP można przypisać komputerom  
☑ W sieci 192.168.0.0/24 dokładnie 126 adresów IP można przypisać komputerom  
☑ W sieci 192.168.0.0/28 dokładnie 16 adresów IP można przypisać komputerom  
☐ W sieci 192.168.0.0/29 dokładnie 6 adresów IP można przypisać komputerom  

## 40. Tylko jedna poprawna odpowiedź (CSMA/CD – maks. odległość)

☑ 40 m  
☐ 800 m  
☐ 400 m  
☐ 160 m  
