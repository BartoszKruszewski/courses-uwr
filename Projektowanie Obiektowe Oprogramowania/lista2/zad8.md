```mermaid
stateDiagram-v2
    [*] --> Oczekiwanie
    Oczekiwanie --> Wybór_napoju
    Wybór_napoju --> Płatność
    Płatność --> Przygotowanie_napoju: zatwierdzona
    Przygotowanie_napoju --> Wydanie_napoju
    Wydanie_napoju --> Oczekiwanie: Napój wydany
    Płatność --> Oczekiwanie: odrzucona
    Przygotowanie_napoju --> Zwrot_środków: Brak składników
    Zwrot_środków --> Oczekiwanie