#### Znaczenie operacji $ x = y \; binop \; z $

Operacja polega na wykonaniu operacji arytmetycznej na $y$ oraz $z$ i przypisanie jej do $x$.

#### Multiplexery

- **RegDst**: pozwala na większy wybór rejestru docelowego
- **ALUSrc**: pozwala na wykonywanie operacji na stałych
- **MemToReg**: pozwala na zapis wyniku z ALU bezpośrednio do rejestru

Wartości sterujące multiplekaserami są odpowiednio ustawiane po odczytaniu instrukcji.

#### Wykonanie operacji

1. Przekazanie numeru instrukcji do rejstru rozkazów.
2. Oczytanie instrukcji przez rejestr rozkazów i przesłanie inforacji o niej do pliku rejestrów, oraz informacji o typie operacji arytmetycznej do ALU.
3. Odczytanie wartości zmiennych $y$ i $z$ przez rejestr plików i przesłanie ich do ALU, oraz wybór rejestru $x$ do zapisu.
4. Zapisanie wyniku działania ALU do rejestru $x$
5. Instrukcja nie zmieniała przebiegu sterowania, więc zwiększamy wartość licznika rozkazów o 32-bity (długość pojedyńczej instrukcji).
