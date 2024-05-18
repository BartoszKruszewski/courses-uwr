#### Opis zadania

- **Misprediction Penalty**: kara za błędne przewidywanie
- **Buffer Miss Penalty**: kara za błędne przewidywanie w buforze skoków
- **Hit Rate**: procentowa ilość trafień w buforze
- **Accuracy**: skuteczność przewidywania skoków
- **Branch Frequency**: częstotliwość występowania skoków w programie
- **Fixed Branch Penalty**: stała kara czasowa za skok

#### Procesora bez bufora:

Kara za przewidywanie skoku:
$branch frequency * branch penalty = 0,15 * 2 = 0,3$

#### Procesora z branch target buffer

Kara za brak trafienia w buforze 
$branch frequency * (1 - hit rate) * buffer miss penalty = 0.15 * (1 - 0.9) * 3 = 0.045$
Koszt przewidywania skoku:
$branch Frequency * hit rate * (1 - accuracy) = 0.15 * 0,9 * (1 - 0,9) * 4 = 0,054$
  
Łączny koszt:
$0,045 + 0,054 = 0,099$

#### Porównanie
Dla procesora bez bufora skoków:
$1 + 0,3 = 1,3$

Dla procesora z buforem skoków:
$1 + 0,099 = 1,099$

Ich stosunek:
$1,3 / 1,099 = 1,1829$
Procesor z branch target buffer jest około 18% szybszy.
