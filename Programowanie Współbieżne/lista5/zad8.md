#### Wait-free

Każdy wątek zawsze kończy swoją operację w skończonej liczbie kroków, niezależnie od innych wątków.​

#### Lock-free

System robi postęp — zawsze jakiś wątek kończy operację.

Pojedynczy wątek może głodować.​

#### Non-blocking/independent

Brak czekania na zamki.

Postęp nie zależy od planisty ani zwalniania zasobów przez innych.​

#### Niezaklszczenie i niezagłodzenie

Zwykle używają zamków, postęp zależy od zwolnienia zamka i/lub fairness planisty, więc są blokujące i zależne.​

#### Zamki != wait-free

Zatrzymanie posiadacza zamka może zatrzymać innych, więc nie spełnia wait-free.​

#### Bounded wait-free

Istnieje jeden stały z góry limit kroków dla wszystkich operacji.

Unbounded wait-free nie ma wspólnego limitu.​

#### `weird()`

jeśli i-te wywołanie kończy się po $2^i$ krokach, to jest wait-free, ale nie bounded wait-free (brak jednego globalnego limitu).​

#### Hierarchia

wait-free $\rightarrow$ lock-free $\rightarrow$ starvation-free $\rightarrow$ deadlock-free
