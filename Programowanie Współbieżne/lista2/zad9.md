#### Własności

- Co najwyżej jeden wątek otrzyma STOP
- Co najwyżej $n-1$ wątków otrzyma wartość DOWN
- Co najwyżej $n-1$ wątków otrzyma wartość RIGHT
- Jeżeli jest przynajmniej jeden odwiedzający to będzie przynajmniej jeden STOP
- Każde pole odwiedzi co najwyżej $k-1$ wątków, gdzie $k$ to suma wątków które odwiedziły pola poprzedzające

#### Nieograniczony graf

Wiemy, że liczba wątków odwiedzających kolejne wierzchołki zmniejsza się.

Jeżeli graf jest nieograniczony to wiemy, że kiedyś liczba odwiedzających spadnie do 1, który otrzyma STOP.

Jeżeli nie ma odwiedzających to znaczy, że wszyscy otrzymali STOP.

#### Liczba potrzebnych wierzchołków

Zauważmy, że w każdej przekątnej grafu ilość odwiedzających będzie mniejsza o co najmniej jeden mniejsza.

Więc potrzeba $n$ przekątnych, żeby mieć pewność, że dla każdego wątku zostanie wywołany STOP.

Taki graf, który ma $n$ przekątnych ma $1 + 2 + ... + n = \frac{n * (n - 1)}{2}$ wierzchołków.
