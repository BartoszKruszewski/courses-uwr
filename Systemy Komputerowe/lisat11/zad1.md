#### Róźnica dla sąsiednich lokalnie adresów
- **środkowe bity**: podobne tagi, ale różne zbiory i offsety
- **najstarsze bity**: podobne zbiory, ale rózne tagi i offsety

#### Korzyści
Największe korzyści z uzywania pamięci cache występują podczas iteracji po tablicy. Maksymalizując podobieństwo tagów maksymalizujemy ilość trafień we wcześniej uzywany tag.