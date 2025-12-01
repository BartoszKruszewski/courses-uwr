#### Konstrukcje

```java
class TASlock {
    AtomicBoolean state = new AtomicBoolean(false);
    void lock() {
        while (state.getAndSet(true)) {}
    }
    
    void unlock() {
        state.set(false);
    }
}

class TTASlock {
    AtomicBoolean state = new AtomicBoolean(false);
    void lock() {
        while (true) {
            while (state.get()) {}
            
            if (!state.getAndSet(true))
                return;
        }
    } 
}
```

#### Metryki

- Liczba operacji w sekcji krytycznej na jednostkę czasu
- Czas oczekiwania na zdobycie wolnego zamka
- Ruch na magistrali

#### TAS (Test-And-Set)

Ciągłe wywoływanie atomowej instrukcji `TAS` w pętli (operacja zapisu RMW)

Każda próba (nawet nieudana) unieważnia linię cache u innych procesorów (MESI: Invalidate)

Nasycenie łącza spowalnia nawet wątek posiadający zamek

#### TTAS (Test-Test-And-Set)

Najpierw sprawdza wartość zwykłym odczytem, dopiero gdy zamek wydaje się wolny, wykonuje atomowy `TAS`

Dzięki temu wątki wirują na lokalnej kopii w cache (MESI: stan Shared)

Drastycznie redukuje to ruch na magistrali
