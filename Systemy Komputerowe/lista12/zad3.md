#### Podpunkt a

Dla danych posortowanych algorytmy LRU, FIFO oraz clock będą działać identycznie.
Po wypełnieniu pamięci kolejne wartości za każdym razem będa zastępować swoich poprzedników, przez co będzie popełniać błąd prawie przy każdej operacji. Powyższe algorytmy dodatkowo zignorują to, że strony 431 oraz 332 występują znacznie częściej niż pozostałe.

#### Podpunkt b

Istnieje algorytm optymalny dla tego konkretnego ciągu, zakładający zapamiętanie stron 332, 431 oraz 497 z pozostałych stron, a jedną ramkę przeznaczyć na wczytywanie pozostałych 13 stron. Ta strategia zadziała tylko dla tego konkretnego ciągu i nie jest uniwersalna.

Istnieje bardziej uniwersalny algorytm pamiętający częstotliwość użycia stron. Wtedy nie musimy wyrzucać z pamięci liczb 431 oraz 332, co znacznie zmniejszy ilość błędów. Strony 332 oraz 431 wczytane z ciągu są oddalone od "przerw" pomiędzy ciągami o odpowiednio $511 - 332 = 179$ i $511 - 431 = 80$ operacji, więc jeżeli zastosujemy algorytm, który pamięta dla każdej strony liczbę odwołań do niej i przesuwa w kolejce FIFO tylko strony które mają najniższy priorytet to strony 332 oraz 431 nigdy nie zostaną usunięte z pamięci, ponieważ zanim ich pierwsze wystąpienia zostaną usunięte z kolejki to nastąpi "przerwa" w ciągu i ich liczność odwołań zostanie zwiększona.
