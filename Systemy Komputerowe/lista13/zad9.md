#### Idea algorytmu

Chcemy mieć możliwość w miarę sprawiedliwego podziału procesora na kilku użytkowników. W tym celu przypisujemy użytkowników do grup. Każda grupa będzie miała przydzieloną równą ilość czasu procesora, niezależnie od liczby procesów.

#### Obliczanie priorytetów

$priority=CPU/constant + Group/constant + base + nice value$

- $CPU$: ostatni czas wykrzystania procesora
- $Group$: ostatni czas wykorzystania procesa przez grupę
- $base$: priorytet ręcznie nadany przez użtykownika
- $nice$: dodatkowy priorytet nadany przez superusera
