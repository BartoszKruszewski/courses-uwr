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
