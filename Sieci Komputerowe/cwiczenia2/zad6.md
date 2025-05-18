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
