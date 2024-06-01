#### Planowanie wywłaszczające

CPU Scheduler może "wywłaszczyć" program poprzez przełączanie stanu "running" na "ready", żeby potem móc przywrócić z "ready" na running". W takim planowaniu CPU Scheduler manipuluje też momentem zmiany stanu procesu z "waiting" na "ready".

#### Planowanie niewywłaszczające

CPU Scheuduler mało ingeruje w przełączanie stanów procesu. Stany procesów przełączane są tylko wtedy, kiedy muszą być przełączone "running" na "waiting" oraz z "running" na "terminated".

#### Proces ograniczony przez dostęp do procesora

Proces, który wymaga długiego dostępu do procesora (np jakieś trudne obliczenia).

#### Proces ograniczony przez wejście/wyjście

Proces, który wymaga dużo oczekiwania na wykonanie operacji wejścia/wyjścia.

#### Proces interaktywny

Proces, którego głównym zadaniem jest interakcja z użytkownikiem, więc występuje z nim dużo operacji wejścia/wyjścia.

#### Proces wsadowy

Proces "wewnętrzny" dla komputera, nie występują w nim interakcje z użytkownikiem.

#### Dlaczego planowanie wywłaszczające jest lepsze?

Planowanie wywłaszczające pomimo tego, że jest trudniejsze w implementacji, pozwala na uzyskanie "iluzji równoległości" działania programów. Jeżeli nie moglibyśmy przełączyć procesu w dowolnym momencie to programy wykonywałyby się w kolejności uruchomienia do momentu, aż się wykonają albo czekają na inny proces. Uniemożliwiałoby to interaktywne korzystanie z komputera.
