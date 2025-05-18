$p = 0.01$ to ppb błedu

$q = 1-p = 0.99$ to ppb poprawności

$q^{100} = 0.99^{100} \approx 0.36$ to ppb, że ramka bez kodowania jest poprawna

Przy kodowaniu Hamminga(7, 4) mamy $100 / 4 = 25$ 4-bitowych bloków.

Każdy blok kodujemy do 7 bitów, więc mamy $25 \cdot 7 = 175$ bitów.

Blok jesteśmy w stanie naprawić jeżeli ma jeden bit błędu.

Stąd ppb otrzymania poprawnego bloku to:

x = $q^{7} + \binom{7}{1} \cdot p \cdot  q^{6} = 0.99^{7} + 7 \cdot 0.01 \cdot 0.99^{6} \approx 0.99797$

Dla całej ramki to 

$x^{25}\approx 0.99797^{25}\approx 0.950$

