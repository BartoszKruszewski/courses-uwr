// Bartosz Kruszewski
// PO lista 6 zadanie 2
// Implementacja interfejsu Collection
// 31.03.2023 Wersja 1.

// javac Main.java <- kompilacja
// java Main <- uruchomienie programu

// Plik List.java musi znajdować się w folderze zadanie2,
// który musi znajdować się w folderze z plikiem Main.java


import zadanie2.List;

public class Main {
    public static void main(String[] args) {

        // utworzenie obiektu klasy List
        List<Integer> l1 = new List<>();

        // dodawanie elementów do listy l1
        l1.add(1);
        l1.add(2);
        l1.add(3);
        l1.add(4);

        // wypisywanie elementów l1 przy użyciu for
        showList(l1 ,"Wypisanie l1 przy użyciu for po elementach: ");

        // długość listy l1
        System.out.println("Długość listy: " + l1.size());

        // czy lista l1 jest pusta
        System.out.println("Czy pusta?: " + l1.isEmpty());

        // czy lista l1 zawiera 3
        System.out.println("Czy zawiera element 3: " + l1.contains(3));

        // wypisywanie elementów tablicy utworzonej na podstawie listy l1
        System.out.print("Wypisanie tablicy l.toArray(): ");
        for (Object a : l1.toArray()) {
            System.out.print(a + " ");
        }
        System.out.println();

        // wypisywanie elementów tablicy utworzonej na podstawie listy l1
        // i większej tablicy
        System.out.print("Wypisanie tablicy l.toArray(new Integer[] {4, 5, 2, 1, 8, 7}): ");
        for (Object a : l1.toArray(new Integer[] {4, 5, 2, 1, 8, 7})) {
            System.out.print(a + " ");
        }
        System.out.println();

        // wypisywanie elementów tablicy utworzonej na podstawie listy l1
        // i mniejszej tablicy
        System.out.print("Wypisanie tablicy l.toArray(new Integer[] {7, 5, 12}): ");
        for (Object a : l1.toArray(new Integer[] {7, 5, 12})) {
            System.out.print(a + " ");
        }
        System.out.println();

        // usuwanie z listy l1
        l1.remove(3);
        showList(l1, "l.remove(3): ");

        // utworzenie innego obiektu klasy List
        List<Integer> l2 = new List<>();

        // dodawanie elementów do listy l2
        l2.add(91);
        l2.add(29);
        l2.add(1);
        l2.add(16);
        showList(l2, "Wypisanie l2 przy użyciu for po elementach: ");

        // czy lista l1 zawiera listę l2
        System.out.println("Czy l1 zawiera l2?: " + l1.containsAll(l2));

        // czy lista l1 listę zawiera l1
        System.out.println("Czy l1 zawiera l1?: " + l1.containsAll(l1));

        // dodanie elementów listy l2 do listy l1
        l1.addAll(l2);
        showList(l1, "l1.addAll(l2): ");

        // usunięcie elementów listy l2 z listy l1
        l1.removeAll(l2);
        showList(l1, "l1.removeAll(l2): ");

        // usunięcie elementów z listy l1, których nie ma w liście l2
        l1.retainAll(l2);
        showList(l1, "l1.retainAll(l2): ");

        // czyszczenie listy l1
        l1.clear();
        showList(l1, "l1.clear(): ");
    }

    public static void showList(List<?> l, String message) {
        // wypisywanie elementów listy przy użyciu for
        System.out.print(message);
        for (var a : l) {
            System.out.print(a + " ");
        }
        System.out.println();
    }
}