Wybieramy jedną osobę która będzie "licznikiem". Będzie ona "wewnętrznie" zliczać ilość pozostałych więźniów, którzy już odwiedzili przełącznik.

Pozostali więźniowie muszą jedynie pamiętać czy już wcześniej odwiedzili przełącznik.

#### Protokół licznika

Jeżeli przełącznik jest:
- wyłączony: nic nie rób
- włączony: wyłącz przełącznik i zwiększ wewnętrzny licznik o $1$. Kiedy licznik będzie równy $n-1$ poinformuj strażnika.

#### Pozostali

Jeżeli przełącznik jest:
- wyłączony: włącz przełącznik, jeżeli wcześniej go jeszcze nie odwiedziłeś
- włączony: nic nie rób

#### Intuicja

Każdy "nielicznik" poprzez włączenie przełącznika melduje się tylko raz. Jego stan może zmienić jedynie "licznik", więc mamy pewność, że zauważy każdy zmianę i ją uwzględni.
