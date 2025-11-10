#### Konstrukcja

Bierzemy dwa niezależne atomowe rejestry 32-bit MRMW i zapisujemy do nich wartości po sobie sekwencyjnie. Odczyt również robimy sekwencyjnie 

#### Regularność i atomowość (nie zachodzi)

Można odczytać starszą "górną" połówkę i nowszą "dolną" lub odwrotnie. Regularnosć wymaga aby została zwrócona aktualna lub poprzednia wartość, ale nie mieszana.

Jeżeli nie zachodzi regularność to atomowość też nie.

#### Bezpieczeństwo

Jest spełnione, ponieważ mamy zapewnione atomowe MRMW, czyli wartości zostaną zapisane poprawnie. Mogą być mieszane, ponieważ bezpieczeństwo zakłada tylko tyle, że wartości mają być zgodne typem.

Rejestr działa prawidłowo dla nienachodzących na siebie operacjach, ponieważ najpierw zostaną zapisane oba rejestry 32-bit, a następnie odczytane.