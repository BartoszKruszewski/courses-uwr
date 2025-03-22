Algorytm polega na przechowywanie przez routery wektora odleglosci do kazdego innego routera oraz ich okresow rozsylaniu miedzy soba w celu zaktualizania tych wektorow.

Poczatkowo wektor odleglosci zawiera tylko informacje o odleglosci do swoich bezposrednich sasiadow. Nastepnie dodaje odleglosci z wektora otrzymanego od sasiadow, bierze minimum wszystkich wynikow i aktualizuje swoje odleglosci.

Stan poczatkowy:

|    | A | B | C | D | E |
|----|---|---|---|---|---|
| A  | - | 1 |   |   |   |
| B  | 1 | - | 1 | 1 |   |
| C  |   | 1 | - | 1 |   |
| D  |   | 1 | 1 | - | 1 |
| E  |   |   |   | 1 | - |
| Su | 1 | 1 |   |   |   |
| Sw |   | 1 |   | 1 |   |
| Sx |   | 1 | 1 | 1 |   |
| Sy |   |   |   | 1 | 1 |
| Sz |   |   | 1 | 1 |   |

1 iteracja:

|    | A         | B         | C         | D         | E         |
|----|-----------|-----------|-----------|-----------|-----------|
| A  | -         | 1         | 2 (via B) | 2 (via B) |           |
| B  | 1         | -         | 1         | 1         | 2 (via D) |
| C  | 2 (via B) | 1         | -         | 1         | 2 (via D) |
| D  | 2 (via B) | 1         | 1         | -         | 1         |
| E  |           | 2 (via D) | 2 (via D) | 1         | -         |
| Su | 1         | 1         | 2 (via B) | 2 (via B) |           |
| Sw | 2 (via B) | 1         | 2 (via B) | 1         | 2 (via D) |
| Sx | 2 (via B) | 1         | 1         | 1         |           | 
| Sy |           | 2 (via D) | 2 (via D) | 1         | 1         |
| Sz |           | 2 (via C) | 1         | 1         | 2 (via D) |

2 iteracja:

|    | A         | B         | C         | D         | E         |
|----|-----------|-----------|-----------|-----------|-----------|
| A  | -         | 1         | 2 (via B) | 2 (via B) | 3 (via D) |
| B  | 1         | -         | 1         | 1         | 2 (via D) |
| C  | 2 (via B) | 1         | -         | 1         | 2 (via D) |
| D  | 2 (via B) | 1         | 1         | -         | 1         |
| E  | 3 (via B) | 2 (via D) | 2 (via D) | 1         | -         |
| Su | 1         | 1         | 2 (via B) | 2 (via B) | 3 (via D) |
| Sw | 2 (via B) | 1         | 2 (via B) | 1         | 2 (via D) |
| Sx | 2 (via B) | 1         | 1         | 1         | 3 (via D) | 
| Sy | 3 (via B) | 2 (via D) | 2 (via D) | 1         | 1         |
| Sz | 3 (via B) | 2 (via C) | 1         | 1         | 2 (via D) |

Stan stabilny