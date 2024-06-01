#### Algorytm

```
while (nie ma procesu do wykonania):
    for proces in queue:
        Wybierz proces o najwyższym priorytecie, który jest załadowany do pamieci
    if (nie ma takeigo procesu):
        Bezczynność maszyny
Usuń wybrany proces z kolejki uruchomień
Przełącz kontekst na wybrany proces i wznów jego wykonanie
```

Jest to algorytm Karuzelowy z wielopoziomowymi kolejkami, oraz priorytetami.

#### Własności algorytmu

- wybierany jest proces z kolejki o najwyższym priorytecie
- jeżeli priorytety są równe, to wybierany jest ten, który dłużej był "ready"
- są dwie grupy kolejek: kolejski jądra systemu, oraz kolejki użytkownika. Nie mogą one przeskakiwać pomiędzy sobą.
- kolejki jądra systemu są podzielone w zależności od ważności dla działania komputera
- priorytety w kolejkach użytkownika są ustalane na podstawie przypisania przez użytkownika, oraz poprzez sprawdzanie czasu dostępu do procesora
- superuser może dodatkowo zapalić wartość "nice" dla procesu, która dodatkowo zwiększa jego priorytety
