#### Dowód dla dwóch wątków

Dla wątków $A$ i $B$:

Zakłóżmy nie wprost, że jeden rejestr $R$ wystarczy dla dwóch wątków.

$B$ zatrzymuje się tuż przed zapisem do $R$.

$A$ zapisuje do $R$ i wchodzi do $CS$

$B$ wykonuje swój zapis do $R$.

Wtedy cały ślad pozostawiony przez $A$ zostaje wymazany.

Algorytm spełnia niezakleszczenie, więc $B$ nie mając śladu $A$ wchodzi do $CS$.

Wtedy oba wątki są w $CS$, więc mamy sprzeczność z własnością wzajemnego wykluczenia.

#### Uogólnienie na $n$ wątków

Założenie indukjcyjne: Potrzeba co co najmniej $n$ współdzielonych rejestrów dla $n$ wątków. 

**Krok bazowy:** dla $n = 2$ udowodniliśmy

**Krok indukcyjny:**

Założmy, że potrzeba co co najmniej $n$ współdzielonych rejestrów dla $n$ wątków.

Do udowodnienia: potrzeba co co najmniej $n + 1$ współdzielonych rejestrów dla $n + 1$ wątków.

Załóżmy nie wprost, że wystarczy $n$ współdzielonych rejestrów dla $n + 1$ wątków.

Oznaczmy $n + 1$-szy wątek jako $C$.

$B$ zatrzymuje się tuż przed zapisem do rejestrów.

$n$ pozostałych wątków zapisuje do $n$ potrzebnych rejestrów i jeden z nich wchodzi do $CS$.

$B$ zapisuje dane do jakiegoś rejestru.

Wtedy cały ślad pozostawiony przez jakiś inny wątek zostaje wymazany.

Możliwe jest, że był to wątek, który wszedł do $CS$.

Algorytm spełnia niezakleszczenie, więc jakiś wątek nie mając śladu wątku, który jest już w $CS$ wchodzi do $CS$.

Wtedy dwa wątki są w $CS$, więc mamy sprzeczność z własnością wzajemnego wykluczenia.

Więc potrzeba co najmniej $n + 1$ współdzielonych rejestrów dla $n + 1$ wątków.
