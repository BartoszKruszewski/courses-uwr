#### Redukcja

Wynikiem takiego protokołu jest wspólna ustalona wartość przez $n$ wątków.

Wiemy, że $n > 2$, więc istnieją dwa pierwsze wątki A oraz B, które ustaliły wartość taką samą jak wszystkie inne, gdzie wszystkie wybierają spośród $0$ i $1$.

Protokół jest wait-free, więc wątki zakończą działanie w skończonej liczbie kroków.

#### Dowód

Załóżmy, że taka implementacha dla n wątków istnieje.

Pokazaliśmy, że można ją zredukować do implementacji dla 2 wątków.

Wiemy, że implementacja dla 2 wątków nie istnieje, zatem mamy sprzeczność.
