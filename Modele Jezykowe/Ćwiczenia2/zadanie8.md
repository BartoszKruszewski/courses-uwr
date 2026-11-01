# Zadanie 8

| Prefiks | Bez spacji | Ze spacją |
|---|---|---|
| Wczoraj poszedłem do | ` lekarza` 0.055 | `laryngo` 0.975 |
| Stolicą Polski jest | ` Warszawa` 0.402 | `ród` 0.361 |
| Najważniejszą rzeczą w życiu jest | ` to` 0.091 | `rządzenie` 0.632 |

Bez spacji tekst jest normalny, ze spacją dziwny („Stolicą Polski jest ród Piastów”).

**Wyjaśnienie:** tokenizer dokleja spację do początku następnego tokenu (` lekarza`). Spacja na końcu prefiksu to osobny, rzadki token, po którym zostają tylko fragmenty słów. Szansa, że następny token zaczyna się spacją, spada średnio z 0.927 do 0.004.
