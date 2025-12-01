#### Zasada lokalności odwołań

Jeżeli procesor używa adresu w pamięci to w najbliższym czasie z dużym ppb będzie używać ponownie tego adresu albo sąsiednich.

#### Zastosowanie w pamięciach podręczne

Pamięci podręczne kopiują większe porcje danych z pamięci operacyjnej.

Dzięki temu, zgodnie z zasadą lokalności odwołań, istnieje duża szansa, że procesor będzie wykonał kosztowne odwołanie do pamięci operacyjnie tylko raz, a wiele następnych będzie wykonanych szybko do pamięci podręcznej.

#### Po co protokoły spójności?

Każdy procesor posiada własną pamięć podręczną, ale współdzieli pamięć główną RAM. Prowadzi to do problemu spójności danych.

Jeśli dwa procesory pobiorą tę samą daną do swoich prywatnych pamięci cache, a następnie jeden z nich ją zmodyfikuje, drugi procesor wciąż będzie posiadał w swoim cache'u starą, nieaktualną wartość.

Bez mechanizmu synchronizacji procesory operowałyby na różnych wartościach tej samej zmiennej.

#### Protokół MESI

Wyróżniamy cztery stany:
- **Modified**: Linia jest tylko w cache'u i została zmodyfikowana. Jej wartość różni się od tej w pamięci RAM. Procesor musi zapisać ją do RAM przed usunięciem z cache'
- **Exclusive**: Linia jest tylko w tym cache'u, ale nie została zmieniona. Jej wartość jest zgodna z pamięcią RAM. Procesor może ją zmodyfikować bez informowania innych (przejdzie wtedy w stan M)
- **Shared**: Linia może znajdować się w wielu cache'ach jednocześnie. Jest zgodna z RAM. Procesor może ją tylko odczytać. Próba zapisu wymaga unieważnienia kopii w innych procesorach
- **Invalid**: Linia w cache'u jest nieaktualna i nie nadaje się do użycia (np. inny procesor zmodyfikował te dane u siebie)

Gdy procesor chce zmodyfikować daną, która jest w stanie Shared, musi wysłać sygnał na magistralę, który nakazuje innym procesorom zmianę stanu tej linii na Invalid.

Dopiero gdy uzyska wyłączność (stan Exclusive lub Modified), może dokonać zapisu.

Jeśli inny procesor zażąda odczytu danej będącej w stanie Modified, właściciel musi najpierw zapisać ją do pamięci głównej, zmieniając stan na Shared.
