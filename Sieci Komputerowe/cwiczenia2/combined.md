# Sieci Komputerowe Ćwiczenia 2

## Bartosz Kruszewski 337568

### Zadanie 1

Aby możliwe było wykrycie kolizji, ramka musi być nadawana przez czas równy co najmniej **dwukrotnemu czasowi propagacji**  między najdalszymi komputerami.

Prędkość sygnału: $10^8\ m/s$

Odległość: $2,5\  km = 2500\ m$

Czas propagacji w jedną stronę: $t_{p} = \frac{2500}{10^8} = 25 \cdot 10^{-6}\ s$

Czas rundy (RTT): $RTT = 2 \cdot 25 \cdot 10^{-6}\ s = 50 \cdot 10^{-6}\ s$

Minimalna liczba bitów: $10^7\ b/s \cdot 50 \cdot 10^{-6}\ s = 500\ \text{b} = 62.5\ \text{B}$

Aby zapewnić wykrywanie kolizji, ramka musi mieć **min. 500 bitów**.

Standard Ethernet zaokrągla to do **64 bajtów (512 bitów)**.

### Zadanie 2

$n$ to liczba możliwych stacji, które mogą wysyłać

$p$ tp ppb, że jedna z nich nada

$(1 - p)^{n-1}$ to ppb, że reszta nie nadaje

Ppb, że dokładnie jedna stacja nada: $P(p, n) = n \cdot p \cdot (1 - p)^{n-1}$

Aby znaleźć maksimum funkcji $P(p, n)$, liczymy pochodną po $p$ i szukamy miejsca zerowego:

$\frac{dP}{dp} = n(1-p)^{n-2} \left[(1 - p) - (n - 1)p\right]$

Zerując wyrażenie w nawiasie:

$(1 - p) - (n - 1)p = 0 \Rightarrow p = \frac{1}{n}$

$\lim_{n \to \infty} P\left(\frac{1}{n}, n\right) = \lim_{n \to \infty} \left( n \cdot \frac{1}{n} \cdot \left(1 - \frac{1}{n}\right)^{n-1} \right) = \lim_{n \to \infty} \left(1 - \frac{1}{n}\right)^{n-1} = \frac{1}{e} \approx 0.3679 $

### Zadanie 3

Sume kontrolą obliczamy używając wzoru:

$CRC = {M(x)\ \cdot x^r} \mod {G(x)}$

gdzie:

$M(x)$ to wiadomość

mnożenie przez $x^r$ to uzupełnienie zerami do odpowiedniego stopnia

$G(x)$ to wielomian, którego używa algorytm

Dzielenie z resztą jest wykonywane w pierścieniu wielomianów $F_2$

Sume kontrolą doklejamy do wiadomości.

|               | $G(x) = x^2 + x + 1 = 111$ | $G(x) = x^7 + 1 = 10000001$ |
| ------------- | -------------------------- | --------------------------- |
| Dopisanie zer | 1010**00**                 | 1010**0000000**             |
| CRC           | 10                         | 0001010                     |
| Ramka         | 1010**10**                 | 1010**0001010**             | 


### Zadanie 4

$M(x) = a_0 + a_1 x + \dots + a_n x^n \in \mathbb{F}_2[x]$

$x + 1 \mid M(x) \;\Leftrightarrow\; M(1) = 0 \;\Leftrightarrow\; \sum_{i=0}^{n} a_i \equiv 0 \pmod{2}$

Więc $x + 1 \mid M(x)$ wtedy i tylko wtedy, gdy suma współczynników jest parzysta

Stąd sprawdzanie sprawdzanie parzystości liczby zapalonych bitów w wiadomości jest równoważne z dzieleniem przez $x + 1$

Dla $G(x) = x + 1 \Rightarrow r = 1$, więc dopisujemy tylko jeden bit jak w przypadku metody bitu parzystości.

Podsumowując:
- dopisywanie bitu jest identyczne w przypadku obu metod, ponieważ dopisany bit oznacza parzystość zapalonych bitów.
- weryfikacja przekłamań jest identyczna, ponieważ w obu przypadkach działania sprowadzają się do sprawdzenia parzystości otrzymanych bitów


### Zadanie 5

Załóżmy, że w wiadomości zmodyfikowano dowolny odcinek długości $n$, czyli kolejne $n$ bitów.

Taki błąd można zapisać jako:

$E(x) = x^k A(x)$, gdzie $\deg A(x) \le n - 1$


czyli błąd występuje w $n$ pozycjach przesuniętych o $k$ bitów.

Dowód nie wprost:
- Błąd nie został wykryty $\Leftrightarrow$ $G(x) dzieli $E(x)$
- $G(x)$ dzieli $E(x)$  $\Leftrightarrow$ $G(x)$ dzieli $x^k$ albo $A(x)$.
- $G(x)$ **nie dzieli** $x^k$, bo ma wyraz stały (czyli nie jest podzielny przez $x$),
- $G(x)$ **nie dzieli** $A(x)$, bo $\deg A(x) < \deg G(x)$.
- Sprzeczność, więc taki błąd **musi zostać wykryty**.

Jeżeli $G(x)$ nie zawiera wyrazu stałego to może się zdarzyć, że $G(x)$ dzieli $x^k$, a wtedy błąd nie zostanie wykryty.

### Zadanie 6

Rozważamy błędy dwubitowe oddalone od siebie o co najwyżej 6 bitów. Taki błąd ma postać:

Dla $1 \le k \le 6$:

$E(x) = x^i(1 + x^k)$

Jest to błąd na $i$-tym i $(i+k)$-tym bicie

Błąd nie zostanie wykryty, gdy:

$G(x)$ dzieli $E(x)$ $\Leftrightarrow$ $G(x)$ dzieli $(1 + x^k)$

Sprawdzamy dla każdego $k$ (odejmujemy od $G(x)$ przemnożone przez odpowiednie $x^a$):

- $x + 1$ za niski stopień
- $x^2 + 1$ za niski stopień
- $x^3 + 1 - (x^3 + x + 1) = x \ne 0$
- $x^4 + 1 - (x^4 + x^2 + x) = x^2 + x + 1 \ne 0$
- $x^5 + 1 - (x^5 + x^3 + x^2) = x^3 + x^2 + 1 \ne 0$
- $x^6 + 1 - (x^6 + x^4 + x^3) = x^4 + x^3 + 1 \ne 0$

Dla $1 \le k \le 6$:

$G(x)$ nie dzieli $(1 + x^k)$

CRC wykryje wszystkie błędy dwubitowe oddalone o co najwyżej 6 bitów.


### Zadanie 7

Używamy CRC z wielomianem: $G(x) = x^3 + x + 1$

Nadajemy wiadomość 4 bity (1101) + 3 dodatkowe bity CRC = 7 bitów

Co najwyżej jeden bit został przekłamany

Odbiorca używając CRC sprawdza czy $G(x)$ dzieli naszą odebraną ramkę

Jeżeli bit został przekłamany to otrzymujemy niezerową resztę

Sprawdźmy jak będzie wyglądać reszta przy zmianie poszczególnych bitów:

| Pozycja bitu (0 = najmniej znaczący) | Wielomian $x^k \bmod G(x)$ | reszta (format binarny) |
|--------------------------------------|----------------------------|-------------------------|
| 0                                    | $1$                        | 001                     |
| 1                                    | $x$                        | 010                     |
| 2                                    | $x^2$                      | 100                     |
| 3                                    | $x + 1$                    | 011                     |
| 4                                    | $x^2 + x$                  | 110                     |
| 5                                    | $x^2 + x + 1$              | 111                     |
| 6                                    | $x^2 + 1$                  | 101                     |

Jak możemy zauważyć reszta w każdym przypadku jest inna

Po wtyliczeniu reszty można spojrzeć w tabelkę i odczytać który bit został przekłamany i go zanegować


### Zadanie 8

Z definicji kodu Hamminga(7, 4)

Bity parzystości w pozycjach potęg dwójki: 1, 2, 4

Bity danych: 3, 5, 6, 7

| pozycja | 1  | 2  | 3  | 4  | 5  | 6  | 7  |
|---------|----|----|----|----|----|----|----|
| rola    | p1 | p2 | d1 | p3 | d2 | d3 | d4 |

Macierz kontroli parzystości

$H=\begin{bmatrix}
1 & 0 & 1 & 0 & 1 & 0 & 1\\
0 & 1 & 1 & 0 & 0 & 1 & 1\\
0 & 0 & 0 & 1 & 1 & 1 & 1
\end{bmatrix}$

Mnożąc macierz przez wektor bitowy otrzymanej ramki otrzymany binarny zapis pozycji przekłamanego bitu.

Minimalna odległość kodowa pomiędzy dwoma kodami (odległość Hamminga) to $3$ (3 niezależne bity parzystości), więc możemy skorygować do $(3-1)/2 = 1$ bitów.

### Zadanie 9

$p = 0.01$ to ppb błedu

$q = 1-p = 0.99$ to ppb poprawności

$q^{100} = 0.99^{100} \approx 0.36$ to ppb, że ramka bez kodowania jest poprawna

Przy kodowaniu Hamminga(7, 4) mamy $100 / 4 = 25$ 4-bitowych bloków.

Każdy blok kodujemy do 7 bitów, więc mamy $25 \cdot 7 = 175$ bitów.

Blok jesteśmy w stanie naprawić jeżeli ma jeden bit błędu.

Stąd ppb otrzymania poprawnego bloku to:

x = $q^{7} + \binom{7}{1} \cdot p \cdot  q^{6} = 0.99^{7} + 7 \cdot 0.01 \cdot 0.99^{6} \approx 0.99797$

Dla całej ramki to 

$x^{25}\approx 0.99797^{25}\approx 0.950$

### Zadanie 10

$p = \prod_{k=0}^{n-1} \left(1 - \frac{k}{2^m}\right)$ to ppb braku kolizji

bo spośród $2^m$ możliwych wartości $h(x)$ już $k$ jest zajętych

Dla dużych $m$, korzystamy z przybliżenia (działa dla małych $x$):

$\ln(1 - x) \approx -x$

stąd:

$\ln p = \sum_{k=0}^{n-1} \ln{(1 - \frac{k}{2^m})} \approx -\sum_{k=0}^{n-1} \frac{k}{2^m} = -\frac{n(n-1)}{2 \cdot 2^m}$

podstawiamy $n = 2^{m/2}$:

$-\frac{n(n-1)}{2 \cdot 2^m} \approx -\frac{1}{2}$

$p \approx e^{-1/2}$

Obliczamy ppb kolizji:

$q = 1 - p \approx 1 - e^{-1/2} \approx 0{,}39 = \Omega(1)$
