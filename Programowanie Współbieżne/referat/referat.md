## Wstęp

1. `sychronized` a lock
2. Monitory
3. Problem z zagnieżdzaniem lockow
4. Skrot pozytywnych cech "thin-lockow"

## Opis algorytmu

1. rodzaje sytuacji w jakich sa uzywane locki i czestosc ich wystepowania
2. fat-locks, juz zaimplementowane wczesniej w javie do ciezkich zadan
3. Wykorzystywanie operacji sprzetowej compare-and-swap
4. headeary obiektow w javie
5. 24bity locka w takim headerze

bity:
- 1: jezeli 0 to thin-lock, jezeli 1 to referencja do fat-locka
- 15: jezeli 0 to jest oblokowany, jezeli cos wiecej to oznacza index w zewnętrznej tablicy referencji wątków
- 8: licznik zagnieżdzenia (pomniejszony o 1, 0 oznacza pojedynczy lock) (z tego powodu wątki powyżej zagnieżdżenia 256 są oblugiwane przez fat-lock)

- jeżeli pierwszy bit to 1, to pozostałe 23 bity to indeks referencji fat-locka

6. kiedy uzywamy think-lockow a kiedy fat-lockow
7. Jak wyglada operacja locka (rozpisac lacznie z dokladnoscia do operaci maszynowych)
    - lock bez rywalizacji (compare-and-swap z sukcesem)
    - unlock bez rywalizacji (compare-and-swap nie jest potrzebny, poniewaz zakladamy ze zablokowanego locka nie moze modyfikowac nikt poza watkiem ktory go zablokowal)
    - zagniezdzony lock i unlock (compare-and-swap z porazka, sprawdzenie czy poprzedni lock byl wykonany przez ten sam watek, operacje bitowe zmieniajace licznik)
    - lock z rywalizacja (compare-and-swap z porazka, sprawdzenie czy poprzedni lock byl wykonany przez ten sam watek, spinowanie i czekanie na zwolnienie locka, zamiana go w fat-locka)
8. spinowanie jest nieporzadane, ale wedlug zasady "lokalnosci rywalizacji" rywalizacja pomiedzy dwoma watkami ktore mialy ja wczesniej jest bardzo prawdopodobna, a spinowanie wystapi tylko za pierwszym razem, kolejne beda korzystac juz z fat-locka

## Pomiary wydajnosci

1. co porownujemny (ThinLock, JDK111, IBM112)
2. Rodzaje testow (tabelka) macro-benchmarki (cale programy)
3. Dlaczego testy na programach jedno-watkowych? Dlatego, ze thin-locki zdejmuja duze obciazenie jakie daja standardowe mechanizmy Javy kiedy jest malo wspoldzielen obiektow, wiec bardzo dobrze widac roznice na programach jedno-watkowych
4. Pomiary jakie rodzaje operacji wystepuja najczesciej (najwiecej jest malo zagnieżdzonych, zagniezdzenie nie przekroczylo ani razu 4 poziomow, 256 zakladane przez tworcow to spora nadwyzka)
5. Micro-benchmarki (konkretne operacje odpalone w petli) i ich rodzaje
6. Opisanie wynikow micro-benchmarkow
7. Porownanie przyspieszenia think-lock wzgledem pozostalych podejsc (srednio 1.22, max 1.7)

## Podsumowanie

1. Troche podobne do MCS lockow ale uzywaja operacje sprzetowych, przez co sa lepsze
2. Think-locki zostaly zaimplementowane w Sun JDK
3. Dla microbenchmarkow moga dawac one nawet 5 krotne przyspieszenie wzgledem oryginalnego JDK
4. Dla normalncyh programow daja srednio 1.22, max 1.7 przyspieszenia
5. Nie zwekszaja wielkosci obiektu, bo sa w headerze
6. Fat-locki sa tworzone TYLKO podczas rywalizacji, wiec podjescie think-lockowe szczegolnie zmniejsza uzycie pamieci kiedy mamy bardzo duzo obiektow wspolbieznych, bo wiekszosc nie bedzie uzyta podczas rywalizacji
