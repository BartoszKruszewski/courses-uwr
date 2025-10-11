#### Prawo Amdahla

$speedup = \frac{1}{1 - p + \frac{p}{n}}$

#### Podpunkt 1.

$1 - p = 0.4$

$p = 0.6$

Dla $n$ zmierzającego do nieskończoności $\frac{p}{n}$ zmierza do $0$.

Stąd $speedup = \frac{1}{0.4 + 0} \approx 2.5$

#### Podpunkt 2.

Oznaczmy wymagane przyśpieszenie jako $s$

Wtedy $2 = \frac{0.3 + \frac{0.7}{n}}{\frac{0.3}{s} + \frac{0.7}{n}}$

Stąd $s = \frac{0.6}{0.3 - \frac{0.7}{n}} = \frac{6n}{3n - 7}$ co jest odpowiedzią

*Dodatkowo*

Dla $n$ zmierzającego do nieskończoności $\frac{0.7}{n}$ zmierza do $0$.

Więc dla $n$ zmierzającego do nieskończoności $s \rarr 2$

#### Podpunkt 3.

Szukamy $1 - p$

Wtedy $2 = \frac{1 - p + \frac{p}{n}}{\frac{1 - p}{3} + \frac{p}{n}}$

Stąd $2 * (\frac{1 - p}{3} + \frac{p}{n}) = 1 - p + \frac{p}{n}$

Stąd $\frac{2 * (1 - p)}{3} + \frac{p}{n} = 1 - p$

Oznaczmy $1 - p$ jako $f$

Stąd $\frac{2 * f}{3} + \frac{1 - f}{n} = f$

Stąd $\frac{1 - f}{n} = \frac{f}{3}$

Stąd $3 - 3f = fn$

Stąd $3 = fn + 3f$

Stąd $3 = f(n + 3)$

Stąd $f = \frac{3}{n + 3}$
