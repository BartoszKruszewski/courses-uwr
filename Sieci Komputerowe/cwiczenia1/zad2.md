## Podział sieci 10.10.0.0/16 na 5 podsieci

Sieć **10.10.0.0/16** ma **65536 adresów** (2¹⁶).
Użyteczne adresy: **65534** (po odjęciu adresu sieci i broadcastu).

### 2. Podział na 5 rozłącznych podsieci
Podziału można dokonać na dwa 
- **Podział na /19**: daje **8192 adresy** na podsieć (8190 użytecznych).
- **Uzyskane podsieci**:
  - 10.10.0.0/19
  - 10.10.32.0/19
  - 10.10.64.0/19
  - 10.10.96.0/19
  - 10.10.128.0/19

### 3. Zmiana liczby użytecznych adresów
- Przed podziałem: **65534** adresy.
- Po podziale na 5 podsieci /19: **40950** adresów.

### 4. Minimalny rozmiar podsieci
- Najmniejsza możliwa podsieć w tym podziale: **/19 (8192 adresy, 8190 użytecznych)**.
