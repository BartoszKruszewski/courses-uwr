Robimy "romby"

```
       O
      / \
     O---O
      \ /
       O
       |
       O
      / \
     O---O
      \ /
       O
       |
       O
      / \
     O---O
      \ /
       O
```

Zakladajac ze na wejsciu takiego romba mamy $k$ kopii komunikatow rozsylamy je do dwoch wewnetrznych routerow romba a nastepnie przesylamy do wyjscia. Wyjscie ma teraz $2k$ kopii komunikatow ale tylko jedna linie do przesylania wiec przeslanie zajmie $2k$ czasu.

Zauwazmy ze romb sklada sie z czterech routerow, wiec mamy $n/4$ rombow, wiec do ostatniego rombu trafi $2^{n/4 - 1}$ kopii, co spelnia $2^{\Omega(n)}$

