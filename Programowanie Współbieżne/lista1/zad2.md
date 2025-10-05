Problem **sekcji krytycznej** polega na tym, że dwa wątki chcą wykorzystać współdzielone zasoby w tym samym czasie, przez co nie są w stanie operacować na aktualnych danych.

#### Protokół Alicji

1. Podnosienie flagi
1. Pociągniecie za sznurek
1. Czekanie dopóki flaga Boba jest podniesiona i wskaźnik wskazuje na Boba
1. Wpuszczenie smoka do jeziora
1. Opuszczenie flagi jak smok wróci

#### Protokół Boba

1. Podnosienie flagi
1. Pociągniecie za sznurek
1. Czekanie dopóki flaga Alicji jest podniesiona i wskaźnik wskazuje na Alicję
1. Wpuszczenie smoka do jeziora
1. Opuszczenie flagi jak smok wróci

#### Intuicja

Jeśli tylko jeden smok chce wejść, warunek oczekiwania jest fałszywy i wchodzi natychmiast. Gdy chcą wejść jednocześnie, obaj ustawiają wskaźnik na rywala, co wymusza naprzemienność.