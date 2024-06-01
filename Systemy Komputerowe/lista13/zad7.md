#### Podział procesów

Procesy mają różną "ważność" dla działania komputera. Możemy je podzielić na grupy z wagą malejąco:

1. Real-time: wymagające ciągłej synchronizacji
2. System: - niezbędne do działania systemu
3. Interactive: - interakcje z użytkownikiem
4. Batch: - mogące działać w tle

### Algorytm Multilevel feedback queues

Procesów przypisywane są do odpowiedniej kolejki w zależności od tego do jakiej należą grupy. Zauważmy, że im jest większy priorytet grupy tym procesy wymagają większej interaktywności. Algorytm promuje procesy bardziej interaktywne.

#### Reguła promocji i degradacji

- Jeśli proces zużywa zbyt dużo czasu procesora, zostanie przeniesiony do kolejki o niższym priorytecie.
- Jeśli proces jest interaktywny, zostanie przeniesiony do kolejki o wyższym priorytecie.
- Jeśli proces czeka zbyt długo, zostanie przeniesiony do kolejki o wyższym priorytecie.
