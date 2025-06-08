# Notatka – Sieci komputerowe – Wykład 1

## Co to jest protokół komunikacyjny? Dlaczego wprowadza się warstwy protokołów?

Protokół komunikacyjny to zbiór zasad określających sposób wymiany danych między aplikacjami w sieci. Warstwy protokołów wprowadza się w celu modularności, ułatwienia implementacji, możliwości niezależnego rozwoju warstw i prostoty zarządzania funkcjami sieciowymi.

## Warstwy internetowego modelu warstwowego i ich zadania

1. **Aplikacji** – HTTP, SMTP – protokoły użytkownika.
2. **Transportowa** – TCP, UDP – dzieli dane na pakiety, wprowadza porty, zapewnia niezawodność.
3. **Sieciowa** – IP – routuje pakiety, dostarcza globalnie.
4. **Łącza danych** – Ethernet, WiFi – przesyła ramki, zapewnia dostęp do medium.
5. **Fizyczna** – przesyła bity przez kanał.

## Warstwy zaimplementowane na komputerach i routerach

- **Komputery**: wszystkie warstwy (1–5).
- **Routery**: warstwa 3 (sieciowa), 2 (łącza danych), 1 (fizyczna).

## Różnice między modelem TCP/IP a OSI

- TCP/IP łączy warstwy fizyczną i łącza danych w jedną.
- OSI ma dodatkowe warstwy: sesji i prezentacji między transportową a aplikacyjną.

## Co jest potrzebne do zbudowania dwukierunkowego niezawodnego kanału?

- Adresacja IP, dzielenie na pakiety, niezawodność przesyłania (np. TCP), porty aplikacji.

## Wady i zalety przełączania obwodów i pakietów

| Cechy | Obwody | Pakiety |
|-------|--------|---------|
| Gwarancja przepustowości | ✔ | ✘ |
| Koszt nawiązania | wysoki | niski |
| Efektywność | niska | wysoka |
| Odporność na awarie | niska | wysoka |
| Skomplikowanie | wysokie | niskie |

## Rodzaje multipleksowania i ich zastosowanie

- **TDM (czasowe)** – każdemu przydzielany czas transmisji.
- **FDM (częstotliwościowe)** – każdemu przydzielana częstotliwość.
- **Statystyczne** – pakiety współdzielą łącze dynamicznie – najlepsze wykorzystanie medium.

## Rodzaje routingu

- **Źródłowy** – trasa w nagłówku pakietu.
- **Z tablic routingu** – routery kierują pakiety wg reguł.
- **Wirtualne obwody** – ustalona trasa po wysłaniu pakietu kontrolnego.

## Rodzaje komunikacji

- **Simpleksowa** – jednokierunkowa.
- **Półdupleksowa** – naprzemienna w obu kierunkach.
- **Pełnodupleksowa** – jednoczesna w obu kierunkach.

## Do czego służy traceroute?

Służy do śledzenia trasy pakietu w sieci i pokazuje pośrednie routery oraz czasy przejścia.

## Po co bufory w routerach? Co to przeciążenie?

Bufory przechowują pakiety przy przeładowaniu. Przeciążenie następuje przy ich przepełnieniu – prowadzi do utraty pakietów.

## Przyczyny opóźnień pakietów

- Czas oczekiwania w kolejce.
- Czas transmisji (rozmiar/przepustowość).
- Czas propagacji sygnału.

## BDP i czas propagacji

- **BDP (Bandwidth-Delay Product)** – ile danych można wysłać przed otrzymaniem odpowiedzi.
- **Czas propagacji** – ile trwa przesłanie sygnału między dwoma punktami.

## Protokół IP – funkcje i zasada best effort

- Umożliwia przesyłanie pakietów między urządzeniami.
- Best effort – brak gwarancji dostarczenia i kolejności, ale pakiety nie są gubione celowo.

## Zalety i wady zasady end-to-end

- **Zalety**: prostota sieci, elastyczność, łatwość wdrażania nowych usług.
- **Wady**: więcej odpowiedzialności po stronie urządzeń końcowych.

## Po co porty?

Porty pozwalają rozróżnić różne aplikacje działające na tym samym urządzeniu.

## Enkapsulacja i dekapsulacja

- **Enkapsulacja** – dodawanie nagłówków przy przechodzeniu do niższych warstw.
- **Dekapsulacja** – usuwanie nagłówków przy przechodzeniu do wyższych warstw.