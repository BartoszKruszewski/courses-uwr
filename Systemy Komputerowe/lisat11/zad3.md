#### Pojęcia

- **translacja adresów**: proces tłumaczenia adresów wirtualnych na fizyczne
- **TLB (Translation lookaside buffer)**: pamieć pomocnicza do obługi pamięci wirtualnej (działa jak cache dla MMU)
- **tablica stron**: pamięć przechowująca informacje o adresach fizycznych poprzednio wczytanych do pamięci operacyjnej lub jeszcze znajdujących się na dysku

#### Znaczenie adresu wirtualnego

- **TLBI (TLB index)**: indeks zbioru w TLB
- **TLBT (TLB tag)**: tag bloku w **TLB**
- **VPO (Virtual Page Offset)**: przesunięcie strony w pamięci wirtualnej
- **VPN (Virtual Page Number)**: numer strony w pamięci wirtualnej (pokrywa się z **TLBI** oraz **TLBT**)

#### Znaczenie adresu fizycznego

- **CT (Cache Tag)**
- **CI (Cache Index)**
- **CO (Cache Offset)**
- **PPN (Physical Page Number)**: 
numer strony w pamięci fizycznej (pokrywa się z **CI** oraz **CO**)
- **PPO (Physical Page Offset)**: przesunięcie strony w pamięci fizycznej (jest takie same jak **VPO**)

#### Translacja adresu

1. sprawdzamy, czy **TLBI** oraz **TLBT** są w **TLB** oraz czy są *Valid*
2. jezeli tak to odczytujemy **PPN** z **TLB**
3. jezeli nie to szukamy **PPN** w tablicy stron za pomoca **VPN**
4. przepisujemy **VPO** do **PPO**
5. Odczytujemy **CT**, **CI**, **CO**

#### Adres 1

$0x027c = 00001001111100$
$TLBT = 000010 = 0x02$
$TLBI = 01 = 0x01$
$VPN = 00001001 = 0x09$
$VPO = 111100 = 0x3c$

Wartość w **TLB** nie jest *Valid*, wiec szukamy za pomoca **VPN**.

$PPN = 0x17 = 010111$

Adres po translacji:  **010111 111100**
$CT = 010111 = 0x17$
$CI = 1111 = 0x0f$
$CO = 00 = 0x00$

#### Adres 2

$0x03a9 = 00001110101001$
$TLBT = 000011 = 0x03$
$TLBI = 10 = 0x03$
$VPN = 00001110 = 0x0e$
$VPO = 101001 = 0x29$

Wartość w **TLB** jest *Valid*, wiec odczytujemy **PPN**.

$PPN = 0x0D = 001101$

Adres po translacji:  **001101 101001**
$CT = 001101 = 0x0D$
$CI = 1010 = 0x0a$
$CO = 01 = 0x01$

#### Adres 3

$0x0040 = 00000001000000$
$TLBT = 000000 = 0x00$
$TLBI = 01 = 0x01$
$VPN = 00000001 = 0x01$
$VPO = 000000 = 0x00$

Nie ma tego tagu w **TLB**, więc szukamy za pomocą **VPN**.

Pod ustalonym **VPN** nie ma wartości w **tablicy stron**, więc mamy chybienie.
