#### Pamięć z mapowaniem  bezpośrednim

- **tag**: $2$ bity 
- **index**: $2$ bity
- **offset**: $1$ bit

$4$ zbiory po $1$ blok

| tag  | index | offset | hit             |
| ---- | ----- | ------ | --------------- |
| 00   | 00    | 0      | compulsory miss |
| 00   | 10    | 0      | compulsory miss |
| 01   | 10    | 0      | conflict miss   |
| 00   | 00    | 0      | hit             |

#### Pamięć dwudrożna z LRU

- **tag**: $3$ bity 
- **index**: $1$ bity
- **offset**: $1$ bit

$2$ zbiory po $2$ bloki.

| tag | index | offset | hit             |
| --- | ----- | ------ | --------------- |
| 000 | 0     | 0      | compulsory miss |
| 001 | 0     | 0      | compulsory miss |
| 011 | 0     | 0      | conflict miss   |
| 000 | 0     | 0      | conflict miss   |
