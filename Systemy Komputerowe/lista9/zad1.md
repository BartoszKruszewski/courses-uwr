#### Bufor predykcji skoków

Bufor predykcji skoków służy do dynamicznego przewidywania skoku w programie. Sprawdzamy go już fazie **Fetch**, dzięki czemu możemy szybciej ustalić czy opłaca się wykonywać instrukcje programu występujące bezpośrednio po instrukcji skoku.

#### Bufor jednobitowy

Bufor jednobitowy ma dwa stany:

- not taken (0)
- taken (1)

#### Bufor dwubitowy

Bufor dwubitowy ma 4 stany:

- strongly not taken (00)
- weakly not taken (01)
- weakly taken (10)
- strongly taken (11)

#### Działanie

W obu przypadkach ponawiamy wykonanie działania z bufora, a jeżeli skok rzeczywiście zostanie wykonany zwiększamy wartość o 1, w przeciwnym razie zmniejszamy o 1.

#### Przykładowy program

```
L1:     ...
(1)     if b goto L3
MAIN:     ...
(2)     if a goto L1
        ...
        goto MAIN
L3:     ...
```

Predykator statyczny, dla skoku $(2)$ będzie przewidywał skok, ponieważ jest to skok do tyłu. Natomiast w tym programie $(2)$ jest skokiem wyjścia z głównej pętli, więc zostanie wykonany tylko raz. Stąd predykator statyczny pomyli się $(n - 1)$ liczbę razy. Predykator z buforem pomyli się tylko raz, ponieważ tylko ostatni skok zostanie źle przewidziany, a każdy poprzedni poprawnie. Dla skoku $(1)$ oba predykatory zachowają się tak samo.

W sytuacji, w której użylibyśmy predykatora statycznego, który przewiduje skoki "na odwrót", to wtedy dla skoku $(2)$ poprawność będzie identyczna jak dla predykatora z buforem, natomiast źle zostanie przewidziany skok $(1)$.

#### Implementacja

Bufor predykatora można przechowywać na dwa sposoby:

- dodatkowa pamięć instrukcji _(bardziej pamięciożerne)_
- osobny moduł _(bardziej oszczędnie)_

#### Uogólnienie dla n-bitów

Jeżeli wykonano skok zwiększ licznik o $1$, zmniejsz wpp. $1$ w najbardziej znaczącym bicie oznacza przewidanie skoku, a $0$ przewidywanie braku skoku.
