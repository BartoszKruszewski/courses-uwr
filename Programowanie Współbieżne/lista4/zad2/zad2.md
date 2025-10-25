#### Diagram 1

`r.write(1) => r.read(1) => r.write(2) => r.read(2)`

#### Diagram 2

`r.write(2) => r.write(1) => r.read(1) => r.read(1)`

#### Diagram 3

Nie ma wspólnego czasu w którym `y` mogłoby trafić do kolejki jako pierwsze, więc nielinearyzowalne.

#### Diagram 4

Rozważając samą kolejkę $p$ występuje sytuacja analogiczna jak na diagramie 3.

