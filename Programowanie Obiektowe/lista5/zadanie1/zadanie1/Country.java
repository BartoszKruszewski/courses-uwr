// Bartosz Kruszewski
// PO lista 5 zadanie 1 Listy
// 25.03.2023 Wersja 1.
// Klasa Country, której obiekty mogą być
// elementami list OrderedList

package zadanie1;

//klasa implementuje interfejsy Comparable oraz ListItem,
//żeby można było używać jej obiektów jako elementów listy
public class Country implements Comparable<Country>, ListItem<Country> {
    //nazwa państwa
    public String name;
    //następny element na liście
    public Country next;

    public Country(String name) throws Exception {

        //sprawdzanie, czy podana nazwa państwa jest poprawna
        String[] names = new String[]{
                "Island", "Poland", "France", "Egypt", "Mexico",
                "Canada", "USA", "Russia"};

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
            throw new Exception("Błędna nazwa państwa!");
        }
    }

    @Override
    public int compareTo(Country other) {

        //sprawdzanie, które państwo jest wyżej w hierarchii
        //(państwa porównywane są pod względem powierzchni)
        //Wartości podane są w km2 (dane pochodzą z google):
        //Islandia 103 000
        //Polska 322 575
        //Francja 551 695
        //Egipt 1 001 450
        //Meksyk 1 973 000
        //Kanada 9 985 000
        //USA 9 834 000
        //Rosja 17 100 000

        String[] hierarchy = new String[]{
                "Island", "Poland", "France", "Egypt", "Mexico",
                "Canada", "USA", "Russia"};

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
    public Country getNext() {
        //zwracanie następnego elementu
        return next;
    }

    @Override
    public void setNext(Country element) {
        //ustawianie następnego elementu
        next = element;
    }

    public String toString() {
        //zwracanie nazwy państwa
        return name;
    }
}

