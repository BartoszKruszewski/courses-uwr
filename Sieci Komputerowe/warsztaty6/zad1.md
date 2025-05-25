### Flagi TCP w przesyłanych segmentach

| Nr | Flagi TCP     | Znaczenie                      |
|----|---------------|--------------------------------|
| 1  | SYN           | Rozpoczęcie połączenia         |
| 2  | SYN, ACK      | Odpowiedź serwera              |
| 3  | ACK           | Potwierdzenie klienta          |
| 4+ | PSH, ACK      | Transmisja danych HTTP         |
| n  | FIN, ACK      | Zamykanie połączenia           |

### Bajty przesyłane i potwierdzane

- **Bajty przesyłane:** określane przez `Seq` i `Len`, np. `Seq=1 Len=512` oznacza bajty 1–512.
- **Bajty potwierdzane:** określane przez `ACK`, np. `ACK=513` oznacza potwierdzenie otrzymania bajtów do 512.

### Stany TCP według diagramu

#### Klient (otwarcie aktywne):
- `CLOSED -> SYN_SENT -> ESTABLISHED -> FIN_WAIT1 -> FIN_WAIT2 -> TIME_WAIT -> CLOSED`

#### Serwer (otwarcie pasywne):
- `LISTEN -> SYN_RECEIVED -> ESTABLISHED -> CLOSE_WAIT -> LAST_ACK -> CLOSED`

- **Otwarcie aktywne:** klient (wysyła SYN)
- **Zamknięcie aktywne:** klient (wysyła FIN)