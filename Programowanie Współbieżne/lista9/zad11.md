#### Zamki kohortowe

Zamki kohortowe to hierarchiczne mechanizmy synchronizacji dla systemów NUMA, które łączą szybkie przekazywanie uprawnień między wątkami na tym samym węźle procesora (ograniczając kosztowną migrację danych między węzłami) z ogólnym dostępem globalnym.

Sprowadza się do wykorzystywania dwóch zamków, globalnego i lokalnego. Wejscie do sekcji krytycznej następuje kiedy kohorta do której należy wątek zajmuje zamek globalny, a sam wątek zajmuje zamek lokalny. Po wyjściu z sekcji krytycznej wątek zwalnia zamek lokalny i sprawdza czy inny wątek z jego kohorty chce wejść do sekcji krytycznej. Jeżeli daj to ta sama kohorta utrzymuje kontrolę nad zamkiem globalnym.

#### TurnArbiter (Klasa)

Odpowiada za sprawiedliwość. Zlicza, ile razy zamek został przekazany lokalnie wewnątrz kohorty. Jeśli limit zostanie osiągnięty, wymusza zwolnienie zamka globalnego, aby inne węzły mogły uzyskać dostęp.

#### `alone()`
Odpowiada za detekcję kohorty. Sprawdza, czy w lokalnej kolejce są inni oczekujący (następcy).

Jeśli true (jest sam): Zwalnia zamek globalny (bo nie ma komu go przekazać lokalnie).

Jeśli false: Może przekazać zamek bezpośrednio lokalnemu sąsiadowi.

#### Intuicja algorytmu

Wątek opuszczający sekcję krytyczną sprawdza, czy ma lokalnych następców (alone()). Jeśli tak i nie przekroczono limitu (TurnArbiter), przekazuje zamek sąsiadowi (szybko). W przeciwnym razie oddaje zamek globalnie (sprawiedliwie).