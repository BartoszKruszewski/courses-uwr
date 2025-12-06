#### OptimisticList bez blokad w `contains()`: JEST linearyzowalny

W standardowej OptimisticList usunięcie węzła jest operacją atomową z punktu widzenia struktury listy (zmiana wskaźnika pred.next). Nie ma tam "fazy przejściowej" (jak w LazyList), w której węzeł jest "logicznie usunięty", ale "fizycznie obecny".

Węzeł jest w zbiorze tak długo, jak jest osiągalny z head.

Operacja `remove(A)` zmienia wskaźnik w jednym kroku (fizyczne odpięcie). To jest jej punkt linearyzacji.

Operacja `contains(A)` (zmodyfikowana, bez blokad) po prostu przeszukuje listę.

- Jeśli znajdzie A: 

    Oznacza to, że w momencie odczytu wskaźnika prowadzącego do A, węzeł A był jeszcze w liście. Możemy zlinearyzować `contains(A)` w tym właśnie momencie.

- Jeśli nie znajdzie A: 

    Oznacza to, że w żadnym momencie swojej wizji listy nie widziała A. Zwraca false.

Nie ma możliwości, aby contains(A) rozpoczęło się po zakończeniu remove(A) i mimo to znalazło A.

Skoro remove(A) fizycznie odcina węzeł od head, to nowe wywołanie contains nie ma jak do niego dotrzeć. "Widzenie" usuniętych węzłów jest możliwe tylko wtedy, gdy contains wystartowało przed lub w trakcie usuwania, co czyni te operacje współbieżnymi – a w takim przypadku true jest dopuszczalnym wynikiem.

#### LazyList bez sprawdzania marked w `contains()`: NIE JEST linearyzowalny

Rozważmy sekwencję zdarzeń, w której operacje nie są współbieżne (następują jedna po drugiej):

- Wątek A wywołuje `remove(x)`.

    Ustawia `x.marked = true`.

    To jest punkt linearyzacji usunięcia! Od teraz x oficjalnie nie ma w zbiorze.

    Wątek A zasypia przed fizycznym odpięciem węzła (przed zmianą `pred.next`).

- Wątek B wywołuje contains(x) (zmodyfikowane, ignoruje marked).

    Zaczyna przeszukiwanie od head.

    Ponieważ x fizycznie wciąż jest w liście, Wątek B dociera do węzła x.

    Sprawdza klucz: zgadza się.

    Ignoruje bit marked.

    Zwraca true.

Operacja contains(x) zwróciła true, mimo że rozpoczęła się całkowicie po punkcie linearyzacji operacji remove(x). Jest to naruszenie warunku linearyzowalności.
