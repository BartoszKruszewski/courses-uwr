// Bartosz Kruszewski
// PO lista 5 zadanie 1 Listy
// 25.03.2023 Wersja 1.
// Klasa Alcohol, której obiekty mogą być
// elementami list OrderedList

package zadanie1;

//klasa implementuje interfejsy Comparable oraz ListItem,
//żeby można było używać jej obiektów jako elementów listy
public class Alcohol implements Comparable<Alcohol>, ListItem<Alcohol> {
    //nazwa alkoholu
    public String name;
    //następny element na liście
    public Alcohol next;

    public Alcohol(String name) throws Exception {

        //sprawdzanie, czy podana nazwa alkoholu jest poprawna
        String[] names = new String[]{
                "beer","wine","vodka","hooch","spirit"};

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
            throw new Exception("Błędna nazwa alkoholu!");
        }
    }

    @Override
    public int compareTo(Alcohol other) {

        //sprawdzanie, która nazwa alkoholu jest wyżej w hierarchii
        //(napoje alkoholowe porównywane są pod względem zawartości alkoholu)
        String[] hierarchy = new String[]{
                "beer","wine","vodka","hooch","spirit"};

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
    public Alcohol getNext() {
        //zwracanie następnego elementu
        return next;
    }

    @Override
    public void setNext(Alcohol element) {
        //ustawianie następnego elementu
        next = element;
    }

    public String toString() {
        //zwracanie nazwy alkoholu
        return name;
    }
}

