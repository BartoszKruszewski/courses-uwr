#### Klienci są obsługiwani zgodnie z kolejnością przybycia.

Bezpieczeństwo, ponieważ mamy kolejkę gwarantującą obsługiwanie jednego klienta na raz.

#### Co idzie do góry, musi zejść na dół.

Żywotność, bo pozwalamy na dostęp do zasobów, ale zakładamy że zostaną zwolnione "kiedyś" bez gwarancji kiedy.

#### Jeśli co najmniej dwa wątki oczekują na wejście do sekcji krytycznej, to przynajmniej jednemu to się udaje.

Żywotność z definicji

#### Jeśli nastąpi przerwanie, to w ciągu sekundy drukowany jest komunikat.

Bezpieczeństwo, ponieważ mamy gwarancję czasu wydrukowania komunikatu, natomiast wymaga to dodanie do protokołu przeczekania czasu bezwładnośći.

####  Jeśli nastąpi przerwanie, to drukowany jest komunikat.

Żywotność, ponieważ nie wiemy po jakim czasie pojawi się komunikat

#### Koszt życia nigdy nie spada.

Bezpieczeństwo - "nigdy nic złego się nie stanie", zakładając, że koszt życia jest porządany

#### Dwie rzeczy są pewne: śmierć i podatki.

Żywotność - "kiedyś stanie się coś pożądanego", zakładając że porządamy śmierci i podatów
