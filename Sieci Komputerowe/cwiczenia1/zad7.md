Stan poczatkowy (jak w poprzednim zadaniu ale A i E wiedza o sobie):

|    | A         | B         | C         | D         | E         |
|----|-----------|-----------|-----------|-----------|-----------|
| A  | -         | 1         | 2 (via B) | 2 (via B) | 1         |
| B  | 1         | -         | 1         | 1         | 2 (via D) |
| C  | 2 (via B) | 1         | -         | 1         | 2 (via D) |
| D  | 2 (via B) | 1         | 1         | -         | 1         |
| E  | 1         | 2 (via D) | 2 (via D) | 1         | -         |
| Su | 1         | 1         | 2 (via B) | 2 (via B) | 3 (via D) |
| Sw | 2 (via B) | 1         | 2 (via B) | 1         | 2 (via D) |
| Sx | 2 (via B) | 1         | 1         | 1         | 3 (via D) | 
| Sy | 3 (via B) | 2 (via D) | 2 (via D) | 1         | 1         |
| Sz | 3 (via B) | 2 (via C) | 1         | 1         | 2 (via D) |
| Sq | 1         |           |           |           | 1         |

1 iteracja:

|    | A         | B         | C         | D         | E         |
|----|-----------|-----------|-----------|-----------|-----------|
| A  | -         | 1         | 2 (via B) | 2 (via B) | 1         |
| B  | 1         | -         | 1         | 1         | 2 (via D) |
| C  | 2 (via B) | 1         | -         | 1         | 2 (via D) |
| D  | 2 (via B) | 1         | 1         | -         | 1         |
| E  | 1         | 2 (via D) | 2 (via D) | 1         | -         |
| Su | 1         | 1         | 2 (via B) | 2 (via B) | 2 (via A) |
| Sw | 2 (via B) | 1         | 2 (via B) | 1         | 2 (via D) |
| Sx | 2 (via B) | 1         | 1         | 1         | 3 (via D) | 
| Sy | 2 (via E) | 2 (via D) | 2 (via D) | 1         | 1         |
| Sz | 3 (via B) | 2 (via C) | 1         | 1         | 2 (via D) |
| Sq | 1         | 2 (via A) |           | 2 (via E) | 1         |

2 iteracja:

|    | A         | B         | C         | D         | E         |
|----|-----------|-----------|-----------|-----------|-----------|
| A  | -         | 1         | 2 (via B) | 2 (via B) | 1         |
| B  | 1         | -         | 1         | 1         | 2 (via D) |
| C  | 2 (via B) | 1         | -         | 1         | 2 (via D) |
| D  | 2 (via B) | 1         | 1         | -         | 1         |
| E  | 1         | 2 (via D) | 2 (via D) | 1         | -         |
| Su | 1         | 1         | 2 (via B) | 2 (via B) | 2 (via A) |
| Sw | 2 (via B) | 1         | 2 (via B) | 1         | 2 (via D) |
| Sx | 2 (via B) | 1         | 1         | 1         | 3 (via D) | 
| Sy | 2 (via E) | 2 (via D) | 2 (via D) | 1         | 1         |
| Sz | 3 (via B) | 2 (via C) | 1         | 1         | 2 (via D) |
| Sq | 1         | 2 (via A) | 3 (via B) | 2 (via E) | 1         |

Stan stabilny