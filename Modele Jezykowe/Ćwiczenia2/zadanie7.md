# Zadanie 7

**Pomysł:** kodowanie arytmetyczne z rozkładem z Papugi. Każdy token kosztuje około `−log₂ P(token | kontekst)` bitów: token o szansie 1/2 to 1 bit, o szansie 1/1024 to 10 bitów. Papuga dobrze przewiduje polski tekst, więc kod jest krótki.

**Kompresja:** dla kolejnych tokenów (na końcu `EOS`) pytamy Papugę o rozkład następnego tokenu i zawężamy przedział do części odpowiadającej temu tokenowi. Wynikiem są bity wskazujące liczbę z końcowego przedziału.

**Dekompresja:** dekoder ma tę samą Papugę, więc dostaje te same rozkłady. Z bitów odczytuje, w przedział którego tokenu trafia liczba, dopisuje ten token do kontekstu i powtarza aż do `EOS`.

**Warunek:** obie strony muszą dostać identyczne rozkłady, więc liczymy na CPU i kwantyzujemy prawdopodobieństwa.
