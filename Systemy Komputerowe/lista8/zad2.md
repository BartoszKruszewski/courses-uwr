#### Intuicja

Algorytm wykorzystuje buforowanie instrukcji oraz weryfikacje zbuforowanych instrukcji, w celu manipulacji czasem ich wykonania, co pozwala na uniknięcie hazardów danych.

#### Algorytm

1. **issue**: pobranie instrukcji oraz sprawdzanie, czy poprzednie instrukcje nie zapisują danych do tego samego rejestru
2. **read operands**: sprawdzanie, czy nowa instrukcja nie korzysta z wcześniej wykorzystywanych rejestrów
3. **execution**: wykonanie instrukcji
4. **write result**: zapis danych jeżeli wszystkie poprzedzające instrukcje, korzystające z tych samym rejestrów zostały już wykonane

#### Rozwiązanie hazardów

- **WAW**: w fazie **issue**
- **RAW**: w fazie **read operands**
- **WAR**: w fazie **write result**
