#### Znaczenie operacji $ if \; x \; relop \; y \; goto \; L $

Operacja polega na obliczeniu $x$ relop $y$, a w przypadku wystąpienia wyniku > 0, na wykonaniu skoku licznika instrukcji do adresu $PC + L$.

_$PC$ to aktaulny stan licznika instrukcji._

#### Obliczanie adresu skoku

$BTA = (PC + 4) + (L << 2)$

Adresy instrukcji są ułożone w pamięci co 4 bajty. Więc dwa ostatnie bity adresu są zawsze równe 00. Przesunięcie $L$ o << 4 pozwala na uzyskanie czterokrotnie zwiększonego zakresu skoku, bez utraty dokładności.

$L$ w takim przypadku oznacza przesunięcie o indeks intrukcji, ponieważ zawsze przesuwamy o $L * 4$ bajty.

$L$ jest zakodowane w systemie U2, więc możliwe są skoki "do tyłu".

$(PC + 4)$ to aktualny adres następnej do wykonania instrukcji.

_Prezentowanie następnego adresu instrukcji zamiast aktualnego jest podytkowane konwencją, w celu ułatwienia odczytywania schematu działania procesora_

#### Ograniczenie

W związku z tym, że $L$ musi się zmieścić w instrukcji obok $x$ i $y$, które zajmują po 4 bity to zakres skoku jest ograniczony.

#### Dodatkowe elementy

- **<<2**: przesunięcie $L$ o dwa bity w lewo (mnożenie przez 4).
- **PCBranch**: obliczenie BTA.
- **Branch**: pozwala na kompatybilność instrukcji wykonujących skok, z tymi które go nie wykonują.
- **PC'**: pozwala ustalić, czy wykonujemy skok, czy standardowe przesunięcie adresu o 4 bajty.

Wartości sterujące elementami są odpowiednio ustawiane po odczytaniu instrukcji.

#### Wykonanie operacji

1. Przekazanie numeru instrukcji do rejstru rozkazów.
2. Oczytanie instrukcji przez rejestr rozkazów i przesłanie inforacji o niej do pliku rejestrów, oraz informacji o typie operacji do ALU.
3. Odczytanie wartości zmiennych $x$ i $y$ przez rejestr plików i przesłanie ich do ALU.
4. Rozszerzenie reprezentacji L do 32-bitów.
5. Przesunięcie L << 2.
6. Dodanie przesuniętego L do PC w PCBranch.
7. Ustalenie na podstawie wyniku z ALU, czy należy wykonać skok.
8. Wykonanie skoku, czyli przesunięcie adresu o wynik z PCBranch.
