// Bartosz Kruszewski
// PO lista 6 zadanie 2
// Interfejs Collection
// 31.03.2023 Wersja 1.
// Klasa List i ListItem

package zadanie2;

import java.util.Collection;
import java.util.Iterator;
import java.util.NoSuchElementException;

public class List<T> implements Collection<T> {
    // pierwszy element listy
    private ListItem<T> head;

    public List() {
        // początkowo nie ma pierwszego elementu listy
        this.head = null;
    }

    @Override
    public int size() {
        // zliczanie elementów
        int s = 0;
        for (T ignored : this) {
            s++;
        }
        return s;
    }

    @Override
    public boolean isEmpty() {
        // jeżeli nie ma pierwszego elementu lista jest pusta
        return head == null;
    }

    @Override
    public boolean contains(Object o) {
        // sprawdzanie po kolei czy, któryś element jest równy o
        for (T element : this) {
            if (element.equals(o)) {
                return true;
            }
        }
        return false;
    }

    @Override
    public Iterator<T> iterator() {
        return new ListIterator();
    }

    // klasa iterator
    private class ListIterator implements Iterator<T> {
        private ListItem<T> actualItem = head;

        @Override
        public boolean hasNext() {
            return actualItem != null;
        }

        @Override
        public T next() {
            if (!hasNext()) {
                throw new NoSuchElementException();
            }
            T value = actualItem.getValue();
            actualItem = actualItem.getNext();
            return value;
        }
    }

    @Override
    public Object[] toArray() {
        // utworzenie tablicy o długości odpowiadającej długości listy
        Object[] array = new Object[size()];

        // przepisanie wszystkich elementów z listy do tablicy
        int i = 0;
        for (T element : this) {
            array[i++] = element;
        }
        return array;
    }

    @Override
    public <T1> T1[] toArray(T1[] a) {

        // utworzenie tablicy
        T1[] result;

        // jeżeli tablica jest mniejsza od listy, tworzymy tablice długości
        // listy, w przeciwnym przypadku kopiujemy tablice
        if (a.length < this.size()) {
            result = (T1[]) java.lang.reflect.Array.newInstance
                    (a.getClass().getComponentType(), this.size());
        } else {
            result = a.clone();
        }

        // przepisywanie elementów z listy do tablicy
        int i = 0;
        for (T element : this) {
            result[i++] = (T1) element;
        }
        return result;
    }

    @Override
    public boolean add(T t) {
        // tworzenie obiektu nowego elementu listy
        ListItem<T> newItem = new ListItem<>(t);

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
        return true;
    }


    @Override
    public boolean remove(Object o) {

        // sprawdzanie, czy lista zawiera element, który chcemy usunąć
        if (this.contains(o)) {
            // sprawdzanie, czy ma tylko pierwszy element
            if (head.getNext() == null) {
                head = null;
            } else {
                // przejście po liście i porównywanie elementów z elementem,
                // który chcemy usunąć i przypisanego elementowi przed nim
                // następnika będącego następnikiem elementu, który usuwamy
                ListItem<T> actualItem = head;
                while (!actualItem.getNext().getValue().equals(o)) {
                    actualItem = actualItem.getNext();
                }
                actualItem.setNext(actualItem.getNext().getNext());
            }
            return true;
        }
        return false;
    }

    @Override
    public boolean containsAll(Collection<?> c) {
        // sprawdzanie każdego elementu kolekcji c, czy znajduje się na liście
        for (Object o : c) {
            if (!contains(o)) {
                return false;
            }
        }
        return true;
    }

    @Override
    public boolean addAll(Collection<? extends T> c) {
        // dodawanie każdego elementu kolekcji c do listy
        boolean isModified = false;
        for (T element : c) {
            if (add(element)) {
                isModified = true;
            }
        }
        return isModified;
    }

    @Override
    public boolean removeAll(Collection<?> c) {
        // usuwanie każdego elementu kolekcji c z listy
        boolean isModified = false;
        for (Object element : c) {
            if (remove(element)) {
                isModified = true;
            }
        }
        return isModified;
    }

    @Override
    public boolean retainAll(Collection<?> c) {
        // usuwanie elementów z listy, jeżeli są w kolekcji
        boolean isModified = false;
        for (Object element : this) {
            if (!c.contains(element)) {
                if (remove(element)) {
                    isModified = true;
                }
            }
        }
        return isModified;
    }

    @Override
    public void clear() {
        // usuwanie pierwszego elementu, bez przypisywania następnika
        head = null;
    }
}

class ListItem<T> {

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

