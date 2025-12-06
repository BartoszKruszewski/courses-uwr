#### Definicja problemu

Mamy tablice 3 elementową. Chcemy konstrukcję spęlniającą interfejs:

```java
interface Assign2 {
    public void assign(int i1, int v1, int i2, int v2);
    public int read(int i);
}
```

Która pozwala na atomowy zapis dwóch wartości.

Sprowadza się to do tego, że wątki nie powinny edytować dwóch tych samych elementów tablicy w tym samym czasie.

#### Konstrukcja

```java

R1, R2, R3 = {-1, -1, -1};
MRMW[3] array; 

void assign(int i1, int v1, int i2, int v2){
    r = {
        [0, 1]: R1,
        [0, 2]: R2,
        [1, 2]: R3,
    }[sort([i1, i2])]; // rozroznienie czy indeksy sa rozlaczne

    r.compareAndSet(-1, ThreadID); // oznaczenie rozpoczecia zapisu
    
    if register.get() == ThreadID {
        array[i1] = v1;
        array[i2] = v2;
        r.set(-1); // oznaczenie zakonczenia zapisu
    }
}

int read(int i) {
    return array[i];
}
```

#### Intuicja

Konstrukcja wykorzystuje rejestry RMW do rozróżnienia czy występuje równolegla chęć zapisu do dwóch tych samych rejestrów.

Do każdego rejestru jest przypisana jedna kombinacja indeksów tablicy.

W przypadku gdy indeksy pokrywają się, wątki robią "wyścig" za pomocą instrukcji CAS o zajęcie rejestru oznaczającego odpowiednią kombinację.

W rezultacie zapis dokonywany jest tylko przez jeden wątek.

#### Pozostałe przypadki

Jeżeli indeksy nie pokrywają się (jakiś indeks się różni), to wtedy we wspólnym polu będzie wartość proponowana przez wątek, który dokonał zapisu później (tak jak powinno być).