#### Format tablicy stron

Procesory w architekturze x86-64 używają czteropoziomowej tablicy stron. Tablice wyższych poziomów zawierają wpisy odnoszące się do tablic niższych poziomów.

#### Format adresów wirtualnych

TLB jest czterodrożne i ma 16 zbiorów.

- **VPN**: 36 bitów (32 bity na TLBT i 4 bity na TLBI)
- **VPO**: 12 bitów

W przypadku miss do TLB, VPO jest dzielone na 4 części po 9 bitów oznaczające odpowiednio offset w tablicach kolejnych poziomów.Adresy kolejnych tablic są przechowywane we wpisach tablic wyższych poziomów.

#### Znaczenie bitów pomocnicznych

- **P**: czy pole adresowe zawiera adres do następnego poziomu tablicy
- **R/W**: czy strony dostępne z tego adresu są dostępne tylko do odczytu czy do odczytu i zapisu
- **U/S**: czy dostęp do stron z tego adresu mają programy użytkownika czy też dostęp ma jedynie jądro systemu
- **WT**: czy strony z tego adresu używają polityki zapisu write-back czy write-through
- **CD**: czy strony z tego adresu mają być sprawdzane czy też należy od razu odwołać się do pamięci głównej
- **A**: bit referencji, określa, czy tablice stron powinny zostać wyrzucone w przypadku chybienia
- **PS**: ustala rozmiar strony na 4KB lub 4MB
- **G**: czy strona powinna zostać wyrzucona z TLB w przypadku zmiany procesu
- **Page table physical base addr**: adres do tablicy niższego poziomu
- **XD**: czy ze stron z tego adresu można odczytać instrukcje dla procesów

#### Tablice 4 poziomu

Wpisy w tablicach 1, 2, 3 są takie same, natomiast tablice 4 poziomu mają jeden dodatkowy bit D (dirty bit), określający, czy należy zmodyfikować stronę w pamięći głównej po usunięciu wpisu z tablicy stron.

#### Różnice pomiędzy tablicą jednopziomową

Jeżeli adres w tablicy wyższego poziomu nie jest określony, to nie trzeba rezerwować pamięci dla tablic niższych poziomów.
Powoduje to dużą oszczędność pamięci, przy stosunkowo małym dodatkowym koszcie czasu.
