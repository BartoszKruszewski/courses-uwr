#### Intuicja

Algorytm opiera się na buforowaniu instrukcji, w celu zachowania ich oryginalnej kolejnośći.

#### Algorytm

1. Pobieranie instrukcji
2. Dodanie instrukcji na kolejkę
3. Równoległe obliczanie instrukcji, jeżeli jej zasoby są dostępne, ale bez zapisywania
4. Jeżeli najstarsza instrukcja została obliczona to zapisujemy ją i usuwamy z kolejki

#### Rozwiązania hazardów

**RAW**: zapisujemy instrukcje w oryginalnej kolejności
**WAR**: instrukcje mają sprawdzaną dostępność zasobów przed rozpoczęciem obliczania
**WAW**: zapisujemy instrukcje w oryginalnej kolejności

#### Porwónanie ze Scoreboardem

Reorder buffer wykonuje dużo operacji na buforze, do sprawdzania dostępnośći zasobów. Natomiast Scoreboard sprawdza wykorzystanie zasobów procesora i blokuje instrukcje, które wykorzystują zajęte rejestry.

Reorder buffer zapewnia precyzyjną obsułgę wyjątków w przeciwieństwie do Scoreboardu.
