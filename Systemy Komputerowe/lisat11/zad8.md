#### Zasada działania

Zauważmy, że często występuje sytuacja (np w zadaniu 3), gdzie $VPO = PPO$. Co za tym idzie w momencie rozpoczęcia odczytywanie wartości z TLB (lub w przypadku miss z tablicy stron) za pomocą VPN, możemy równolegle odczytać CI oraz CO z VPO i pobrać odpowiedni zbiór z cache'u. Taka optymalizacja sprawia, że w momencie odczytania CT, możemy od razu rozpocząć szukanie bloku o znalezionym tagu zamiast rozpoczynać wyszukiwanie zbioru.

#### Podstawowa wersja

```
VPN, VPO -> TLBT, TLBI, PPO -> CT, CI, CO -> pobranie zbioru -> wyszukanie bloku za pomocą CT
```

#### Zoptymalizowana wersja

```
VPO -> CI, CO     -> pobranie zbioru -> wyszukanie bloku za pomocą CT
VPN -> TLBT, TLBI -> CT
```

#### Podsumowanie

Jak widać na powyższych schematach, zrównoleglając translacje możemy ją skrócić o jeden etap obliczeń
