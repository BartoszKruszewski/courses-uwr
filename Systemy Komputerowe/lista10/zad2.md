#### Mapowanie bezpośrednie

Mapowanie bezpośrednie występuje, kiedy w każdym zbiorze mamy tylko jeden blok.

#### A

Offset ma 5 bitów, czyli liczba możliwych offsetów to $2^{5} = 32$, więc blok ma rozmiar $32$ bajtów.

#### B

Indeksy mają 5 bitów, czyli liczba możliwych indeksów to $2^{5} = 32$, więc pamięc ma $32$ wiersze.

#### C

Dane składowane są na 32-bajtach, jak wynika z podpunktu A, więc mamy 32 \* 8 bitów.
Metadane to tag oraz valid, więc razem 23.

```
(32 * 8) / (22 + 1) = 11.13
```
