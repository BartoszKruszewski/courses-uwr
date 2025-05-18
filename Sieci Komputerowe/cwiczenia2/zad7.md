Używamy CRC z wielomianem: $G(x) = x^3 + x + 1$

Nadajemy wiadomość 4 bity (1101) + 3 dodatkowe bity CRC = 7 bitów

Co najwyżej jeden bit został przekłamany

Odbiorca używając CRC sprawdza czy $G(x)$ dzieli naszą odebraną ramkę

Jeżeli bit został przekłamany to otrzymujemy niezerową resztę

Sprawdźmy jak będzie wyglądać reszta przy zmianie poszczególnych bitów:

| Pozycja bitu (0 = najmniej znaczący) | Wielomian $x^k \bmod G(x)$ | reszta (format binarny) |
|--------------------------------------|----------------------------|-------------------------|
| 0                                    | $1$                        | 001                     |
| 1                                    | $x$                        | 010                     |
| 2                                    | $x^2$                      | 100                     |
| 3                                    | $x + 1$                    | 011                     |
| 4                                    | $x^2 + x$                  | 110                     |
| 5                                    | $x^2 + x + 1$              | 111                     |
| 6                                    | $x^2 + 1$                  | 101                     |

Jak możemy zauważyć reszta w każdym przypadku jest inna

Po wtyliczeniu reszty można spojrzeć w tabelkę i odczytać który bit został przekłamany i go zanegować
