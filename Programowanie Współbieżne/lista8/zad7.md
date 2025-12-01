#### Algorytm (lista 7 zadanie 6)

```java
public class ConsensusProposal {
    Boolean proposed[] = new Boolean[2];
    Integer[] speed = new Integer[2];
    Integer[] position = new Integer[2];

    public ConsensusProposal(){
        position[0] = 0;
        position[1] = 0;
        speed[0] = 3;
        speed[1] = 1;
    }

    public Boolean decide(Boolean value) {
        int i = ThreadID.get(); //0 or 1
        int j = 1 - i;
        proposed[i] = value;
        while (true) {
            position[i] = position[i] + speed[i];
            if (position[i] > position[j] + speed[j]) // I am far ahead of you
                return proposed[i];
            else if (position[i] < position[j]) // I am behind you
                return proposed[j];
        }
    }
}
```

#### Intuicja

Wątki zapisują swoje propozycje do rejestów.

Ustalamy rejestry z pozycjami wątków oraz prędkości (różne dla każdego wątku).

Wątki "ścigają się", zwiekszając swoją pozycję o prędkość.

Wątki znają swoje pozycje, więc mogą w każdym momencie ustalić który jest pierwszy, a kto drugi.

Przy oddaleniu się wątki wybierają propozycję przodującego.

#### Zwracana wartość jest jedną z ustalonych

Jeżeli jeden z wątków będzie dużo szybszy i wygra zanim drugi w ogóle zacznie się ścigać to i tak zwróci swoją wartość, którą musiał przypisać zanim wszedł do wyścigu.

#### Zwracana wartość jest taka sama

Jedyna zmieniająca się wartość to `position`.

Zmienia się ona tylko w `position[i] = position[i] + speed[i];`

Rozważmy przypadki:
- Oba wątki sprawdzają ify: `position` jest atomowe, więc zwrócą to samo
- Jeden wątek sprawdził ifa i wyszedł, a drugi zmienia `position`:
    - `position[i] > position[j] + speed[j]`: po dodaniu `speed` dalej jest spełnione
    - `position[i] < position[j]`: po dodaniu `speed` dalej jest spełnione

Czyli zawsze wątki wyjdą przeciwymi ifami, zwracając tą samą wartość.

#### Dlaczego nie ma sprzeczności ?

Ten algorytm nie jest *wait-free* (wątki mogą w nieskończoność utrzymywać niewielką odległość od siebie, "bieg łeb w łeb").

Więc nie spełnia warunków potrzebnych do złamania poziomu konsensusu.

#### Niehamowanie

Algorytm jest niehamujący, jeżeli wstrzymanie lub awaria jednego z wątków nie uniemożliwia pozostałym wątkom dokonania postępu.

Jeśli jeden z wątków (np. wątek j) zostanie wstrzymany w dowolnym momencie, drugi wątek (i) będzie kontynuował wykonywanie swojej pętli while. W każdej iteracji wartość `position[i]` rośnie, podczas gdy `position[j]` pozostaje stała. W rezultacie, po skończonej liczbie kroków, warunek `position[i] > position[j] + speed[j]` zostanie spełniony, co pozwoli wątkowi zakończyć działanie i podjąć decyzję.​
