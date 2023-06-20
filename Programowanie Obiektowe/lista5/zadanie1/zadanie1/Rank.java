// Bartosz Kruszewski
// PO lista 5 zadanie 1 Listy
// 25.03.2023 Wersja 1.
// Klasa Rank, której obiekty mogą być
// elementami list OrderedList

package zadanie1;

//klasa implementuje interfejsy Comparable oraz ListItem,
//żeby można było używać jej obiektów jako elementów listy
public class Rank implements Comparable<Rank>, ListItem<Rank> {
    //nazwa stopnia wojskowego
    public String name;
    //następny element na liście
    public Rank next;

    public Rank(String name) throws Exception {

        //sprawdzanie, czy podana nazwa stopnia wojskowego jest poprawna
        String[] names = new String[]{
                "private", "corporal", "sergeant", "capitan",
                "major", "colonel", "general", "marshal"};

        boolean isNameCorrect = false;

        for (String n : names) {
            if (name.equals(n)) {
                isNameCorrect = true;
                break;
            }
        }

        if (isNameCorrect) {
            this.name = name;
        } else {
            throw new Exception("Błędna nazwa rangi!");
        }
    }

    @Override
    public int compareTo(Rank other) {

        //sprawdzanie, która nazwa stopnia wojskowego jest wyżej w hierarchii
        String[] hierarchy = new String[]{
                "private", "corporal", "sergeant", "capitan",
                "major", "colonel", "general", "marshal"};

        int thisIndex = 0;
        while (!hierarchy[thisIndex].equals(this.name)) {

            thisIndex++;
        }
        int otherIndex = 0;
        while (!hierarchy[otherIndex].equals(other.name)) {
            otherIndex++;
        }

        return Integer.compare(thisIndex, otherIndex);
    }

    @Override
    public Rank getNext() {
        //zwracanie następnego elementu
        return next;
    }

    @Override
    public void setNext(Rank element) {
        //ustawianie następnego elementu
        next = element;
    }

    public String toString() {
        //zwracanie nazwy stopnia wojskowego
        return name;
    }
}

