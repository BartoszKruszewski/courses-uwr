#### Zbiór roboczy

Zbiór aktualnie aktywnych stron w pamięci wirtualnej wykorzystywanych przez proces.

#### Obliczenia

TLB zawiera $64$ wpisy, ma $4$ wpisy na zbiór (bo jest czterodrożne), czyli ma $64 / 4 = 16$ zbiorów.

Możemy zakładać różne warianty trafień w TLB:

- **optymistyczny**: trafiamy ciągle w ten sam zbiór (wykorzytujemy tylko jeden zbiór, czyli 4 wpisy)
- **pesymistyczny**: trafiamy za każdym razem w różne wpisy (wykorzystujemy całe TLB, czyli 64 wpisy)

Warianty rozpatruje pod względem wykorzystania pamięci. Jeśli chodzi o efektywność działania procesu to nazwy **optymistyczny** i **pesymistyczny** będą na odwrót.

#### Oszacowania dla stron o wielkości 4KiB

Optymistycznie: $4 * 4KiB = 16KiB$
Pesymistycznie: $64 * 4KiB = 256KiB$

#### Oszacowania dla stron o wielkości 4MiB

Optymistycznie: $4 * 4MiB = 16MiB$
Pesymistycznie: $64 * 4MiB = 256MiB$

#### Przestrzeń adresowa

Przestrzeń adresowa ma wielkość $2^48B = 2^18GiB$, także na pewno pokryje wszystkie adresy.
