# Zadanie 5

**Zasada:** bezpieczeństwo zależy tylko od tajności klucza, algorytm może być jawny.

**Ocena:** formalnie spełniona, ale model to słaby klucz: bywa publiczny, można go skopiować i trudno wymienić.

**Naprawa:** kluczem staje się krótki sekret `K` ustalony wcześniej, a model może być jawny.

1. Z `K` i numeru listu powstaje pseudolosowy ciąg bitów `S`. Numer listu sprawia, że ciąg się nie powtarza.
2. Szyfrujemy: `c = wiadomość XOR S`, i to `c` ukrywamy w liście metodą z zad. 4.
3. Towarzysze odczytują `c` i liczą `c XOR S`, co daje wiadomość.
