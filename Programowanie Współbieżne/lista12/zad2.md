#### Problem ABA

Problem ABA polega na fałszywie udanym `compareAndSet()`, gdy referencja zmienia się z A na B i z powrotem na A, ukrywając pośrednie modyfikacje stanu struktury danych.
​
#### Występowanie

Problem objawia się w algorytmach lock-free (np. kolejka bez blokad), gdy wątek śpi po odczycie A inne wątki usuwają i ponownie wstawiają A, powodując błędne przepięcie na B z listy recyclingu. `compareAndSet()` nie wykrywa zmian kontekstu wokół A, naruszając niezmienniki struktury.

​
#### Mechanizm zapobiegania - Dodanie sygnatur

Węzeł ma tag/licznik wersji, zmieniany przy każdej modyfikacji CAS na parze (ref+tag) zawiedzie przy zmianie A na B na A.

#### Sprzętowy mechanizm zapobiegania

LL/SC (Load-Link/Store-Conditional): Sprzętowe monitorowanie modyfikacji między load a store – każda interferencja resetuje flagę, blokując zapis
