#### Algorytm

```java
class Bouncer {
    private boolean goRight = false;
    private int last = -1;

    int visit() {
        int i = ThreadID.get();
        last = i;
        if (goRight) return RIGHT;
        goRight = true;
        return if (last == i) ? STOP : DOWN;
    }
}
```

#### Co najwyżej jeden wątek otrzyma STOP

Przez `if (goRight)` można przejśc tylko "jednocześnie", ponieważ po jego przejściu wywołane jest `goRight = true`

Wszystkie wątki które tam są wywołały `last = i`

Więc wartość `last` jest ustawiona na co najwyżej jednego z nich i on otrzyma `STOP`.

#### Co najwyżej n-1 wątków otrzyma wartość DOWN

Przez `if (goRight)` można przejśc tylko "jednocześnie", ponieważ po jego przejściu wywołane jest `goRight = true`

Nawet jeżeli wszystkie wątki przeszły w tym samym czasie to `last` jest ustawiona na co najwyżej jednego z nich.

Wtedy on otrzyma `STOP` a reszta (czyli $n-1$) `DOWN`.

#### Co najwyżej n-1 wątków otrzyma wartość RIGHT

Pierwszy wątek musi przejść przez `if (goRight)`, więc `RIGHT` otrzyma co najwyżej reszta bez niego. 