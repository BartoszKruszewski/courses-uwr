// Bartosz Kruszewski
// PO lista 5 zadanie 1 Listy
// 25.03.2023 Wersja 1.
// Klasa OrderedList oraz interfejs ListItem

package zadanie1;

public class OrderedList<T extends ListItem<T> & Comparable<T>> {
    //pierwszy element listy
    private T head;
    public OrderedList() {
        //początkowo nie ma pierwszego elementu listy
        this.head = null;
    }
    public void add(T newElement) {

        //sprawdzanie, czy należy dodać element jako pierwszy
        if (head == null) {
            head = newElement;
        } else {
            //sprawdzanie, czy element nie jest mniejszy od pierwszego
            if (head.compareTo(newElement) > 0) {
                newElement.setNext(head);
                head = newElement;
            } else {
                //przeszukiwanie listy aż natrafi się na większy element
                T actualElement = head;
                while (actualElement.getNext() != null &&
                        actualElement.getNext().compareTo(newElement) < 0)
                    actualElement = actualElement.getNext();
                newElement.setNext(actualElement.getNext());
                actualElement.setNext(newElement);
            }
        }
    }

    public String toString() {
        String result = "";
        T actualElement = head;
        //utworzenie napisu z każdego elementu listy i złączenie ich
        while (actualElement.getNext() != null) {
            result += actualElement.toString() + " ";
            actualElement = actualElement.getNext();
        }
        //ostatni element jest dodawany bez spacji
        result += actualElement.toString() + " ";
        return result;
    }
    public T getFirst() {
        //zwracanie pierwszego elementu
        return head;
    }
}

//interfejs pozwalający na używanie obiektów klasy implementującej
//go jako elementów listy
interface ListItem<T> {
    //metoda zwracająca kolejny element danego elementu listy
    T getNext();

    //metoda zwracająca ustawiająca element danego elementu listy
    void setNext(T element);

    //metoda zwracająca napis z informacją o elemencie listy
    String toString();
}