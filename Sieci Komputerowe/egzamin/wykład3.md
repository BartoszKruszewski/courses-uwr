# Routing – tworzenie tablic

## Co to jest cykl w routingu? Co go powoduje?
Cykl w routingu to sytuacja, gdy pakiet krąży w sieci bez końca między routerami. Powodowany jest przez niespójne lub błędne tablice routingu – np. gdy routery nie wiedzą o awarii łącza i aktualizują się wzajemnie, tworząc błędne trasy.

## Czym różni się tablica routingu od tablicy przekazywania?
- **Tablica routingu** zawiera wszystkie znane trasy, także zapasowe.
- **Tablica przekazywania (forwarding table)** zawiera tylko informacje potrzebne do podjęcia decyzji o przesłaniu pakietu – zawiera najdłużej pasujący prefiks i wskazanie następnego hopu.

## Dlaczego w algorytmach routingu dynamicznego obliczamy najkrótsze ścieżki?
Aby zminimalizować opóźnienie, koszt lub liczbę przeskoków – zależnie od wybranej metryki. Unika to cykli i pozwala efektywnie wykorzystywać sieć.

## Co to jest metryka? Jakie metryki mają sens?
Metryka to wartość przypisana krawędziom sieci używana do wyznaczania najkrótszych ścieżek. Przykłady:
- czas propagacji,
- koszt finansowy,
- liczba przeskoków (hops).

## Czym różnią się algorytmy wektora odległości od algorytmów stanów łączy?
- **Stanów łączy**: każdy router informuje wszystkich o swoich sąsiadach i sam oblicza ścieżki.
- **Wektora odległości**: routery wymieniają się informacjami tylko z sąsiadami, aktualizując tablice na podstawie ich wektorów.

## Jak router może stwierdzić, że bezpośrednio podłączona sieć jest nieosiągalna?
Poprzez brak odpowiedzi lub brak komunikatów od sąsiada przez określony czas (np. brak Hello przez 30s). Wtedy ustawia odległość do tej sieci na ∞.

## Co to znaczy, że stan tablic routingu jest stabilny?
Oznacza, że kolejne wymiany informacji nie powodują już zmian w tablicach – sieć zbiega się do stanu spójnego.

## Jak zalewać sieć informacją? Co to są komunikaty LSA?
- **Zalewanie**: router wysyła informację do wszystkich sąsiadów, którzy przesyłają ją dalej (z pominięciem źródła).
- **LSA (Link State Advertisement)**: komunikat opisujący stan łącza – zawiera źródło, numer sekwencyjny i jest podstawą działania OSPF.

## Co wchodzi w skład wektora odległości?
Wektor odległości zawiera:
- odległość do znanych sieci,
- informację o następnym routerze (hopie) do celu.

## W jaki sposób może powstać cykl w routingu?
Gdy routery aktualizują się nawzajem na podstawie błędnych informacji (np. po awarii łącza) – powstaje błędne przekonanie, że ścieżka istnieje przez sąsiada, który używa nas jako trasy.

## Co to jest problem zliczania do nieskończoności? Kiedy występuje?
Występuje w wektorze odległości, gdy routery błędnie zwiększają wartość odległości do nieosiągalnej sieci w każdej turze – powoduje to opóźnione wykrycie problemu.

## Na czym polega technika zatruwania ścieżki zwrotnej (poison reverse)?
Router, który używa danego sąsiada jako trasy do celu, wysyła temu sąsiadowi informację, że ma do celu odległość ∞, aby zapobiec błędnej aktualizacji.

## Po co w algorytmach wektora odległości definiuje się największą odległość (np. 16 w RIP)?
Aby przerwać zliczanie do nieskończoności – po osiągnięciu tej wartości sieć jest uznawana za nieosiągalną.

## Po co stosuje się przyspieszone uaktualnienia?
Aby szybciej propagować informacje o zmianach w sieci (np. awariach), bez czekania na standardowy interwał aktualizacji.

## Co to jest system autonomiczny (AS)? Jakie znasz typy AS?
AS to zbiór routerów zarządzanych przez jednego operatora z jednolitą polityką routingu. Typy:
- z jednym wyjściem,
- nietranzytowy (wiele wyjść, nie przekazuje ruchu),
- tranzytowy (przekazuje ruch innych AS).

## Czym różnią się połączenia dostawca-klient od łącz partnerskich (peering)?
- **Dostawca-klient**: klient płaci, dostawca rozgłasza jego trasy.
- **Peering**: wzajemna wymiana danych bez opłat; nie rozgłasza się tras do swoich dostawców.

## Dlaczego w routingu między AS nie stosuje się najkrótszych ścieżek?
Bo decyzje routingowe wynikają z polityki (koszty, prywatność, autonomia), a nie z długości trasy.

## Które trasy w BGP warto rozgłaszać i komu? A które wybierać?
- **Rozgłaszać**: trasy do siebie, swoich klientów (bo płacą).
- **Nie rozgłaszać**: tras do dostawców i partnerów (chyba że klientowi).
- **Wybierać**: najpierw przez klienta, potem partnera, na końcu dostawcę.

## Jak BGP może współpracować z algorytmami routingu wewnątrz AS?
Routery brzegowe używają BGP do poznania tras między AS-ami, a następnie udostępniają te informacje do wewnętrznego protokołu (np. OSPF, RIP), który rozprowadza je wewnątrz AS.
