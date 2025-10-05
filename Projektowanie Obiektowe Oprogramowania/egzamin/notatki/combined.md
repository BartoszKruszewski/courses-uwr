# Wykład 1 - Unified Process

## 1. Unified Process (UP)

Unified Process to ramowy proces tworzenia oprogramowania składający się z faz:
- inicjowania,
- projektowania,
- implementacji,
- testowania,
- wdrażania.

Diagram procesowy pokazuje iteracyjny charakter UP:

analiza → projekt → implementacja → testy → wdrożenie → kolejna iteracja

## 2. Faza rozpoczęcia (Business Modelling)

Określenie zakresu, wizji i uwarunkowań biznesowych.

### Artefakty:
- **Wizja i analiza biznesowa** – cele i uwarunkowania.
- **Słowniczek** – terminologia dziedzinowa.
- **Prototyp** – weryfikacja techniczna.
- **Plan pierwszej iteracji**.
- **Specyfikacja dodatkowa** – wymagania wpływające na architekturę.
- **Plan zarządzania ryzykiem** – scenariusze alternatywne (biznesowe, techniczne).

## 3. Zbieranie wymagań (Requirements)

### 3.1 FURPS+
**FURPS** to klasyfikacja wymagań:
- **F**unctional – funkcje, bezpieczeństwo
- **U**sability – UX, pomoc
- **R**eliability – niezawodność
- **P**erformance – wydajność
- **S**upportability – utrzymanie

**+** obejmuje:
- Design, Implementation, Interface, Physical.

### Typowe problemy:
- Wszystko ma być zrobione („shopping cart mentality”).
- Brak priorytetów.
- Niejednoznaczne/niemierzalne wymagania.

### Wymagania regulacyjne:
- RODO, KRI, Ustawa o dostępności cyfrowej, WCAG 2.0.

### 3.2 S.M.A.R.T.
Kryteria dla dobrych wymagań:
- **S**imple
- **M**easurable
- **A**chievable
- **R**elevant
- **T**ime-specific

#### Przykład SMART:
- System dostępny przez przeglądarkę bez dodatkowego oprogramowania.
- Średni czas odpowiedzi < 5 sek.

## 4. Projektowanie analityczne – przypadki użycia

### Definicja:
Opis interakcji użytkownika (aktora) z systemem w formie scenariusza.

### Typy dokumentacji:
- **Brief** – krótki opis.
- **Fully dressed** – szczegółowy opis: poziom, warunki początkowe i końcowe, scenariusz sukcesu, alternatywy, wyjątki.

### Przykład Gherkin:
Feature: zarządzanie zbiorem kontrahentów

Scenario: dodawanie kontrahenta
- Given: jestem zalogowany jako ADMIN
- When: dodaję kontrahenta z poprawnymi danymi
- Then: kontrahent zostaje 

# Wykład 2 - UML

## Wprowadzenie

UML składa się z **diagramów struktur** (statyczne elementy systemu) oraz **diagramów zachowań** (dynamiczne procesy).

Narzędzia do UML:
- Lekkie: draw.io, yuml.me, umletino
- Profesjonalne: Enterprise Architect (płatne), Visual Paradigm (darmowa wersja Community)

## Diagramy klas

Służą do reprezentacji modeli pojęciowych, klas obiektowych oraz schematów relacyjnych baz danych.

### Hierarchia modeli

#### 1. Diagram modelu pojęciowego
- Ustalanie wspólnego języka w projekcie (bez dziedziczenia i metod)
- Tylko publiczne atrybuty i relacje (asocjacje) między pojęciami

#### 2. Diagram modelu obiektowego (klas)
- Refaktoryzacja modelu pojęciowego:
  - Usuwanie zbędnych pojęć
  - Dodawanie klas pomocniczych
  - Dodawanie metod, widoczności, typów relacji (asocjacje, agregacje, kompozycje, dziedziczenie)
- Na tym etapie wszystkie relacje muszą być implementowalne w języku obiektowym

#### 3. Diagram modelu implementacyjnego (relacyjnego)
- Struktura fizyczna bazy danych:
  - Bez metod i dziedziczenia (zastępowane przez:
    - Table-per-concrete-type
    - Table-per-hierarchy
    - Table-per-type)
  - Surrogate keys (sztuczne identyfikatory)
  - Tabele pomocnicze do relacji wiele-wiele

### Formalizm klas i asocjacji

| Symbol | Znaczenie   |
|--------|-------------|
| `+`    | publiczna   |
| `-`    | prywatna    |
| `#`    | chroniona   |
| `~`    | pakietowa   |

- **Asocjacja** - Powiązanie między klasami (np. „Użytkownik ma Konto”)
- **Agregacja** - Część może istnieć bez całości (`◇`)
- **Kompozycja** - Część żyje razem z całością (`◆`)
- **Dziedziczenie** - „jest-a” – podklasa rozszerza nadklasę (`△`)
- **Realizacja** - Implementacja interfejsu przez klasę (`▻`)

### Składowe

- Atrybuty: prywatne, publiczne, protected, static, const, kolekcje, pochodne
- Metody: publiczne, prywatne, protected, internal, abstrakcyjne, statyczne, konstruktory
- Asocjacje

### Atrybut vs Asocjacja

| Cecha                  | Atrybut                    | Asocjacja                            |
|------------------------|----------------------------|--------------------------------------|
| Przechowuje wartość    | Tak                         | Tak (referencja do innej klasy)     |
| Typ                    | Prosty (np. `int`, `str`)   | Złożony (inny obiekt)               |
| Reprezentacja w UML    | Wewnątrz klasy              | Linia między klasami                |

### Dziedziczenie

- Generalizacja/specjalizacja – dziedziczenie
- Realizacja – implementacja interfejsu

## Diagramy obiektów

Migawka systemu: instancje obiektów i ich stan w danym momencie

Narzędzia:
- **Enterprise Architect** – Instance Classifier, Set Run State
- **Visual Paradigm** – Object Diagram, Add Classifier, Open Specification

## Diagramy stanów

- Reprezentują maszyny stanowe
- **Stany** – nazwane rzeczownikowo/przymiotnikowo  
- **Akcje/przejścia** – strzałki między stanami (nie nazwane)

## Diagramy czynności

Dokumentują procesy, np. przypadki użycia i algorytmy

- **Czynności** – ogólne, podzielne  
- **Akcje** – konkretne, krótkie (czasowniki)

- Diagramy te używają:
  - Strzałki jako następstwa
  - Partycji (np. aktorzy)
  - Regionów (np. przerywalne)
  - Warunków (`if`, `else`, `przerwij`)

## Diagramy sekwencji

Dokumentują przepływ komunikatów między obiektami

- **Linie życia** – obiekty
- **Komunikaty** – np. `a.fooA()`, `return value`
- Obiekty typowane:
  - `Boundary`, `Control`, `Entity`
- Ramki: `loop`, `alt`, `opt`, `neg`, `par`, `ref`, `sd`
- Diagram pokazuje chronologiczny przebieg metod

## Diagramy komponentów

Reprezentacja komponentów (modułów, pakietów) i ich 

Komponent posiada **porty**:
  - **Dostawca usługi** – udostępnia interfejs
  - **Odbiorca usługi** – korzysta z interfejsu

# Porównanie diagramów UML

| Diagram     | Typ          | Przeznaczenie                         | Kluczowe elementy                      |
|-------------|--------------|---------------------------------------|----------------------------------------|
| Klas        | Strukturalny | Struktura systemu (klasy, relacje)    | Klasy, atrybuty, metody, relacje       |
| Obiektów    | Strukturalny | Migawka systemu w danym momencie      | Obiekty, wartości atrybutów            |
| Stanów      | Behawioralny | Stany obiektu i zmiany między nimi    | Stany, akcje i przejścia (nienazwane)  |
| Czynności   | Behawioralny | Przebieg procesów, algorytmy          | Akcje (czasowniki), przepływ, partycje |
| Sekwencji   | Behawioralny | Komunikacja między obiektami w czasie | Linie życia, komunikaty, ramki         |
| Komponentów | Strukturalny | Architektura wysokiego poziomu        | Komponenty, porty, zależności          |

## Diagrams-as-code

Tekstowa reprezentacja diagramów, łatwa do wersjonowania

- Przykłady narzędzi:
  - PlantUML
  - Mermaid.js

# Wykład 3: SOLID, GRASP

## 1. Responsibility-Driven Development (RDD)

Projektowanie obiektowe = określanie odpowiedzialności obiektów (klas) i ich relacji.

**Odpowiedzialność** – kontrakt związany z:
- **Działaniem**: tworzenie, obliczenia, inicjalizacja, kontrola innych obiektów.
- **Wiedzą**: dane, wiedza o innych obiektach.

**RDD** = przemyślane projektowanie poprzez właściwe przypisywanie odpowiedzialności klasom.

### Skrajności w projektowaniu:
- Jedna ogromna klasa zawierająca wszystko.
- Mnóstwo klas z jedną metodą.

## 2. GRASP – General Responsibility Assignment Software Patterns

### 2.1 Creator

Kto tworzy instancje klasy A?

**Rozwiązanie**: Klasa B, jeśli:
- Zawiera lub agreguje A
- Zapamiętuje A
- Używa A
- Posiada dane inicjalizacyjne dla A

### 2.2 Information Expert

Komu przydzielić odpowiedzialność?

**Rozwiązanie**: Temu, kto posiada niezbędne informacje (ekspertowi).

### 2.3 Controller

Kto spoza GUI kontroluje żądania systemowe?

**Rozwiązanie**: Klasa:
- Reprezentująca system
- Reprezentująca przypadek użycia (np. `LoginHandler`)

### 2.4 Low Coupling

Jak zmniejszyć zależności i zwiększyć możliwość ponownego użycia?

**Rozwiązanie**: Ogranicz liczbę powiązań między klasami.

### 2.5 High Cohesion

Jak tworzyć klasy z jasnym celem i łatwe w utrzymaniu?

**Rozwiązanie**: Wysoka spójność wewnętrzna klasy (metody ściśle powiązane).

**Przykład**:
- Klasa `Samochód` wykonująca zbyt wiele zadań → podzielić na mniejsze klasy (`Kierowca`, `Mechanik`, `Myjnia`)

### 2.6 Polymorphism

Jak obsługiwać warunki zależne od typu?

**Rozwiązanie**: Używaj operacji polimorficznych dla typów o różnych zachowaniach.

### 2.7 Indirection

Jak uniknąć bezpośrednich zależności między obiektami?

**Rozwiązanie**: Wprowadzenie obiektu pośredniczącego.

### 2.8 Pure Fabrication

Jak zachować Low Coupling i High Cohesion, gdy nie działa Information Expert?

**Rozwiązanie**: Wprowadź sztuczną klasę pomocniczą (np. `OrderRepository`).

### 2.9 Protected Variations (Law of Demeter)

Jak projektować odporne na zmiany komponenty?

**Rozwiązanie**: Otocz punkty zmienności stabilnym interfejsem.  
Prawo Demeter = „nie rozmawiaj z nieznajomymi”.

## 3. SOLID – Pięć zasad obiektowych

### 3.1 SRP – Single Responsibility Principle
- Klasa powinna mieć tylko jedną odpowiedzialność.
- **Test SRP**: czy klasa może być zmodyfikowana z więcej niż jednego powodu?

### 3.2 OCP – Open-Closed Principle
- Otwarte na rozszerzenia, zamknięte na modyfikacje.

**Sposoby realizacji**:
- Zależność od abstrakcji
- Polimorfizm
- Strategie, szablony, delegacje

### 3.3 LSP – Liskov Substitution Principle
- Obiekt klasy potomnej musi być zamienny z klasą bazową (semantycznie, nie tylko składniowo).

**Zasada**:
- Dozwolone: osłabienie warunku wejścia, wzmocnienie warunku wyjścia.
- Naruszenia:
  - Zwracanie `null` zamiast wartości
  - Zaostrzenie wymagań wejściowych (np. `Set` zamiast `List`)

### 3.4 ISP – Interface Segregation Principle
- Klasy nie powinny być zmuszane do implementacji metod, których nie używają.

### 3.5 DIP – Dependency Inversion Principle
- Moduły wysokiego poziomu powinny zależeć od abstrakcji, nie od szczegółów.

## 4. Inne zasady

### 4.1 DRY – Don’t Repeat Yourself
Unikaj powtórzeń kodu i odpowiedzialności.

### 4.2 Law of Demeter
= Protected Variations (zasada najmniejszej wiedzy)

### 4.3 DMMT – Don’t Make Me Think
Projektuj intuicyjne interfejsy.

### 4.4 DOP – Don’t Optimize Prematurely
Nie optymalizuj zbyt wcześnie.

## 5. Miary jakościowe (metryki R. Martina)

- **Ce**: zależności *od* innych pakietów
- **Ca**: zależności *na* dany pakiet
- **I** = Ce / (Ce + Ca) – niestabilność
- **A** = Ta / (Ta + Tc) – abstrakcyjność
- **D** = |A + I – 1| – odległość od ideału

**Preferencje**:
- I ∈ [0, 0.3] → fundament
- I ∈ [0.7, 1] → fasada

# Wykład 4 - Wzorce kreacyjne

### 1.1 Interface vs Abstract class

- Klasa abstrakcyjna może zawierać implementacje metod, interfejs nie.
- Dziedziczenie możliwe jest tylko z jednej klasy abstrakcyjnej, natomiast interfejsów może być wiele.

### 1.2 Delegacja (Prefer Delegation over Inheritance)

- Dziedziczenie jest statyczne (określone na etapie kompilacji), delegacja może być dynamiczna (w czasie działania).
- Delegujący obiekt może ukrywać metody obiektu delegowanego lub zmieniać jego kontrakt – co nie jest możliwe przy dziedziczeniu.
- Przykład dobrej praktyki: zamiast `Person` dziedziczącego z `Hashtable`, lepiej żeby `Person` delegował do `Hashtable`.
- Delegacja zwiększa ilość kodu – wiele języków (np. C#) nie wspiera jej składniowo, chociaż są propozycje rozszerzeń.

## 2. Wzorce kreacyjne

### 2.1 Singleton

- Zapewnia istnienie tylko jednej instancji klasy, współdzielonej przez wszystkich klientów.
- Często wykorzystywany jako centralny punkt startowy architektury.

### 2.2 Monostate

- Znosi ograniczenie jednej instancji z Singletona, ale wszystkie instancje dzielą ten sam stan.
- Klasy mogą być wielokrotnie instancjonowane, ale zachowują się jak Singleton poprzez współdzielenie danych.

### 2.3 (Delegate) Factory

- Realizuje odpowiedzialność typu **Creator** z GRASP.
- Fabryka może posiadać wiele metod tworzących różne typy obiektów.
- Może zwracać obiekty podtypów oczekiwanych przez klienta.
- Może kontrolować czas życia obiektów.

**Zalety:**
- Umożliwia rozszerzanie aplikacji bez naruszania istniejącego kodu (Zasada OCP).
- Zapewnia stabilny interfejs (Law of Demeter – GRASP).
- Może zastępować Singletony i Monostaty zapewniając lepszą elastyczność.

### 2.4 Factory Method

- Delegowanie tworzenia obiektu do metody fabrykującej, zazwyczaj abstrakcyjnej.
- Umożliwia użycie metody fabrykującej w klasach bazowych (przed implementacją).
- Konkretne podklasy dostarczają implementacji tworzenia.

### 2.5 Abstract Factory

- Nazywany również „toolkitem”.
- Zapewnia tworzenie całej rodziny powiązanych obiektów.
- Klient nie tworzy obiektów samodzielnie, lecz zleca to fabryce.

**Różnice względem Factory Method:**
- W FM klasa użytkowa sama tworzy obiekty pomocnicze.
- W AF tworzenie jest w pełni delegowane do osobnej fabryki.
- Klient z AF odpowiada Creatorowi z FM.

**Refaktoryzacja:** z FM do AF zachodzi przy zwiększeniu liczby typów tworzonych obiektów.

### 2.6 Prototype

- Tworzenie nowych obiektów przez kopiowanie istniejących prototypów.
- Nieistotne jest, jak prototyp został utworzony.
- Przydatne przy dynamicznym tworzeniu złożonych struktur.

### 2.7 Object Pool

- Wzorzec do zarządzania pulą „ciężkich” obiektów, które są kosztowne w tworzeniu.
- Zamiast tworzyć nowe obiekty, są one współdzielone i zwracane do puli.

### 2.8 Builder

- Stopniowe konstruowanie obiektów
- Ukrywa szczegóły procesu konstruowania złożonych obiektów.
- Ułatwia tworzenie struktur skomplikowanych wewnętrznie.

# Wykład 5 - Wzorce strukturalne

## 1. Facade

Uproszczony interfejs dla podsystemu z wieloma interfejsami.

- Celem wzorca jest ukrycie złożoności systemu.
- Facade udostępnia uproszczony interfejs dla zestawu klas.
- Stosowany często do „opakowania” bibliotek lub skomplikowanych API.

## 2. Read-only interface

Interfejs do odczytu dla wszystkich, a do zapisu tylko dla wybranych.

- Stosowany w celu ograniczenia możliwości modyfikacji danych.
- Przykład: `ReadOnlyCollection`, `AsReadOnly()`
- Projektowane są dwa interfejsy:
  - Interfejs do odczytu (`ReadOnlyInterface`)
  - Interfejs do modyfikacji (`MutableInterface`)
- Klient korzystający tylko z odczytu nie widzi metod modyfikujących.

## 3. Flyweight

Efektywne zarządzanie wieloma drobnymi obiektami.

- **Cel:** zmniejszenie zużycia pamięci przez współdzielenie danych.
- Kojarzony z: `Object Pool`, `immutable`, wiele danych.
- **FlyweightFactory**:
  - Utrzymuje niewielką liczbę współdzielonych instancji.
  - Zwraca te same obiekty na podstawie klucza (np. koloru bierki).
- **Stan obiektu:**
  - *Intrinsic*: wspólny dla wielu obiektów (np. kolor).
  - *Extrinsic*: przekazywany z zewnątrz (np. pozycja X/Y).

Przykład: plansza do warcabów 1mln x 1mln – tylko dwie bierki w pamięci: biała i czarna.

## 4. Decorator

Dynamiczne rozszerzanie odpowiedzialności obiektów (alternatywa dla podklas).

- Pozwala "owijać" obiekty innymi obiektami w celu dodania funkcjonalności.
- Popularny w bibliotekach do przetwarzania strumieni.
- Każdy dekorator implementuje ten sam interfejs co dekorowany obiekt.
- Może być stosowany wielokrotnie (rekursywność).
- Kluczowe cechy:
  - Zachowanie oryginalnego interfejsu.
  - Możliwość dowolnej kombinacji dekoratorów.

## 5. Proxy

Substytut obiektu w celu kontrolowania dostępu do niego.

### Rodzaje Proxy:
- **Zdalne (Remote)** – lokalny reprezentant zdalnego obiektu.
- **Wirtualne (Virtual)** – leniwe tworzenie kosztownego obiektu.
- **Ochronne (Protective)** – kontrola dostępu (np. autoryzacja).
- **Logujące (Logging)** – rejestruje dostęp do obiektu.

### Różnice Proxy vs Decorator:
- **Proxy** nie rozszerza interfejsu, jedynie kontroluje dostęp.
- **Decorator** może dodawać nowe funkcje i zachowania.

### Szczególny przypadek: **Circuit Breaker**
- Monitoruje liczbę błędów w wywołaniach zdalnych.
- Po przekroczeniu limitu przechodzi w tryb lokalny.
- Po czasie podejmuje próbę przywrócenia połączenia.

## 6. Adapter

Uzgadnianie niezgodnych interfejsów.

- Umożliwia współpracę klas o niekompatybilnych interfejsach.
- Tworzy „tłumacza”, który implementuje oczekiwany interfejs i deleguje działania do klasy źródłowej.
- Często wykorzystywany przy integracji starych bibliotek lub systemów.

## 7. Bridge

SRP + ISP + DIP dla hierarchii o dwóch stopniach swobody.

**Cel:** Oddzielenie abstrakcji od implementacji.

- Stosowany gdy obiekt ma dwie niezależnie zmieniające się odpowiedzialności.
- Przykład:
  - **Stopień 1:** pozyskiwanie danych (np. z SQL, XML)
  - **Stopień 2:** przetwarzanie danych (np. wypisanie na konsolę, wysyłka do usługi)
  - Podczas tworzebnia obiektu podajemy niezależnie sposób pozyskiwania danych oraz ich przetwarzania
- Bridge umożliwia niezależny rozwój obu aspektów.

# Wykład 6 - Wzorce czynnościowe

## 1. Null Object

Pusta implementacja zwalniająca klienta z testów `if` na `null`.

- Implementuje interfejs oczekiwany przez klienta, ale w sposób neutralny (nic nie robi).
- Klient może używać takiego obiektu zamiast normalnego bez sprawdzania, czy nie jest `null`.

**Zastosowanie z fabryką:**  
- W przypadku błędnych parametrów inicjalizacyjnych fabryka zwraca `NullObject`.
- Gwarantuje to zgodność z interfejsem, choć bez funkcjonalności.

## 2. Iterator

Dostęp do elementów kolekcji bez ujawniania jej struktury wewnętrznej.

**Kojarzyć z:** `IEnumerator`, `IEnumerable`.

## 3. Composite

Składanie obiektów w struktury drzewiaste.

- Klasa bazowa reprezentuje wspólny interfejs (np. `Tree`)
- Podklasy to liście (`TreeLeaf`) i węzły (`TreeNode`).
- Dzięki polimorfizmowi można wykonywać operacje rekurencyjnie bez znajomości szczegółów implementacji

## 4. Interpreter (Little Language)

Reprezentacja gramatyki języka i jego interpretera.

- Interpreter implementuje gramatykę języka jako hierarchię klas.
- Każdy element wyrażenia implementuje metodę `Interpret`, oraz kontekst (`Context`) – słownik z wartościami zmiennych.
- Służy do przechowywania informacji pomocniczych potrzebnych do interpretacji (np. mapowanie nazw zmiennych na wartości).

**Wzorzec bazuje na:**  
- Composite – struktura wyrażeń jako drzewo.
- Polimorfizm – delegowanie `Interpret` do odpowiedniej klasy.

## 5. Visitor

Interpreter, ale operacje są „wyniesione” do osobnej klasy – `Visitor`.

### Visitor nieznający struktury kompozytowej

- Struktura kompozytowa (np. drzewo) zna logikę przeglądania swoich elementów
- Elementy (`Element`), które implementują metodę `Accept`.
- Visitor zawiera metody `Visit{nazwa_elementu}` dla każdego typu elementu.
- Visitor nie musi znać szczegółów implementacyjnych, a jedynie implementuje `VisitLeaf` i `VisitNode`.

### Visitor znający szczegóły struktury kompozytowej

- Visitor sam przegląda strukturę (np. sam rekurencyjnie odwiedza poddrzewa). Brak metody `Accept` w strukturze.
- Zmienność struktury kompozytowej wymusza zmiany w Visitorze.

# Wykład 7 - Wzorce czynnościowe 2

## 1. Mediator

Koordynator komunikacji ściśle określonej grupy obiektów – dzięki niemu nie odwołują się do siebie wprost, lecz przesyłają powiadomienia przez mediatora.

- Uproszczony wariant Observera.
- Komunikuje ograniczoną grupę obiektów, do których ma jawne referencje.
- Kolaborujące obiekty powiadamiają się nawzajem o zmianie stanu (Mediator sam nie przechowuje stanu).

### Przykład:
Typowe okienka (Form) w aplikacjach desktopowych pełnią rolę mediatorów między kontrolkami wewnętrznymi.

## 2. Observer

Powiadamianie zainteresowanych o zmianie stanu – obiekty nie odwołują się do siebie wprost.

- Umożliwia komunikację między obiektami bez jawnych zależności.
- Uogólnia interfejs Mediatora – może obsługiwać dowolną liczbę obserwatorów poprzez listę.

### Przykład:
W architekturze aplikacji GUI:
- Wewnątrz okienka – używany Mediator.
- Pomiędzy różnymi okienkami – stosowany Observer.

## 3. Event Aggregator

Rozwiązuje problem Observera ogólniej – jeden mechanizm dla różnych typów powiadomień.

- Hub komunikacyjny: realizacja Observera jako słownika list słuchaczy, indeksowanych typem powiadomienia.
- Obiekty publikujące i subskrybujące nie muszą znać siebie nawzajem – jedynie EventAggregatora.

## 4. Memento

Zapamiętuj i odzyskuj stan obiektu.

### Charakterystyka:
- Obiekt Memento przechowuje stan innego obiektu (Originatora), który potrafi tworzyć i przywracać swoje Memento.
- Memento może przechowywać pełny stan lub tylko przyrostową zmianę (deltę).
- Stosowany m.in. do implementacji mechanizmu Undo/Redo.

### Undo/Redo – Założenia:
- Każda zmiana stanu powinna odkładać się w historii.
- Cofanie (Undo) możliwe do najdalszego zapamiętanego stanu.
- Przywracanie (Redo) możliwe, dopóki nie zmieniono stanu ręcznie.
- Zmiana po Undo usuwa "przyszłość".

### Implementacja:
- Stos do przechowywania historii `undo`.
- Stos do przywracania zmian `redo`.
- Podczas zmiany stanu:
  - Tworzone jest Memento i dodawane na stos `undo`.
  - Stos `redo` jest czyszczony.
- Przy `Undo`:
  - Bieżący stan trafia na stos `redo`, a poprzedni zostaje przywrócony.
- Przy `Redo`:
  - Stan z `redo` trafia na stos `undo` i zostaje przywrócony.

# Wykład 8 - Wzorce czynnościowe 3

## 1. Chain of Responsibility

- Pozwala na przekazywanie żądań wzdłuż łańcucha potencjalnych odbiorców.  
- Każdy obiekt w łańcuchu może zdecydować, czy przetwarza żądanie, czy przekazuje je dalej.
- Typowe zastosowanie: skomplikowana logika przetwarzania, wielu niezależnych odbiorców.

## 2. Command (Polecenie)

- Kapsułkowanie żądań w postaci obiektów o jednolitym interfejsie. 
- Oddzielenie wywołującego (Invoker) od odbiorcy (Receiver).
- Pozwala na zapisanie żądań jako obiektów.

## 3. Template Method (Metoda szablonowa)

Określ szkielet algorytmu, delegując implementację szczegółów do podklasy.

- Klasa bazowa zawiera metodę szablonową (`TemplateMethod()`), która wywołuje metody abstrakcyjne lub wirtualne.  
- Podklasy definiują szczegóły działania poprzez nadpisanie tych metod.

## 4. Strategy (Strategia)

Template Method, ale bez dziedziczenia

- Opiera sie na delegacji a nie dziedziczeniu
- Umożliwia zmianę algorytmu w czasie działania programu.  
- Obiekt deleguje konkretne kroki do klasy strategii, zgodnie z interfejsem `Strategy`.

## 5. State (Stan)

Maszyna stanowa.

- Każdy stan to osobna klasa implementująca wspólny interfejs `State`.
- Obiekt kontekstu deleguje wywołania do bieżącego stanu.

# Wykład 9 - Wzorce architektury aplikacji

## 1. Automated Code Generation

Technika wspomagająca, polegająca na generowaniu kodu przez automat w sposób deklaratywny. 

- **Elementy imperatywne**: zawarte w blokach `<# … #>`, wykonywane jako kod.
- **Elementy deklaratywne**: kopiowane bez zmian do wyjścia.

## 2. Object-Relational Mapping (ORM)

Rozwiązanie problemu niezgodności świata obiektowego z relacyjnym.
Umożliwia pracę z bazą danych przy użyciu obiektów.

### Przykładowe implementacje:
- Hibernate / nHibernate (Java / .NET)
- Entity Framework (.NET)
- JPA (Java)
- Sequelize (Node.js)
- Active Record (Ruby)

### 2.1 Database First / Model First / Code First

- **Database First**: najpierw struktura relacyjna, model generowany automatycznie.
- **Model First**: najpierw model mapowania, potem baza i klasy.
- **Code First**: najpierw klasy, a struktura bazy generowana przez narzędzie.

Obecnie używa się głównie **Code First**

### 2.2 Metadata Mapping

Strategie definiowania metadanych:
- **W klasach** (np. atrybuty, dziedziczenie).
- **Zewnętrzne** (np. XML, API).

Niektóre technologie wspierają **migracje** — wersjonowanie modelu relacyjnego.

### 2.3 Lazy Loading

Ładowanie danych tylko na żądanie — unika nadmiarowego ładowania danych powiązanych.

#### Techniki:
1. **Lazy initialization** – kod z flagą `isLoaded`.
2. **Virtual proxy** – proxy z automatycznym ładowaniem danych.
3. **Value holder** – delegacja pobierania danych do osobnego obiektu.

### 2.4 Relacje

Mapowanie relacji jeden-do-jednego:
- Jedna klasa odwzorowana w dwóch tabelach (split entity).
- Dwie klasy powiązane relacją.

Relacja wiele-do-wiele odwzorowana jako tabela asocjacyjna.
Silnik ORM może nią zarządzać automatycznie lub wymagać jawnego modelowania.

### 2.6 Dziedziczenie

#### Strategie:
1. **Concrete Table (TPC)** – jedna tabela na klasę:
   - Proste, ale problemy z identyfikatorami i relacjami.
2. **Single Table (TPH)** – jedna tabela na całą hierarchię:
   - Kolumna dyskryminatora, ale dużo `NULL`, łamie 3NF.
3. **Class Table (TPT)** – osobna tabela na każdą klasę:
   - Poprawna normalizacja, ale złożone zapytania.

### 2.7 1st Level Cache (Identity Map)

Buforowanie obiektów w kontekście zapytań po ID — przypisanie ID → obiekt.

### 2.8 2nd Level Cache

Buforowanie wybranych zapytań — jawne zarządzanie cache, możliwość wymiany implementacji.

### 2.9 Język Zapytaniowy

Języki obiektowe do zapytań:
- **LINQ** (C#)
- **HQL / JPQL** (Hibernate, JPA)
- **Criteria API** (Java)

### 2.12 Global Filter

Możliwość ustawienia filtrów globalnych (np. dla daty obowiązywania) — stosowane automatycznie w zapytaniach.

### 2.13 Soft Delete

Logiczne usuwanie — znakowanie rekordu zamiast fizycznego usunięcia.

#### Zalety:
- Szybsze niż DELETE.
- Możliwość audytu i przywrócenia.

#### Wady:
- Wymaga uwzględnienia kolumny `IsDeleted` w zapytaniach.

# Wykład 10 - Wzorce architektury aplikacji 2

## Inversion of Control / Dependency Injection

### 1. Inversion of Control vs Dependency Injection

- **Inversion of Control (IoC)** – zbiór technik pozwalających tworzyć luźno powiązane struktury klas.
- **Dependency Injection (DI)** – konkretna implementacja IoC w językach obiektowych.

Korzyści:
- **Późne wiązanie** – zmiana implementacji bez rekompilacji.
- **Ułatwienie testowania** – podstawianie stubów/fake’ów.
- **Uniwersalna fabryka** – dynamiczne tworzenie instancji typów.

### 2. Dependency Inversion Principle (DIP)

**Zalety:**
- Rozszerzalność (zgodność z OCP)
- Równoległa implementacja dzięki interfejsom
- Lepsza konserwowalność
- Niezależne testowanie klas
- Możliwość późnego określenia implementacji

### 3. Twarde vs Miękkie zależności

- **Twarde (stable)** – zależności do stabilnych, istniejących modułów.
- **Miękkie (volatile)** – zależności konfigurowane dynamicznie, np. przez kontener DI.
- **Spoina (seam)** – miejsce, gdzie zależność jest reprezentowana przez interfejs.

**Uwaga:** Zależność do samego frameworka DI jest zwykle twarda.

### 4. Kluczowe podwzorce Dependency Injection

#### 4.1 Składanie obiektów (Composition)

- **Kontener (kernel)** – odpowiedzialny za tworzenie instancji i rozwiązywanie zależności.
- **Rejestrowanie typów** – zarówno konkretnych (sztywnych), jak i interfejsów (miękkich).
- **Rejestrowanie instancji** – umożliwia kontrolę nad pojedynczym obiektem.
- **Cykl w grafie zależności** – potencjalny problem.
- **Wstrzykiwanie zależności:**
  - przez konstruktor (zalecane)
  - przez metodę (atrybut `[InjectionMethod]`)
  - przez właściwość (atrybut `[Dependency]`)
- **BuildUp** – uzupełnianie już istniejącego obiektu zależnościami.
- **Injection Factory** – możliwość wytwarzania zależności poprzez złożoną logikę.

#### 4.2 Zarządzanie czasem życia obiektów (Lifecycle Management)

- **Transient** – nowy obiekt za każdym razem.
- **ContainerControlled** – singleton.
- **Hierarchical** – singleton per podkontener.
- **PerThread** – inny obiekt na każdy wątek.
- **PerHttpContext** – nowy obiekt na każde żądanie HTTP.
- **Custom** – niestandardowy cykl życia.

#### 4.3 Konfiguracja kontenera

- **Deklaratywna** – XML, np. `unity.config`.
- **Imperatywna** – w kodzie (np. `RegisterType`).
- **Autokonfiguracja** – automatyczne mapowanie typów z pakietu.

#### 4.4 Przechwytywanie żądań (Proxy)

**Typowe zastosowania:**
- Audytowanie, logowanie, monitorowanie, bezpieczeństwo, cache’owanie, obsługa błędów.

**Rodzaje interceptorów:**
- `InterfaceInterceptor` – działa na metodach interfejsu.
- `VirtualMethodInterceptor` – działa na metodach wirtualnych.

### 6. Service Locator vs Composition Root + Local Factory

#### Service Locator (SL)

- Singleton kontenera dostępny globalnie.
- **Zalety**: redukcja zależności między klasami.
- **Wady (dlaczego antywzorzec):**
  - Wprowadza zależność do frameworka DI.
  - Ukrywa zależności (niejawne, trudne do śledzenia).

#### Composition Root (CR)

- Miejsce w aplikacji, gdzie rejestrowane są zależności (np. `Main`, `Application_Start`).
- Jedyny legalny punkt styku z DI.

#### Local Factory (Dependency Resolver)

- Wstrzykiwana fabryka lokalna odpowiedzialna za tworzenie instancji klas.
- Dzięki niej klasy są niezależne od frameworka DI.
- Fabryka ma miękką zależność – można ją łatwo wymienić, np. do testów.

# Wykład 11 - Wzorce architektury aplikacji 3

## Repository

Repository stanowi dodatkową warstwę abstrakcji nad warstwą dostępu do danych.
Odpowiada za dostęp do jednej kategorii danych (np. jednej tabeli w bazie danych).

## Rodzaje Repository

### Generic Repository
- Jeden wspólny interfejs dla wszystkich encji.
- Wspiera uniwersalne interfejsy zapytań (np. LINQ, JPA).
- Umożliwia prostsze zarządzanie repozytoriami.

### Concrete Repository
- Osobny interfejs repozytorium dla każdej klasy modelu.
- Umożliwia tworzenie metod specyficznych dla danego typu (np. `FindAllUsersForStartingLetter`).
- Trudniejsze w utrzymaniu i rozwijaniu – konieczność dodawania metod przy ewolucji projektu.

## Unit of Work (UoW)

Jedna warstwa agregująca wiele repozytoriów. Odpowiada za:
- Udostępnianie dostępu do wszystkich repozytoriów z jednego miejsca.
- Współdzielenie kontekstu dostępu do danych.
- Zarządzanie transakcjami (opcjonalnie).

### Korzyści
- Upraszcza korzystanie z repozytoriów (jedna instancja zamiast wielu).
- Zapewnia spójność (wspólny kontekst dostępu do danych).
- Możliwość rozbudowy o zarządzanie transakcjami i metadanymi.

**Uwaga:** Repository powinien być implementowany wraz z Unit of Work. 
Oddzielne repozytoria bez UoW prowadzą do problemów z integracją w wyższych warstwach aplikacji.

## Struktura projektu

### Warstwa abstrakcji
- Interfejsy modeli: `IUser`, `IAddress`, `IParent`, `IChild`
- Interfejs repozytorium: `IGenericRepository<T>` lub zestaw konkretnych interfejsów
- Interfejs UoW: `IUnitOfWork`
- Fabryka `UnitOfWorkFactory` – zapewnia instancje UoW

### Kod kliencki
- Odwołuje się tylko do abstrakcji i fabryki.
- Nie zna implementacji repozytoriów ani modeli.

### Warstwa implementacji
- Różne zestawy modeli, repozytoriów i UoW dla każdej technologii (np. `EFUnitOfWork`, `LinqUnitOfWork`)
- Dopasowanie wygenerowanych klas do interfejsów (np. `Child : IChild`)
- Konfiguracja zależności w `Composition Root`

### Composition Root
- Ustawia dostawcę fabryki `UnitOfWorkFactory`
- Może korzystać z kontenera IoC

# Wykład 12 - Wzorce architektury aplikacji 4

## 1. Architektura aplikacji

### 1.1 Diagram referencyjny
Architekturę aplikacji często przedstawia się jako stos warstw (od warstwy danych do interfejsu użytkownika). Stos to zestaw technologii wspierających implementację poszczególnych warstw.

### 1.2 Rodzaje aplikacji
- **Mobile Application**: obsługa scenariuszy offline, ograniczone zasoby.
- **Rich Client Application**: lokalne zasoby, możliwość działania offline.
- **Rich Internet Application**: bogaty interfejs, działa w przeglądarce.
- **Service Application**: luźne powiązania, komunikacja przez wiadomości XML.
- **Web Application**: tylko online, zasoby na serwerze.

### 1.3 Style architektury aplikacji
- **Client-Server**: klient żąda usług od serwera.
- **Component-Based**: aplikacja jako zestaw komponentów z interfejsami.
- **Layered Architecture**: podział aplikacji na warstwy.
- **Message-Bus**: komunikacja przez wiadomości.
- **MVC**: rozdzielenie interakcji użytkownika, logiki i danych.
- **N-tier / 3-tier**: podobna do Layered, ale z rozdziałem fizycznym.
- **SOA**: komponenty jako usługi wymieniające wiadomości.

### 1.4 Kryteria ewaluacji architektury
- **Availability**: czas działania systemu.
- **Conceptual Integrity**: spójność projektowa.
- **Flexibility**: możliwość adaptacji.
- **Interoperability**: wymiana danych między systemami.
- **Maintainability**: łatwość modyfikacji.
- **Manageability**: zarządzanie i monitoring.
- **Performance**: responsywność (latency, throughput).
- **Reliability**: zdolność do pracy bez awarii.
- **Reusability**: możliwość ponownego wykorzystania.
- **Scalability**: działanie przy wzroście obciążenia.
- **Security**: ochrona danych.
- **Supportability**: łatwość obsługi przez operatorów.
- **Testability**: możliwość testowania.
- **Usability**: jakość interakcji z użytkownikiem.

### 1.5 Kluczowe decyzje projektowe
- **Autoryzacja i uwierzytelnianie**
- **Zarządzanie stanem i cache'owaniem**
- **Komunikacja i współbieżność**
- **Zarządzanie konfiguracją**
- **Separacja odpowiedzialności**
- **Dostęp do danych i wyjątki**
- **Doświadczenie użytkownika**
- **Walidacja i workflow** 

## 2. Wzorce architektury warstwy interfejsu użytkownika

Celem wzorców UI jest separacja logiki aplikacyjnej od prezentacji, co umożliwia łatwiejsze testowanie oraz utrzymanie kodu.

### 2.1 Model-View-Controller (MVC)

- **Typ aplikacji**: Web Application
- **Interakcja**:
  - Użytkownik → Controller → Model + View → Użytkownik
- **Zalety**:
  - Controller jest tworzony przez framework na podstawie żądania.
  - Controller przygotowuje Model i wskazuje View do renderowania.
  - Testowalność przez możliwość wywoływania akcji kontrolera bez interfejsu.

### 2.2 Model-View-Presenter (MVP)

- **Typ aplikacji**: Rich Client Application
- **Interakcja**:
  - Użytkownik → View ⇄ Presenter → Model
- **Charakterystyka**:
  - Widok deleguje logikę do prezentera.
  - Prezenter steruje widokiem i przetwarza dane.
  - Wstrzykiwanie widoku do prezentera (interfejs).
- **Testowalność**:
  - Alternatywna implementacja widoku bez UI.
  - Prezenter testowalny niezależnie.
- **Refaktoryzacja do MVP**:
  - Utworzenie prezenterów i interfejsów dla formularzy.
  - Przeniesienie logiki ze zdarzeń UI do prezenterów.
  - Widoki implementują interfejsy, prezenter je steruje.

### 2.3 Model-View-ViewModel (MVVM)

- **Inspiracja MVP**, głównie dla WPF/XAML (.NET)
- **Różnice**:
  - Widok nie zawiera logiki (data-binding).
  - Widok korzysta tylko z ViewModelu (nie prezenter).
  - ViewModel wystawia dane do powiązań.
- **Zalety**:
  - Silna separacja.
  - Deklaratywność i prostota testowania.

## 3. Architektura Heksagonalna (Ports and Adapters / Onion Architecture)

- **Cel**: oddzielenie logiki biznesowej od wejścia/wyjścia aplikacji.
- **Zastosowanie**: Web i Rich Client.
- **Podział**:
  - **Porty pierwotne (wejściowe)**: klasy wykonujące przypadki użycia.
  - **Porty wtórne (wyjściowe)**: interfejsy np. do baz danych, e-maili itp.
- **Wzorce pomocnicze**:
  - Command dla portów pierwotnych.
  - Dependency Injection, Local Factory dla portów wtórnych.
- **Asymetria lewo-prawo**:
  - Porty pierwotne – konkretne klasy.
  - Porty wtórne – interfejsy.

### Architektura Czysta (Clean Architecture)
- Kombinacja Architektury Heksagonalnej i Domain-Driven Design (DDD).
- **DDD** – skupienie na modelu domenowym, nie definiuje reszty architektury.
- **Wnioski**:
  - Architektura heksagonalna ≠ DDD.
  - Możliwe użycie jednego bez drugiego.
  - Clean Architecture = Hex + DDD.

### Testowalność
- Porty pierwotne można testować bez UI.
- Porty wtórne można podmienić na "mocki".

# Wykład 13 - Testowanie oprogramowania

## 1. Wprowadzenie

Współczesne testowanie obejmuje nie tylko testy jednostkowe, ale również użycie narzędzi wspierających:

- **Obiekty zastępcze (mock objects)** – eliminują potrzebę pisania własnych implementacji zastępczych.
- **Automatyczne generowanie przypadków testowych** – na podstawie struktury kodu.
- **Dynamiczna i statyczna walidacja poprawności programów**.

## 2. TDD vs BDD

### TDD (Test-Driven Development)
- Programowanie sterowane testami.
- Główne pojęcia:
  - **SUT (System Under Test)** – testowana klasa użytkowa.
  - **Collaborators** – usługi pomocnicze, których SUT używa.

### AAA – Arrange / Act / Assert
Metodyka struktury testów:
1. **Arrange** – przygotowanie SUT i jego współpracowników.
2. **Act** – wykonanie akcji.
3. **Assert** – sprawdzenie oczekiwań.

### Czy używać prawdziwych usług pomocniczych?
**Nie!** Skutki uboczne (np. wysyłka maili) są niepożądane.

### Test Doubles (Dublerzy)
Rodzaje obiektów zastępczych:

- **Dummy** – nieużywana implementacja, tylko do wypełnienia zależności.
- **Stub** – zwraca spreparowane wyniki dla konkretnego testu.
- **Fake** – uproszczona, działająca wersja prawdziwej implementacji (np. zapis do pamięci).
- **Mock** – w pełni kontrolowany obiekt używany w testach BDD.

### BDD (Behavior-Driven Development)
- Rozszerzenie TDD – testowanie **zachowania**, a nie stanu.

#### Co testuje BDD?
- Czy SUT wywołuje odpowiednie metody collaboratorów.
- Czy parametry i liczba wywołań są właściwe.
- Czy kolejność wywołań jest zgodna z oczekiwaniami.

#### Zalety
- Unikanie wielokrotnego `Act-Assert` dzięki skupieniu na interakcjach.

## 3. Design by Contract (DbC)

Technika projektowania obiektowego, gdzie kontrakty stają się częścią interfejsu klasy:

- **Precondition** – warunek przed rozpoczęciem metody.
- **Postcondition** – warunek po zakończeniu metody.
- **Invariant** – warunek, który musi być zawsze spełniony.

### Język do wyrażania kontraktów
- **OCL (Object Constraint Language)** – logika pierwszego rzędu.

### Weryfikacja kontraktów
- **Dynamiczna** – np. przez `Contract.Ensures`, `Contract.Requires`.
- **Statyczna** – niepraktyczna ze względu na nierozstrzygalność.

### Przykład użycia kontraktów:
- `Abs(x)` – gwarantuje, że wynik ≥ 0.
- `Swap(ref x, ref y)` – zapewnia zamianę wartości.

## 4. Testowanie UI – UI Automation

Testy akceptacyjne poprzez interfejs użytkownika.

### Technologie:
- **UI Automation** (MS Windows).
- **White** – wygodniejsze API na bazie UI Automation.
- **WebDriver** – standard od 2004.
- **Playwright** – nowoczesna platforma do automatyzacji przeglądarek.
- **Puppeteer** – biblioteka do automatyzacji Chrome (od 2017).

# Wykład 15 - Service Oriented Architecture

## 1. Modele integracji danych

Integracja danych eliminuje konieczność wielokrotnego wprowadzania tych samych danych w różnych systemach. 
Kluczowe jest rozdzielenie poziomu technicznego (jak przekazywać dane) od poziomu analitycznego (co i kiedy przekazywać).

### 1.1 Integracja przez wymianę plików

**Zalety:**
- Możliwość użycia w heterogenicznych środowiskach.

**Wady:**
- Wymaga ręcznej ingerencji użytkownika.
- Automatyzacja wymaga współdzielenia nośnika.
- Potencjalne ryzyko wycieku danych (brak szyfrowania).

### 1.2 Integracja przez wspólną bazę danych

**Zalety:**
- Natychmiastowa i automatyczna integracja.

**Wady:**
- Trudna skalowalność (powyżej ~1000 tabel).
- Problemy w integracji aplikacji od różnych dostawców.
- Wysoka złożoność zarządzania.

### 1.3 Integracja przez usługi aplikacyjne (Web Services)

**Zalety:**
- Możliwość integracji różnych technologii.
- Standardy interoperacyjności (REST, WSDL).

**Wady:**
- Problem sieci połączeń „każdy z każdym” – liczba połączeń rośnie wykładniczo.

### 1.4 Integracja przez brokera/szynę usług

- Połączenie Web Services i Event Aggregator.
- Aplikacje publikują/subskrybują zdarzenia.
- Złożoność połączeń liniowa.
- Wiarygodne dostarczanie, uwierzytelnianie i standardy komunikacji.

## 2. Message Oriented Architecture (MOA)

Model architektury oparty na komunikatach, z użyciem Message-Oriented Middleware (MOM).

### Podejścia:

#### API Driven

- Abstrakcja poprzez interfejs (np. JMS).
- **Zalety:** wymienność dostawcy.
- **Wady:** brak interoperacyjności (np. z .NET, PHP).

#### Protocol Driven

- Abstrakcja poprzez protokół (np. AMQP).
- **Zalety:** rzeczywista interoperacyjność.
- **Wady:** może wymagać warstwy pośredniej dla spełnienia formalnych wymagań (np. XML/WSDL).

## 3. Enterprise Service Bus (ESB)

Szyna usług – zewnętrzna usługa typu MOM dla integracji systemów.

### 3.1 Wzorce komunikacyjne:

- **Publish/Subscribe (P/S):** rozdzielenie nadawców i odbiorców.
- **Request/Reply (R/R):** zapytanie i odpowiedź.
- **Saga (Long Running Transaction):** złożone procesy biznesowe z logiką warunkową.

### 3.2 Asynchroniczność

- Różne tempo przetwarzania u subskrybentów.
- Wymagane repozytorium trwałe (BD, kolejki).

### 3.3 Porty wejścia/wyjścia

- **Port wejścia:**
  - *Pull:* szyna monitoruje zasób (pliki, BD).
  - *Push:* dane dostarczane przez usługę aplikacyjną.

- **Port wyjścia:**
  - *Pull:* aplikacja subskrybenta monitoruje stan portu.
  - *Push:* szyna aktywnie przekazuje dane.

**Wydajność:** tryb push efektywniejszy, ale technicznie nie zawsze możliwy.

### 3.4 Szyna vs Business Process Engine

- **BPEL:** XML-owy język (traci na znaczeniu).
- **BPMN:** graficzna notacja procesów wspierana przez narzędzia (rekomendowana).

## 4. Command-Query Responsibility Segregation (CQRS)

Architektura systemu transakcyjnego z rozdzieleniem odczytu i zapisu.

**Cechy:**
- Odczyt występuje dużo częściej niż zapis (nawet 1000:1).
- Odczyt – struktura zdenormalizowana, zapis – znormalizowana.
- Możliwość użycia różnych baz danych (np. SQL + NoSQL).
- Komunikaty `Command` → aktualizacja → komunikaty `Change` → widok.
- Dobrze współgra z architekturą heksagonalną i systemami kolejkowymi.

# Bonus (komplet kamyczków w ogródku)

## Wzorce kreacyjne (tworzenie obiektów)

- **Singleton** – zwraca jedna i tą samą instancja klasy
- **Monostate** – wiele instancji klasy, ale współdzielą ten sam stan
- **Factory** – metoda lub klasa tworząca obiekty zamiast używania `new`
- **Factory Method** – factory parametryzowane funkcją opisującą jak tworzyć obiekt
- **Abstract Factory** – Factory Method, ale bardziej rozbudowane z dziedziczeniem zamiast funkcji
- **Prototype** – tworzy obiekt przez kopiowanie innego (np. przez `.clone()`).
- **Object Pool** – przechowuje pulę gotowe obiekty do ponownego użycia (wyciąga się z niej i zwraca obiekty do niej).
- **Builder** – konstruuje złożone obiekty krok po kroku (można przez to dostować obiekt w trakcie tworzenia).

## Wzorce strukturalne (łączenie obiektów i interfejsów)

- **Facade** – upraszcza dostęp do złożonego systemu przez prosty interfejs.
- **Read-only Interface** – udostępnia tylko metody odczytu (np. dla bezpieczeństwa danych).
- **Flyweight** – współdzieli wspólne dane pomiędzy wieloma obiektami, oszczędzając pamięć.
- **Decorator** – dynamicznie dodaje funkcje do obiektu bez zmiany jego klasy.
- **Proxy** – pośrednik kontrolujący dostęp do innego obiektu (np. opóźnione ładowanie).
- **Adapter** – zmienia interfejs jednego obiektu na zgodny z oczekiwanym.
- **Bridge** – rozdziela abstrakcję od jej implementacji, umożliwiając ich niezależne rozwijanie.

## Wzorce czynnościowe (zachowanie obiektów)

- **Null Object** – obiekt, który „nic nie robi”, ale zachowuje interfejs używany zamiast `null`.
- **Iterator** – umożliwia przechodzenie po elementach kolekcji bez znajomości jej struktury.
- **Composite** – umożliwia traktowanie obiektów rekurencyjnie (np. struktura drzewa).
- **Interpreter** – przetwarza dane według zdefiniowanej gramatyki języka (Composite z metodą Interpret).
- **Visitor** – Interpreter z osobną klasą na implementację funkcjonalności.
- **Mediator** – obiekt pośrednik w komunikacji dwóch obiektów (ma ich referencje)
- **Observer** – Mediator bez posiadania referencji na obiekty (można je rejestrować), informujący o zmianie stanu
- **Event Aggregator** – centralne miejsce do obsługi i rozgłaszania zdarzeń (rozszerza Observera).
- **Memento** – pozwala zapamiętać i przywrócić stan obiektu bez naruszania prywatności.
- **Chain of Responsibility** – przekazuje żądanie przez rekurencyjny łańcuch obiektów, aż któreś je obsłuży.
- **Command** – zamienia żądanie w obiekt, pozwala na jego zapis, cofnięcie lub kolejkowanie.
- **Template Method** – szkielet algorytmu w klasie bazowej, szczegóły w podklasach.
- **Strategy** – Template Method, ale z delegacją zamiast dziedziczenia
- **State** – każdy stan obiektu ma podklasę z implementacją unikalną dla danego stanu

## Wzorce architektury aplikacji

- **Object-Relational Mapping (ORM)** – automatyczne mapowanie obiektów na dane w bazie.
- **Inversion of Control / Dependency Injection** – przekazywaenie zalżności do obiektu z zewnątrz (np. przez konstruktor).
- **Repository** – pośrednik między aplikacją a bazą danych, ukrywa zapytania i szczegóły dostępu (realizuje CRUD).
- **Unit of Work** – zbiera i zarządza zmianami w danych jako jedną transakcją.
- **Model-View-Controller (MVC)** – podział aplikacji na model (logika), widok (interfejs) i kontroler (sterowanie).
- **Model-View-Presenter (MVP)** – jak MVC, ale logika sterująca jest w prezenterze, który komunikuje się z widokiem.
- **Architektura Heksagonalna** – logika aplikacji jest odseparowana od zewnętrznych interfejsów (np. bazy, API) przez porty i adaptery.

## Wzorce architektury systemów

- **Domain Driven Design (DDD)** – projektowanie systemu wokół logiki i pojęć biznesowych (np. Klient, Faktura).
- **Microservices** – system jako zestaw niezależnych usług komunikujących się przez sieć.
- **Message Oriented Architecture (MOA)** – systemy komunikują się przez asynchroniczne wiadomości (np. kolejki).
- **Enterprise Service Bus (ESB)** – centralny kanał do integracji systemów i usług za pomocą wiadomości.
