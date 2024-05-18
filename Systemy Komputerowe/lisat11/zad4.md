#### Rozłozenie bitów adresu

Strony mają wielkość $4KiB$, więc mamy 4048 komórek pamięci do zaadresowania. Odpowiada to offsetowi o wielkości $log_2(4048) = 12$

Mając 12 bitów na **VPO (Virtual Page Offset)** reszta bitów zostanie przeznaczona na **VPN (Virtual Page Number)**.

**TLB** jest w pełni asocjacyjne, to znaczy, ze nie mamy zbiorów, a co za tym idzie nie mamy tez **TLBI (TLB index)**, czyli całość bitów przeznaczonych na **VPN** odwzorowuje **TLBT (TLB tag)**.

Najwiekszy adres do jakiego odwołujemy się w tym zadaniu to $49225 = 1100000001001001$, więc przyjmujemy, że długość adresu to binarna długość tego adresu, czyli $16$ bitów.

Więc na **TLBT** przeznaczamy $16 - 12 = 4$ bity.

#### Adres 1

$4669 = 0001 001000111101$
$TLBT = VPN = 1$
nie ma go w **TLB**, i nie jest *Valid* w tablicy stron

Wpis do **tablicy stron**:
VPN: 1, valid: 1, PPN: 13 (pierwszy wolny)

Wpis do **TLB**:
Valid: 1, Tag: 1, LRU: 0, PPN: 13

| Valid? | Tag | LRU | PPN |
|:------:|:---:|:---:|:---:|
|   1    |  1  |  0  | 13  |
|   1    | 11  |  1  | 12  |
|   1    |  7  |  2  |  4  |
|   1    |  3  |  3  |  6  |

| VPN | Valid? | PPN  |
|:---:|:------:|:----:|
|  0  |   1    |  5   |
|  1  |   1    |  13  |
|  2  |   0    | dysk |
|  3  |   1    |  6   |
|  4  |   1    |  9   |
|  5  |   1    |  11  |
|  6  |   0    | dysk |
|  7  |   1    |  4   |
|  8  |   0    | dysk |
|  9  |   0    | dysk |
| 10  |   1    |  3   |
| 11  |   1    |  12  |
| 12  |   0    | brak |

#### Adres 2
$2227 = 0000 100010110011$
$TLBT = VPN = 0$
nie ma go w tablicy **TLB**, jest w **tablicy stron** z $PPN = 5$

Wpis do TLB:
valid: 1, tag 0, PPN: 5

| Valid? | Tag | LRU | PPN |
|:------:|:---:|:---:|:---:|
|   1    |  0  |  0  |  5  |
|   1    |  1  |  1  | 13  |
|   1    | 11  |  2  | 12  |
|   1    |  7  |  3  |  4  |

| VPN | Valid? | PPN  |
|:---:|:------:|:----:|
|  0  |   1    |  5   |
|  1  |   1    |  13  |
|  2  |   0    | dysk |
|  3  |   1    |  6   |
|  4  |   1    |  9   |
|  5  |   1    |  11  |
|  6  |   0    | dysk |
|  7  |   1    |  4   |
|  8  |   0    | dysk |
|  9  |   0    | dysk |
| 10  |   1    |  3   |
| 11  |   1    |  12  |
| 12  |   0    | brak |

#### Adres 3
$13916 = 0011 011001011100$
$TLBT = VPN = 3$
nie ma go w **TLB**, jest w tablicy stron, $PPN = 6$

| Valid? | Tag | LRU | PPN |
|:------:|:---:|:---:|:---:|
|   1    |  3  |  0  |  6  |
|   1    |  0  |  1  |  5  |
|   1    |  1  |  2  | 13  |
|   1    | 11  |  3  | 12  |

| VPN | Valid? | PPN  |
|:---:|:------:|:----:|
|  0  |   1    |  5   |
|  1  |   1    |  13  |
|  2  |   0    | dysk |
|  3  |   1    |  6   |
|  4  |   1    |  9   |
|  5  |   1    |  11  |
|  6  |   0    | dysk |
|  7  |   1    |  4   |
|  8  |   0    | dysk |
|  9  |   0    | dysk |
| 10  |   1    |  3   |
| 11  |   1    |  12  |
| 12  |   0    | brak |

#### Adres 4 
$34587 = 1000 011100011011$
$TLBT = VPN = 8$
nie ma go w **TLB**, i nie jest *Valid* w tablicy stron

Wpis do tablicy stron:
VPN: 8, valid: 1, PPN: 14 

| Valid? | Tag | LRU | PPN |
|:------:|:---:|:---:|:---:|
|   1    |  8  |  0  | 14  |
|   1    |  3  |  1  |  6  |
|   1    |  0  |  2  |  5  |
|   1    |  1  |  3  | 13  |

| VPN | Valid? | PPN  |
|:---:|:------:|:----:|
|  0  |   1    |  5   |
|  1  |   1    |  13  |
|  2  |   0    | dysk |
|  3  |   1    |  6   |
|  4  |   1    |  9   |
|  5  |   1    |  11  |
|  6  |   0    | dysk |
|  7  |   1    |  4   |
|  8  |   1    |  14  |
|  9  |   0    | dysk |
| 10  |   1    |  3   |
| 11  |   1    |  12  |
| 12  |   0    | brak |

#### Adres 5
$48870 = 1011 111011100110$
$TLBT = VPN = 11$
nie ma go w **TLB**, jest w **tablicy stron**, $PPN = 12$

| Valid? | Tag | LRU | PPN |
|:------:|:---:|:---:|:---:|
|   1    | 11  |  0  | 12  |
|   1    |  8  |  1  | 14  |
|   1    |  3  |  2  |  6  |
|   1    |  0  |  3  |  5  |

| VPN | Valid? | PPN  |
|:---:|:------:|:----:|
|  0  |   1    |  5   |
|  1  |   1    |  13  |
|  2  |   0    | dysk |
|  3  |   1    |  6   |
|  4  |   1    |  9   |
|  5  |   1    |  11  |
|  6  |   0    | dysk |
|  7  |   1    |  4   |
|  8  |   1    |  14  |
|  9  |   0    | dysk |
| 10  |   1    |  3   |
| 11  |   1    |  12  |
| 12  |   0    | brak |

#### Adres 6
$12608 = 0011 000101000000$
$TLBT = VPN = 3$
jest w **TLB**

| Valid? | Tag | LRU | PPN |
|:------:|:---:|:---:|:---:|
|   1    |  3  |  0  |  6  |
|   1    | 11  |  1  | 12  |
|   1    |  8  |  2  | 14  |
|   1    |  0  |  3  |  5  |

| VPN | Valid? | PPN  |
|:---:|:------:|:----:|
|  0  |   1    |  5   |
|  1  |   1    |  13  |
|  2  |   0    | dysk |
|  3  |   1    |  6   |
|  4  |   1    |  9   |
|  5  |   1    |  11  |
|  6  |   0    | dysk |
|  7  |   1    |  4   |
|  8  |   1    |  14  |
|  9  |   0    | dysk |
| 10  |   1    |  3   |
| 11  |   1    |  12  |
| 12  |   0    | brak |

#### Adres 7
$49225$ = 1100 000001001001$ 
$TLBT = VPN = 12$
nie ma go w **TLB**, nie ma go w **tablicy ston**

otrzymujemy błąd

| Valid? | Tag | LRU | PPN |
|:------:|:---:|:---:|:---:|
|   1    |  3  |  0  |  6  |
|   1    | 11  |  1  | 12  |
|   1    |  8  |  2  | 14  |
|   1    |  0  |  3  |  5  |

| VPN | Valid? | PPN  |
|:---:|:------:|:----:|
|  0  |   1    |  5   |
|  1  |   1    |  13  |
|  2  |   0    | dysk |
|  3  |   1    |  6   |
|  4  |   1    |  9   |
|  5  |   1    |  11  |
|  6  |   0    | dysk |
|  7  |   1    |  4   |
|  8  |   1    |  14  |
|  9  |   0    | dysk |
| 10  |   1    |  3   |
| 11  |   1    |  12  |
| 12  |   0    | brak |
