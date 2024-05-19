| id  | czas przybycia | bit referenced |
| :-: | :------------: | :------------: |
|  B  |       3        |       1        |
|  C  |       7        |       1        |
|  D  |       8        |       0        |
|  E  |       12       |       1        |
|  F  |       14       |       1        |
|  G  |       15       |       0        |
|  H  |       18       |       1        |
|  A  |       20       |       1        |

Strony B oraz C są z przodu kolejki, ale mają bit referenced ustawiony na 1, więc zostaną przesunięte z bitem referenced ustawionym na 0 na koniec kolejki. Strona D ma bit referenced ustawiony na 0, a po przeniesieniu B oraz C, będzie się znajdować z przodu kolejki, więc ona zostanie zastąpiona.
