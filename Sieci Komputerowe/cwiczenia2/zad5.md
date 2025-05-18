Załóżmy, że w wiadomości zmodyfikowano dowolny odcinek długości $n$, czyli kolejne $n$ bitów.

Taki błąd można zapisać jako:

$E(x) = x^k A(x)$, gdzie $\deg A(x) \le n - 1$


czyli błąd występuje w $n$ pozycjach przesuniętych o $k$ bitów.

Dowód nie wprost:
- Błąd nie został wykryty $\Leftrightarrow$ $G(x) dzieli $E(x)$
- $G(x)$ dzieli $E(x)$  $\Leftrightarrow$ $G(x)$ dzieli $x^k$ albo $A(x)$.
- $G(x)$ **nie dzieli** $x^k$, bo ma wyraz stały (czyli nie jest podzielny przez $x$),
- $G(x)$ **nie dzieli** $A(x)$, bo $\deg A(x) < \deg G(x)$.
- Sprzeczność ⇒ taki błąd **musi zostać wykryty**.

Jeżeli $G(x)$ nie zawiera wyrazu stałego to może się zdarzyć, że $G(x)$ dzieli $x^k$, a wtedy błąd nie zostanie wykryty.

