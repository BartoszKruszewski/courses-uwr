# Zadanie 1

**Pojęcia:**
- **Perplexity:** miara tego, jak bardzo tekst zaskakuje model: `exp(−średni log P(token | poprzednie))`. Im niższa, tym tekst bardziej przewidywalny.
- **Temperatura:** dzieli logity przed softmaxem. Niska wzmacnia najbardziej prawdopodobne tokeny, wysoka wyrównuje rozkład.
- **Top-p:** losowanie tylko z najbardziej prawdopodobnych tokenów, których łączne prawdopodobieństwo sięga `p`.

**Dlaczego działa:** model wybiera tokeny dla siebie prawdopodobne, człowiek częściej zaskakuje.

**Wady:** teksty urzędowe i cytaty dają fałszywe alarmy, wynik zależy od modelu detektora, krótkie teksty to szum.

**Kontrola:** temperatura, top-p, prompt („pisz nietypowo”), parafraza.
