# CPU Inheritance Scheduling

## Definicja

CPU Inheritance Scheduling to mechanizm szeregowania procesów, opracowany przez Bryana Forda i Sai Susarlę z Uniwersytetu Utah w 1996 roku. Algorytm ten umożliwia wątkom działanie jako szeregatory dla innych wątków, co pozwala na elastyczne zarządzanie priorytetami i czasem CPU. Dzięki dziedziczeniu priorytetów, CPU Inheritance Scheduling skutecznie zapobiega problemom takim jak inwersja priorytetów.

## Główne założenia

1. **Modularność**: Umożliwienie wątkom działanie jako szeregatory innych wątków.
2. **Elastyczność**: Pozwolenie na różnorodne polityki szeregowania w ramach jednego systemu.
3. **Hierarchiczność**: Umożliwienie tworzenia złożonych hierarchii szeregowania, które mogą być dostosowane do specyficznych potrzeb administracyjnych i aplikacyjnych.

## Zalety algorytmu

1. **Zróżnicowane polityki szeregowania**: Umożliwia implementację różnych polityk szeregowania, które mogą być dostosowane do indywidualnych potrzeb aplikacji. Na przykład, aplikacje czasu rzeczywistego mogą wymagać różnych strategii szeregowania niż aplikacje multimedialne.
2. **Priorytetowa inwersja**: Nowe podejście zapewnia generalizowaną formę dziedziczenia priorytetów, która minimalizuje problem inwersji priorytetów. Wątki mogą dziedziczyć priorytety od innych wątków, co zapewnia bardziej sprawiedliwe i efektywne wykorzystanie czasu procesora.
3. **Multiprocessing i procesory wielordzeniowe**: CPU Inheritance Scheduling jest naturalnie skalowalne do systemów wieloprocesorowych, umożliwiając efektywne zarządzanie zasobami procesora w środowiskach z wieloma rdzeniami.
4. **Techniki powiązania procesora**: Umożliwia implementację technik powiązania procesora (processor affinity), które pozwalają na lepsze wykorzystanie cache procesora i zwiększenie wydajności aplikacji.
5. **Aktywacje szeregatora**: Wspiera mechanizm aktywacji szeregatora (scheduler activations), który umożliwia lepsze zarządzanie wątkami i zasobami procesora w systemach operacyjnych.

## Przykład hierarchii szeregowania

![Hierarchia Szeregowania](hierarchy.jpg)

## Mechanizm przekazywania czasu procesora

1. **Delegacja czasu CPU**: Wątek szeregator może przekazać część lub całość swojego przydziału czasu CPU innemu wątkowi.
2. **Dziedziczenie priorytetów**: Wątek, który otrzymuje czas procesora, dziedziczy również priorytety wątku szeregatora. Zapewnia to, że wątki o wysokim priorytecie nie będą blokowane przez wątki o niższym priorytecie.

Rozważmy scenariusz, w którym mamy trzy wątki: A, B i C. Wątek A działa jako szeregator dla wątków B i C. W pewnym momencie wątek A decyduje, że wątek B potrzebuje więcej czasu procesora, aby zakończyć ważne zadanie.

1. **Przekazanie czasu**: Wątek A przekazuje część swojego czasu procesora do wątku B.
2. **Dziedziczenie priorytetów**: Wątek B dziedziczy priorytet wątku A, co oznacza, że teraz ma taki sam priorytet jak wątek A.
3. **Wykorzystanie czasu CPU**: Wątek B wykorzystuje przydzielony czas CPU, aby ukończyć swoje zadanie. Po zakończeniu, pozostały czas może zostać zwrócony do wątku A lub przekazany do wątku C, w zależności od potrzeb.

CPU Inheritance Scheduling zawiera mechanizmy powiadamiania, które informują wątki o zmianach w przydziale czasu CPU. Dzięki temu wątki mogą dynamicznie dostosowywać swoje działania. Proces ten przebiega następująco:

1. **Powiadomienie**: Gdy wątek A przekazuje czas procesora do wątku B, system powiadamia wątek B o nowym przydziale czasu CPU.
2. **Reakcja wątku**: Wątek B, otrzymawszy powiadomienie, może odpowiednio dostosować swoje działania, np. przyspieszyć realizację zadania, które wcześniej było opóźniane z powodu braku zasobów CPU.
3. **Ponowne przydzielanie**: Po zakończeniu zadania przez wątek B, system może ponownie przydzielić pozostały czas CPU. Jeśli wątek B zakończy swoje zadanie przed wyczerpaniem przydzielonego czasu, pozostały czas może zostać przekazany z powrotem do wątku A lub do innego wątku, który potrzebuje zasobów.

## Zarządzanie priorytetami i inwersja priorytetów

Jednym z kluczowych problemów w tradycyjnych systemach szeregowania jest inwersja priorytetów. CPU Inheritance Scheduling minimalizuje ten problem poprzez mechanizm dziedziczenia priorytetów. Wątek, który otrzymuje czas CPU od innego wątku, dziedziczy również jego priorytet. Dzięki temu wątki o wysokim priorytecie mogą kontynuować pracę bez blokowania przez wątki o niższym priorytecie.

## Systemy wieloprocesorowe

1. **Rozkład obciążenia**: Efektywne rozłożenie obciążenia między procesory, co prowadzi do lepszego wykorzystania zasobów systemowych.
2. **Powiązanie procesora (processor affinity)**: Możliwość przypisywania wątków do określonych procesorów, co może zwiększyć efektywność poprzez lepsze wykorzystanie pamięci podręcznej (cache).
3. **Aktywacje szeregatora (scheduler activations)**: Mechanizm ten umożliwia lepsze zarządzanie zasobami CPU i wątkami poprzez dynamiczne aktywacje szeregatorów, co poprawia responsywność i wydajność systemu.

## Implementacja

Structura danych: Wątek
- Każdy wątek posiada priorytet, przydział czasu CPU oraz referencję do swojego szeregatora.
- Wątki mogą dziedziczyć priorytety od innych wątków.

Structura danych: Szeregator
- Szeregator zarządza kolejką wątków gotowych do wykonania.
- Szeregator posiada metody do dodawania wątków, wybierania następnego wątku do wykonania oraz aktualizowania priorytetów wątków.

Dodawanie wątku do szeregatora
- Wątek jest dodawany do kolejki szeregatora.
- Szeregator decyduje o priorytecie wątku i umieszcza go w odpowiednim miejscu w kolejce.

Wybór kolejnego wątku do wykonania
- Szeregator wybiera następny wątek do wykonania na podstawie priorytetów.
- Wątek o najwyższym priorytecie jest wybierany jako pierwszy.

Przekazywanie czasu CPU
- Wątek przekazuje część swojego czasu CPU innemu wątkowi.
- Priorytet przekazującego wątku jest dziedziczony przez odbiorcę.

Aktualizacja priorytetu wątku
- Szeregator aktualizuje priorytet wątku na nowy priorytet.
- Wątek jest ponownie umieszczany w kolejce priorytetowej.

Zapobieganie inwersji priorytetów
- Jeśli wątek przekazujący priorytet ma wyższy priorytet niż odbiorca, priorytet odbiorcy jest aktualizowany na wyższy.
- Mechanizm ten zapobiega blokowaniu wątków o wysokim priorytecie przez wątki o niższym priorytecie.

Rozkład obciążenia między procesorami
- Szeregator rozdziela wątki między różne procesory, aby zapewnić równomierne obciążenie.
- Każdy procesor wykonuje wątki przydzielone przez szeregator.

Powiązanie procesora 
- Wątek może być przypisany do określonego procesora, co zwiększa wydajność.
- Przypisanie wątku do procesora zapewnia lepsze wykorzystanie pamięci podręcznej procesora.

Inicjalizacja szeregatora
- System operacyjny inicjalizuje szeregatory dla każdego procesora podczas uruchamiania.
- Tworzone są nowe instancje szeregatorów dla każdego procesora.


## Porównanie z innymi metodami szeregowania

### Tradycyjne metody priorytetowe

Tradycyjne metody priorytetowe obejmują różne algorytmy szeregowania, takie jak **Fixed-Priority Scheduling** i **Round Robin**. Każda z tych metod ma swoje zalety i wady.

#### Fixed-Priority Scheduling
- **Zalety**:
  - Prosta implementacja.
  - Stałe priorytety ułatwiają przewidywalność zachowania systemu.
- **Wady**:
  - Problem inwersji priorytetów, gdzie wątki o wysokim priorytecie mogą czekać na zakończenie pracy wątków o niższym priorytecie.
  - Brak elastyczności w dynamicznym dostosowywaniu priorytetów wątków.

#### Round Robin
- **Zalety**:
  - Sprawiedliwe przydzielanie czasu CPU, gdzie każdy wątek otrzymuje równą szansę na wykonanie.
  - Prosta implementacja, dobra dla systemów bez twardych wymagań czasowych.
- **Wady**:
  - Może prowadzić do marnowania zasobów CPU, jeśli wątki często zmieniają kontekst.
  - Brak wsparcia dla priorytetów, co może być problematyczne dla aplikacji czasu rzeczywistego.

### Metody wieloklasowe

Metody wieloklasowe, takie jak **Multilevel Queue Scheduling** i **Multilevel Feedback Queue**, oferują bardziej złożone podejście do szeregowania.

#### Multilevel Queue Scheduling
- **Zalety**:
  - Możliwość separacji wątków o różnych priorytetach do różnych kolejek.
  - Lepsze zarządzanie różnymi typami zadań (np. zadania interaktywne vs. zadania wsadowe).
- **Wady**:
  - Skomplikowana konfiguracja i zarządzanie.
  - Problem głodzenia (starvation) wątków o niższym priorytecie.

#### Multilevel Feedback Queue
- **Zalety**:
  - Dynamiczne dostosowywanie priorytetów wątków w zależności od ich zachowania i potrzeb.
  - Lepsza wydajność w systemach z mieszanymi obciążeniami.
- **Wady**:
  - Skuteczność zależy od dobrze dobranych parametrów, co może być trudne do osiągnięcia.
  - Większa złożoność implementacji.

### Porównanie z CPU Inheritance Scheduling

**CPU Inheritance Scheduling** oferuje unikalne podejście, które łączy zalety tradycyjnych metod priorytetowych i metod wieloklasowych, jednocześnie minimalizując ich wady.

#### Elastyczność i modularność
- **Tradycyjne metody priorytetowe** i **metody wieloklasowe** mają ograniczoną elastyczność w dostosowywaniu priorytetów i polityk szeregowania.
- **CPU Inheritance Scheduling** umożliwia dynamiczne dziedziczenie priorytetów i elastyczne przekazywanie czasu CPU między wątkami, co pozwala na lepsze dostosowanie do bieżących potrzeb aplikacji i systemu.

#### Rozwiązywanie problemu inwersji priorytetów
- W tradycyjnych metodach priorytetowych problem inwersji priorytetów jest poważnym ograniczeniem.
- **CPU Inheritance Scheduling** minimalizuje ten problem poprzez mechanizm dziedziczenia priorytetów, gdzie wątki mogą przejmować priorytety od innych wątków, zapewniając bardziej efektywne wykorzystanie czasu CPU.

#### Zarządzanie w środowiskach wieloprocesorowych
- Tradycyjne metody i metody wieloklasowe mogą mieć trudności z efektywnym zarządzaniem czasem CPU w systemach wieloprocesorowych.
- **CPU Inheritance Scheduling** jest naturalnie skalowalne do systemów wieloprocesorowych, umożliwiając efektywne rozłożenie obciążenia i lepsze zarządzanie zasobami procesora.

### Podział zastosowań
- **Tradycyjne metody** są często stosowane w prostych systemach, gdzie przewidywalność jest ważniejsza niż elastyczność.
- **Metody wieloklasowe** są używane w systemach, gdzie różne typy zadań muszą być efektywnie zarządzane.
- **CPU Inheritance Scheduling** znajduje zastosowanie w złożonych systemach, gdzie różne aplikacje mają różne wymagania dotyczące zasobów CPU i gdzie dynamiczne dostosowywanie priorytetów jest kluczowe.

## Podsumowanie

CPU Inheritance Scheduling to zaawansowany algorytm szeregowania procesorów, który zyskał zainteresowanie głównie w środowiskach akademickich i badawczych, a jego popularność w komercyjnych systemach operacyjnych jest ograniczona. Jego elastyczność i zdolność do zarządzania różnymi politykami szeregowania w ramach jednego systemu sprawiają, że jest szczególnie użyteczny w systemach czasu rzeczywistego i eksperymentalnych projektach badawczych. Pomimo swojego potencjału, CIS nie jest powszechnie stosowany w praktycznych implementacjach komercyjnych systemów operacyjnych.