Rozmiar podsieci może być tylko potęgą 2.
Sieć **10.10.0.0/16** ma **(2^16) adresów** (w tym dwa nieużyteczne).
Czyli najmniejsze x musi wystapic dwa razy, poniewaz musza sie sumowac do wyzszej potegi (chcemy pokryc wszystkie adresy).
Jezeli chcemy zeby siec zajmowala najmniej to pozostale sieci musza zajmowac jak najwiecej.

$2^{15} + 2^{14} + 2^{13} + 2^{12} + 2^{12} = 2^{16}$.

Wyznaczmy podsieci takich wielkosci:
- $10.10.128.0/17$
- $10.10.64.0/18$
- $10.10.32.0/19$
- $10.10.16.0/20$
- $10.10.0.0/20$

Minimalny rozmiar podsieci to $2^{12} - 2 = 4096 - 2 = 4094$ \
(Odejmujemy dwa bo to adres sieci i rozgloszeniowy)

