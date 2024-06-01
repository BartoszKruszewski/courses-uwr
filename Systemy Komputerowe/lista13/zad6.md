#### Technika wykładniczego uśrednienia

Jest to sposób predykcji długości następnego procesu na podstawie poprzednich, wykonanych już procesów, według wzoru:

$\tau_{n+1} = \alpha \cdot t_n + (1 - \alpha)\tau_n$

- $\tau_{n+1}$ - przewidywana długość obecnego procesu
- $\tau_{n}$ - przewidywana długość poprzedniego procesu
- $t_n$ - faktyczna długość poprzeniego procesu
- $\alpha$ - stała, $0 \leq \alpha \leq 1$, (najczęściej $\alpha = \frac{1}{2}$)

#### SRT (Shortest Remaining Time)

Jest to wariant wywłaszczający algorytmu SJF. Aktualizacja kolejności procesów odbywa się dokładnie w momencie wprowadzenia nowego procesu, bez czekania na zakończenie obecnie wykonywanego jak w przypadku standardowego SJF.

#### Obliczenia $\alpha = 0$ i $\tau_0 = 100 ms$

$\tau_{n+1} = 0 \cdot t_n + (1 - 0)\tau_n = \tau_n$

Pomijamy faktyczne czasy wykonanie. Zakładamy że każda faza będzie trwać $100ms$.

#### Obliczenia $\alpha = 0.99$ i $\tau_0 = 10 ms$

$\tau_{n+1} = 0.99 \cdot t_n + (1 - 0.99)\tau_n = 0.99 \cdot t_n + 0.01 \cdot \tau_n$

Prawie pomijamy poprzednie predykcje. Każda następna predkcja będzie mniej więcej równa z faktycznym czasem wykonania poprzedniego procesu.
