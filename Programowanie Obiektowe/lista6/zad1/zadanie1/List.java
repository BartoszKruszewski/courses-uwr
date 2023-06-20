// Bartosz Kruszewski
// PO lista 6 zadanie 1
// Zapisywanie i wczytywanie kolekcji do pliku
// 31.03.2023 Wersja 1.
// Klasa List i ListItem

package zadanie1;

import java.io.Serializable;

public class List<T> implements Serializable {
    // pierwszy element listy
    private ListItem<T> head;

    public List() {
        // początkowo nie ma pierwszego elementu listy
        this.head = null;
    }

    public void add(T value) {

        // tworzenie obiektu nowego elementu listy
        ListItem<T> newItem = new ListItem<>(value);

        // sprawdzanie, czy należy dodać element jako pierwszy
        if (head == null) {
            head = newItem;
        } else {
            // przejście po liście do ostatniego elementu i przypisanego nowego
            // elementu jako jego następnik
            ListItem<T> actualItem = head;
            while (actualItem.getNext() != null) {
                actualItem = actualItem.getNext();
            }
            actualItem.setNext(newItem);
        }
    }

    public T pop() throws Exception {
        T valueToReturn;
        // sprawdzanie, czy lista nie jest pusta
        if (head == null) {
            throw new Exception("Lista jest pusta. Nie można usunąć jej ostatniego elementu!");
        } else {
            // sprawdzanie, czy lista ma jeden element, jeżeli tak to usuwamy
            // przypisanie przodu listy do elementu
            if (head.getNext() == null) {
                valueToReturn = head.getValue();
                head = null;
            } else {
                // przejście po liście do przedostatniego elementu i usunięcie
                // przypisania do jego następnika
                ListItem<T> actualItem = head;
                while (actualItem.getNext().getNext() != null) {
                    actualItem = actualItem.getNext();
                }
                valueToReturn = actualItem.getNext().getValue();
                actualItem.setNext(null);
            }
            return valueToReturn;
        }
    }
}

class ListItem<T> implements Serializable {

    // następny element
    ListItem<T> next;

    // wartość elementu
    T value;

    public ListItem(T value) {
        // przypisanie wartości
        this.value = value;
        // początkowo nie ma następnego elementu
        this.next = null;
    }

    // metoda ustawiająca następny element danego elementu listy
    public void setNext(ListItem<T> element) {
        this.next = element;
    }

    // metoda zwracająca następny element danego elementu listy
    public ListItem<T> getNext() {
        return this.next;
    }

    // metoda zwracająca wartość elementu listy
    public T getValue() {
        return this.value;
    }
}