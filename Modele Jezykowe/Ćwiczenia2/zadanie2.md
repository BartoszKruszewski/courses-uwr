# Zadanie 2

**Metoda naturalna:** jeśli dane słowo pada z szansą 1/1000, to na jeden sukces trzeba około 1000 prób. Przy 10 takich warunkach byłoby to już `1000¹⁰` prób.

**Pomysł:** nie odrzucamy gotowych tekstów, tylko od razu losujemy z uwzględnieniem warunku.

## a) Słowo `w` na pozycji k
Zaczynamy od `w`, nie od początku tekstu:
- w prawo losujemy zwykle: `P(następne | w)`,
- w lewo losujemy z odwróconych zliczeń: `P(poprzednie | w) = c(poprzednie, w) / c(w)`.

Warunek jest spełniony zawsze.

## b) Ustalone pozycje parzyste
Każde losowane słowo `x` ma znanych obu sąsiadów, więc wybieramy je osobno:

`x ~ P(x | lewy) · P(prawy | x)`

Drugi czynnik gwarantuje, że `x` pasuje do słowa po prawej.

## c) Zadane pierwsze i ostatnie słowo
Najpierw liczymy od końca tabelę `β_t(w)`, czyli szansę dojścia z `w` do słowa końcowego w dokładnie `t` krokach:
- `β_0(koniec) = 1`, dla innych słów `β_0 = 0`,
- `β_t(w) = Σ_v P(v | w) · β_{t-1}(v)`.

Potem losujemy od pierwszego słowa, gdy zostało `t` kroków:

`następne ~ P(następne | w) · β_{t-1}(następne)`

Słowa, z których nie da się dojść do końca, mają `β = 0`, więc nigdy nie wejdziemy w ślepą uliczkę.

## d) i-te słowo ma sufiks `s_i`
`C_i` to słowa ze słownika o sufiksie `s_i`. Tylko one są kandydatami na pozycję `i`.

1. **Forward:** `α_1(w) = P(w)`, a dalej `α_i(w) = Σ_{v ∈ C_{i-1}} α_{i-1}(v) · P(w | v)`.
2. **Losowanie wstecz:** ostatnie słowo `w` wybieramy proporcjonalnie do `α_n(w)`, a poprzednie `v` proporcjonalnie do `α_{i-1}(v) · P(w | v)`.

Każda wylosowana ścieżka spełnia warunek, bo w kracie są tylko słowa z właściwym sufiksem.
