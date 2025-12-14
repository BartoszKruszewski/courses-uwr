#### Problem

Wątki mogą równolegle modyfikować te same wskaźniki, gubiąc elementy i naruszając uporządkowanie listy.

CAS na `prev.next` nie informuje, że węzeł jest usuwany – wątki mogą wchodzić na "umierające" węzły, wstawiając za nimi lub opierając się na nich, co łamie założenia zbioru.

#### `AtomicMarkableReference`

Ta klasa posiada atomową metodę:

```java
compareAndSet(
    T expectedReference, 
    T newReference, 
    boolean expectedMark, 
    boolean newMark
)
```
​
#### Rozwiązanie

`AtomicMarkableReference` umożliwia dwuetapowe usuwanie:

- najpierw logiczne (ustaw `mark=true` na next)
- potem fizyczne (CAS omijający zaznaczony węzeł).

Każdy widzi usunięte węzły i może je "posprzątać".
