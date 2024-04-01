#### Znaczenie operacji $ \*(x + imm):= y $

Operacja polega na wpisaniu do pamięci wartości y pod adresem $x + imm$.

#### Wykonanie operacji

1. Przekazanie numeru instrukcji do rejstru rozkazów.
2. Oczytanie instrukcji przez rejestr rozkazów i przesłanie inforacji o niej do pliku rejestrów, oraz informacji, ze bedzie wykonywac dodawanie do ALU.
3. Odczytanie wartości zmiennych $x$ i $y$ przez rejestr plików i przesłanie wartości $x$ do ALU, a wartości $y$ do pamięci.
4. Rozszerzenie reprezentacji $imm$ do 32-bitów, zeby mozna było ją dodać do $x$.
5. Przekazanie $x$ oraz $imm$ do ALU, gdzie zostaną dodane.
6. Zapisanie wartości $y$ w pamięci pod wyliczonym w ALU adresem.
7. Instrukcja nie zmieniała przebiegu sterowania, więc zwiększamy wartość licznika rozkazów o 32-bity (długość pojedyńczej instrukcji).
