// Bartosz Kruszewski
// PO lista 5 zadanie 1 Listy
// 25.03.2023 Wersja 1.
// Klasa Card, której obiekty mogą być
// elementami list OrderedList

package zadanie1;

//klasa implementuje interfejsy Comparable oraz ListItem,
//żeby można było używać jej obiektów jako elementów listy
public class Card implements Comparable<Card>, ListItem<Card> {
    //nazwa karty
    public String name;
    //następny element na liście
    public Card next;

    public Card(String name) throws Exception {

        //sprawdzanie, czy podana nazwa karty jest poprawna
        String[] names = new String[]{
                "2", "3", "4", "5", "6", "7", "8", "9", "10",
                "jack", "queen", "king", "ace"};

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
            throw new Exception("Błędna nazwa karty!");
        }
    }

    @Override
    public int compareTo(Card other) {

        //sprawdzanie, która nazwa karty jest wyżej w hierarchii
        String[] hierarchy = new String[]{
                "2", "3", "4", "5", "6", "7", "8", "9", "10",
                "jack", "queen", "king", "ace"};

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
    public Card getNext() {
        //zwracanie następnego elementu
        return next;
    }

    @Override
    public void setNext(Card element) {
        //ustawianie następnego elementu
        next = element;
    }

    public String toString() {
        //zwracanie nazwy karty
        return name;
    }
}
