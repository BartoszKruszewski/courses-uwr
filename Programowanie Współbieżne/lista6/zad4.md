#### Warunek (*)

*Dla każdego $i$ nie jest prawdą, że $ R^i \rightarrow W^i$*

Oznacza to, że odczyt wartości zapisanej przez i-ty zapis nigdy nie wystąpi przed tym zapisem.

#### Warunek (**)

*Dla każdych $i$ oraz $j$ nie jest prawdą, że $W^i$ \rightarrow W^j \rightarrow R^i$*

Oznacza to, że odczyt wartości zapisanej przez i-ty zapis nigdy nie wystąpi, jeżeli pomiędzy tym zapisem był dowolny inny zapis.

#### jeżeli (*) oraz (**) to rejestr jest regularny

Rozważmy przypadki:

1. Odczyt nie jest współbieżny z żadnym zapisem.

    Załóżmy wtedy nie wprost, że odczytał z innego zapisu niż z poprzedniego.
    
    Z faktu, że rejestr jest dobry wiemy, że wartość musi pochodzić z jakiegoś zapisu.

    Jeśli odczytana pochodzi z przyszłego zapisu to mamy sprzeczność na podstawie (*).

    W przeciwnym przypadku mamy sprzeczność na podstawie (**).

2. Odczyt $R^i$ jest współbieżny z zapisami $W^a, W^b, \dots W^z$.

    Przez $W^A$ oznaczmy ostatni zapis nie współbieżny z $R^i$.

    Na podstawie (*) wiemy, że zapis nie pochodzi z przyszłości.
    
    W połączeniu z faktem, że rejestr jest dobry wiemy, że odczytana wartość pochodzi z jednego z zapisów $W^a, W^b, \dots W^z$ lub $W^A$ lub zapisu $W^B$ takiego, że $W^B \rightarrow R^i$.
    
    Jednak na podstawie (**) wiemy, że opcja odczytu z $W^B$ nie jest możliwa, ponieważ ostatni zapis to $W^A$. 

#### jeżeli rejestr jest regularny to (*) oraz (**)

(*) załóżmy nie wprost, że istnieje takie i dla których $ R^i \rightarrow W^i$

Rejestr jest regularny, więc dla $R^i$: $W^i$ musiał być ostatnim lub przedostatnim zapisem.

Może zajść tylko jedno $W^i$, a $R^i$ odbyło się przed nim, stąd sprzeczność.

(**) Rejestr regularny zwraca aktualną wartość dla niepokrywających się zapisów i odczytów.

Załóżmy nie wprost, że istnieją $i$ oraz $j$ dla których $W^i$ \rightarrow W^j \rightarrow R^i$

Wtedy w szczególności $W^j \rightarrow R^i$ co jest sprzeczne bo $W^j$ jest aktualne.