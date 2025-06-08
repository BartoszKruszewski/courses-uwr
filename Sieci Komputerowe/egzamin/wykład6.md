# Notatka z wykładu 6 – Transport (podstawy)

## 1. Co może stać się z przesyłanym ciągiem pakietów IP?
W przypadku zawodnego transportu (UDP) pakiety mogą zostać: uszkodzone, zgubione, opóźnione, przyjść w złej kolejności lub zostać zduplikowane. Niezawodny transport (TCP) wykrywa i naprawia te błędy.

## 2. Co to jest kontrola przepływu?
Mechanizm zapobiegający zalewaniu odbiorcy danymi, na które nie ma miejsca w buforze. Odbiorca wysyła tzw. okno oferowane (wolne miejsce), a nadawca dostosowuje szybkość transmisji.

## 3. UDP vs TCP + zastosowania
**UDP:** szybki, zawodny – np. DNS, DHCP, gry.  
**TCP:** wolniejszy, niezawodny – np. HTTP(S), transmisje danych.

## 4. Co to segmentacja i MSS?
Segmentacja to dzielenie danych na mniejsze jednostki.  
MSS (Maximum Segment Size) = MTU - nagłówki IP i TCP.  
Segmenty mają ograniczoną wielkość z powodu ryzyka błędów i ograniczeń sieci.

## 5. Jednostki danych w warstwach:
- Aplikacji: dane
- Transportowej: segmenty (TCP) / datagramy (UDP)
- Sieciowej: pakiety
- Łącza danych: ramki

## 6. Jak małe pakiety zmniejszają opóźnienie?
Małe pakiety szybciej przechodzą przez routery i są łatwiejsze do umieszczenia w kolejce.

## 7. RTT i RTO
**RTT** – czas przelotu tam i z powrotem.  
**RTO** – czas oczekiwania na ACK, po którym następuje retransmisja.  
RTO = 2×avg_RTT + 4×var_RTT

## 8. Jak wykrywane są duplikaty?
Za pomocą numerów sekwencyjnych. Duplikaty są ignorowane lub potwierdzane ponownie.

## 9. Stop-and-Wait – opis
Nadawca czeka na ACK po każdym segmencie.  
**Zalety:** prostota.  
**Wady:** niska wydajność na dużych opóźnieniach (niewykorzystane łącze).

## 10. Numery sekwencyjne – do czego służą?
Numerują segmenty/bajty, umożliwiają wykrycie brakujących lub duplikatów i ich uporządkowanie.

## 11. Algorytm okna przesuwnego
Nadawca może wysłać kilka segmentów bez oczekiwania na ACK. Po odebraniu ACK okno przesuwa się dalej.

## 12. Rozmiar okna a BDP
BDP (bandwidth-delay product) = przepustowość × opóźnienie. Okno powinno być co najmniej tej wielkości, aby w pełni wykorzystać łącze.

## 13. Porównanie mechanizmów potwierdzania:
- **Go-Back-N:** ACK tylko dla ostatniego poprawnego segmentu, brak bufora, retransmisje wielu segmentów.
- **Selektywne:** ACK dla każdego segmentu, buforowanie, retransmisja tylko brakujących.
- **Skumulowane:** ACK dla największego ciągłego segmentu, możliwość opóźniania ACK.

## 14. Dlaczego istotne są ACK duplikatów?
Pozwala nadawcy odróżnić brak ACK od jego utraty i uniknąć niepotrzebnych retransmisji.

## 15. Okno oferowane
Okno oznacza ile miejsca ma odbiorca. Wysyłane nadawcy, który dostosowuje transmisję.

## 16. TCP – mechanizmy niezawodności i kontroli:
- retransmisje, timeouty, numery sekwencyjne, potwierdzenia (ACK),
- kontrola przepływu za pomocą okna oferowanego.

## 17. Opóźnione ACK w TCP
ACK nie jest wysyłane natychmiast – czeka się chwilę lub do wysłania danych w drugą stronę.

## 18. Mechanizm Nagle’a
Zbiera małe dane i wysyła większy pakiet – ogranicza liczbę małych pakietów. Nie stosować w aplikacjach interaktywnych.

## 19. Pola w nagłówku TCP:
- **Numer sekwencyjny** – numer pierwszego bajtu.
- **Numer potwierdzenia (ACK)** – numer kolejnego oczekiwanego bajtu.

## 20. Czy warstwa transportowa jest na routerach?
Nie. Transport działa tylko na końcach (hostach), routery operują na warstwie sieciowej.

## 21. Zasada end-to-end:
- **Słaba wersja:** niższe warstwy mogą pomagać.
- **Silna wersja:** niezawodność zapewniana tylko na końcach – routery nie ingerują.
