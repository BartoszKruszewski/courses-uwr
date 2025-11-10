#### $(*) (**) (***) => atomowość$

Z poprzedniego zadania wiemy, że (*) oraz (**) daje regularność.

Warunek (***), mówi że dla każdych $i$ oraz $j$ jeśli zachodzi $R^i \rightarrow R^j$ to $i \le j$

Czyli, że odczyty zachowują kolejność zapisów, co w połączeniu z regularność sprawia, że takie historie są linearyzowalne.

Czyli rejestr jest atomowy.

#### $atomowość => (*) (**) (***)$

Jeżeli rejestr jest atomowy to tym bardziej jest regularny, więc wiemy z poprzedniego zadania, że zachodzi (*) oraz (**).

Jeżeli jest atomowy to historia współbieżnych dostępów jest linearyzowalna, więc zachowuje porządzek odczytów, co mówi (***).