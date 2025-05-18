$n$ to liczba możliwych stacji, które mogą wysyłać

$p$ tp ppb, że jedna z nich nada

$(1 - p)^{n-1}$ to ppb, że reszta nie nadaje

Ppb, że dokładnie jedna stacja nada: $P(p, n) = n \cdot p \cdot (1 - p)^{n-1}$

Aby znaleźć maksimum funkcji $P(p, n)$, liczymy pochodną po $p$ i szukamy miejsca zerowego:

$\frac{dP}{dp} = n(1-p)^{n-2} \left[(1 - p) - (n - 1)p\right]$

Zerując wyrażenie w nawiasie:

$(1 - p) - (n - 1)p = 0 \Rightarrow p = \frac{1}{n}$

$\lim_{n \to \infty} P\left(\frac{1}{n}, n\right) = \lim_{n \to \infty} \left( n \cdot \frac{1}{n} \cdot \left(1 - \frac{1}{n}\right)^{n-1} \right) = \lim_{n \to \infty} \left(1 - \frac{1}{n}\right)^{n-1} = \frac{1}{e} \approx 0.3679 $
