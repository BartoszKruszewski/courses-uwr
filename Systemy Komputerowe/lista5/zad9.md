#### Zadania poszczególnych elementów procesora

- **licznik rozkazów**: przesyła kolejne numery instrukcji w kazdym cyklu zegara
- **rejestr rozkazów**: przyjmuje numer instrukcji od licznika i zwraca jej treść
- **plik rejestrów**: odczytuje i zapisuje wartości zmiennych do rejestrów,
wejścia A1, A2 i RD1, RD2 słuzą do odczytu, natomiast A3 i WD3 do zapisu.
Wejście jednobitowe WE3 sluzy do okreslenia czy chcemy zapisywac
- **ALU *(jednostka arytmetyczno-logiczna)***: wykonuje podstawowe operacje arytmetyczne i logiczne, jest sterowana przez 3-bitowe wejśćie, za pomocą którego wybieramy jaką operacje chcemy wykonać
- **pamiec danych**: zapisuje i odczytuje dane, głównie z przeznaczeniem "na pózniej".

#### Znaczenie operacji $ x:= *(y + imm)$

Operacja polega na odczytaniu wartości z pamięci pod adresem $y + imm$, a następnie przypisaniu jej do $x$.

#### Wykonanie operacji

1. Przekazanie numeru instrukcji do rejstru rozkazów
2. Oczytanie instrukcji przez rejestr rozkazów i przesłanie inforacji o niej do pliku rejestrów, oraz informacji, ze bedzie wykonywac dodawanie do ALU
3. Odczytanie wartości zmiennych $y$ i $imm$ przez rejestr plików, oraz zdefiniowanie, ze będzie zapisać dane do $x$
4. Rozszerzenie reprezentacji $imm$ do 32-bitów, zeby mozna było ją dodać do $y$
5. Przekazanie $y$ oraz $imm$ do ALU, gdzie zostaną dodane
6. Odczytanie danych z pamięci pod wyliczonym w kroku 5. adresem i przekazanie ich do pliku rejestrów, gdzie zostaną zapisane jako $x$
7. Instrukcja nie zmieniała przebiegu sterowania, więc zwiększamy wartość licznika rozkazów o 32-bity (długość pojedyńczej instrukcji).
