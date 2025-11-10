#### Konstrukcja

Używamy tyle atomowych rejestrów MRSW ilu mamy pisarzy.

Każdy pisarz sprawdza jaki jest najwyższy timestamp w każdym rejestrze, zwiększa go o jeden i zapisuje wartość.

Czytający sprawdzają jaki jest najwyższy timestamp w każdym rejestrze i odczytuja jego wartość.

Jeżeli dwóch pisarzy zapisze identyczny timestamp (jest to możliwe) to czytający rozróżniają te wpisy leksykograficznie (jak w algorytmie piekarni).

#### Obserwacje

- `read()` nie może zwrócić wartości zapisanej po jego zakończeniu, bo jego max nie zobaczy nowego timestampu
- jeśli pisarz `A` zapisał przed pisarzem `B` to nastepny read zwróci wartość `B`, jeżeli `A` i `B` zapiszą równocześnie to zawsze zwrócony zostanie `A` bo jest pierwszy leksykograficznie
- jeśli wcześniejszy read zwrócił `D`, to późniejszy nie może zwrócić wcześniejszego `C`, bo slot D nadal ma co najmniej ten sam największy znacznik, przy remisach po liczbie wygrywa większe id zgodnie z porządkiem.
​
#### Linearyzacja `write()`

Write liniaryzuje się w momencie atomowej publikacji pary `(timestamp, wartość)`. 

Po tej chwili każdy czytelnik może ją odczytać, a porządek leksykograficzny ustala jej miejsce w historii.

#### Linearyzacja `read()`

Read liniaryzuje się w chwili wyboru maksymalnej pary

Zwracana wartość odpowiada ostatniemu write’owi w porządku leksykograficznym.
