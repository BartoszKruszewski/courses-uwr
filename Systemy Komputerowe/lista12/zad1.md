#### Potencjalne błędy stron

Zauważmy, że w zapytaniach 0 1 7 2 3 2 7 1 0 3 mamy 5 różnych stron, więc pamięć wirtualna, która ma pojemność 8 stron nigdy nie zostanie przepełniona, więc wystarczy analizować pamięć fizyczną.

#### Algorytm FIFO

System operacyjny utrzymuje listę wszystkich stron, które aktualnie znajdują się w pamięci,
przy czym strony dodane
jako ostatnie znajdują się na końcu, natomiast te dodane najwcześniej — na początku. W przy-
padku wystąpienia błędu braku strony strona znajdująca się na początku listy jest usuwana,
a nowa strona jest umieszczana na końcu listy. W odniesieniu do sklepu zastosowanie algo-
rytmu FIFO może doprowadzić do usunięcia wosku do wąsów, ale także mąki, soli czy masła.
W przypadku komputerów występuje ten sam problem: najstarsza strona w dalszym ciągu może
być potrzebna. Z tego powodu algorytm FIFO w klasycznej postaci jest rzadko używany.

```
0 -> 0       miss
1 -> 1 0     miss
7 -> 7 1 0   miss
2 -> 2 7 1 0 miss
3 -> 3 2 7 1 swap
2 -> 3 2 7 1
7 -> 3 2 7 1
1 -> 3 2 7 1
0 -> 0 3 7 2 swap
3 -> 0 3 7 2
```

Liczba błędów: $6$

#### Algorytm LRU

```
0 -> 0       miss
1 -> 1 0     miss
7 -> 7 1 0   miss
2 -> 2 7 1 0 miss
3 -> 2 7 1 3 swap
2 -> 2 7 1 3
7 -> 2 7 1 3
1 -> 2 7 1 3
0 -> 2 7 1 0 swap
3 -> 2 7 1 3 swap
```

Liczba błędów: $7$
