# Notatka z wykładu – Routing wewnątrz routera

## Prywatne adresy IP i zarezerwowane pule
Prywatne adresy IP są przeznaczone do użytku w sieciach lokalnych i nie są routowalne w Internecie. Zarezerwowane pule:
- 10.0.0.0/8
- 172.16.0.0/12
- 192.168.0.0/16
- IPv6: fd00::/8

## Funkcja `bind()`
Służy do powiązania gniazda z konkretnym adresem IP i portem. Wymagana dla serwera. Klienci często korzystają z automatycznie przydzielanego portu.

## Porty < 1024
Porty o numerach mniejszych niż 1024 są tzw. portami uprzywilejowanymi. Aby się z nimi związać, wymagane są uprawnienia administratora.

## Zadania elementów routera
- **Procesor routingu** – tworzy tablice przekazywania.
- **Port wejściowy** – odbiera pakiety, modyfikuje TTL i sumy kontrolne.
- **Port wyjściowy** – wysyła pakiety.
- **Struktura przełączająca** – przekazuje pakiety między portami z dużą prędkością.

## Przełączanie przez RAM vs strukturę przełączającą
- RAM: wszystkie operacje przez CPU, wolniejsze.
- Struktura przełączająca: dedykowana sieć połączeń, szybsze i skalowalne przekazywanie.

## Pożądane cechy struktury przełączającej
- Przepustowość zbliżona do N × R (N – liczba portów, R – prędkość portu).
- Niska złożoność połączeń (np. O(N log N) – sieci Benesa).

## Buforowanie w routerze
Stosowane przy portach wejściowych i wyjściowych:
- **Wyjściowe** – zapobiegają utracie przy nagłych skokach ruchu.
- **Wejściowe** – konieczne, gdy struktura przełączająca jest zbyt wolna.

## Klasyfikacja pakietów w portach wyjściowych
Służy do przypisania pakietów do strumieni i umożliwia szeregowanie wg priorytetów lub round-robin.

## Blokowanie początku kolejki
Zjawisko, gdy pakiet czekający na zajęty port blokuje inne. Występuje przy buforowaniu na wejściu. Rozwiązanie: wirtualne kolejki (dla każdego portu wyjściowego osobna kolejka).

## LPM – Longest Prefix Match
Mechanizm wyboru reguły w tablicy przekazywania z najdłuższym pasującym prefiksem.

## Struktury danych dla LPM
1. **Lista prefiksów** – pamięć O(n), lookup O(n)
2. **Tablice haszujące** – O(w) lookup, O(1) insert/delete
3. **Trie (drzewo prefiksów)** – O(w) wszystkie operacje, możliwość kompresji
4. **Trie z krawędziami skracającymi** – lookup O(log w), insert/delete nawet O(n)
5. **TCAM** – sprzętowa, szybkie wyszukiwanie pasujących prefiksów równolegle

## TCAM
Ternary CAM – pamięć sprzętowa do szybkiego wyszukiwania. Zawiera pary (prefiks, maska) i pozwala na równoległe dopasowanie wszystkich reguł.

## Fragmentacja IP
Dzieli pakiet na mniejsze fragmenty, jeśli przekracza MTU. Może zachodzić na dowolnym routerze, a łączenie fragmentów następuje dopiero u odbiorcy.

## MTU i jego wykrywanie
MTU = maksymalna wielkość pakietu dla łącza. Wykrywanie przez ustawienie bitu DF – router zwraca ICMP, jeśli konieczna fragmentacja, z informacją o MTU.

## Szeregowanie pakietów
- FIFO – wg kolejności przyjścia.
- Priorytetowe – wg ważności strumienia.
- Round-robin – naprzemiennie z każdego strumienia.

## IPv4 vs IPv6
- IPv6: 128-bitowe adresy, brak fragmentacji i sumy kontrolnej, nagłówek o stałej długości.
- IPv4: 32-bitowe adresy, możliwość fragmentacji, suma kontrolna.

## Skrócony adres IPv6
0321:0000:0000:0123:0000:0000:0000:0001 → `321:0:0:123::1`

## Tunelowanie 6in4
Pakiety IPv6 osadzane jako dane w pakietach IPv4. Umożliwia przesył IPv6 przez infrastrukturę IPv4.

## NAT – Network Address Translation
Mechanizm zamiany prywatnych adresów IP na publiczne. Zalety:
- Oszczędność adresów IP.
- Niezależność od ISP.
Wady:
- Trudność w inicjowaniu połączeń z Internetu.
- Łamanie modelu warstwowego.

## Stan w NAT
Router NAT musi przechowywać tabelę mapującą (adres źródłowy, port, adres docelowy, port) → port translacji. Przypisanie tymczasowe, używane do powrotu pakietów.
