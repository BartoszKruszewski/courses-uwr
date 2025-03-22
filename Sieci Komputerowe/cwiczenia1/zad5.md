Najlepsze dopasowanie w tablicy routingu to takie ktore ma najwiecej pasujacych pierwszych bitow.

Stad zeby uzyskac efekt "pierwszy dopasowany - najlepszy dopasowany" najlepiej posortowac wpisy po długości adresu (malejaco wzdlegem wartosci CIDR).

Dowod formalny:

Zalozenia: tablica jest posortowana malejaco wzgledem dlugosci bitow
Teza: Pierwsze dopasowanie bedzie najlepszym dopasowaniem

Wezmy adres i znajdzmy jego pierwsze dopasowanie (Zakladamy ze jakies dopasowanie istnieje, inaczej i tak nie ma z czym porownac). Poniewaz adres zostal dopasowany to jego $x$ pierwszych bitow jest dopasowane. Wezmy dowolne inne dopasowanie, wtedy $y$ bitow zostalo dopasowane. Z zalozenia ze tablica jest posortowana malejaco wiemy ze dowolny inny adres byl tak samo dlugi lub krotszy. Stad $x \ge y$, wiec z definicji pierwsze dopasowanie jest tak samo dobre lub lepsze niz dowolne inne, wiec jest najlepsze.