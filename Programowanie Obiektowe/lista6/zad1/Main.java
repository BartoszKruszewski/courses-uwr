// Bartosz Kruszewski
// PO lista 6 zadanie 1
// Zapisywanie i wczytywanie kolekcji do pliku
// 31.03.2023 Wersja 1.

// javac Main.java <- kompilacja
// java Main <- uruchomienie programu

// Plik List.java musi znajdować się w folderze zadanie1,
// który musi znajdować się w folderze z plikiem Main.java

// Proszę zignorować ostrzeżenie wyświetlane po kompilacji - "uses unchecked
// or unsafe operations", dotyczy ono linii kodu "l3 = (List<Integer>)
// in.readObject();", gdzie dokonujemy zamiany typu wczytywanego obiektu,
// nie sprawdzając wcześniej, jakiego jest typu, jednak na potrzeby testu
// wiemy, że zapisany przez nas obiekt jest właściwego typu

import zadanie1.List;

import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        // test klasy List
        List<Integer> l1 = new List<>();
        l1.add(1);
        l1.add(2);
        l1.add(3);
        l1.add(4);

        System.out.print("Wartości l1: ");
        for (int i = 0; i < 4; i++) {
            System.out.print(l1.pop() + " ");
        }
        System.out.println();

        // utworzenie obiektu klasy List, za pomocą którego będziemy testować
        // zapisywanie i wczytywanie obiektów tej klasy do pliku
        List<Integer> l2 = new List<>();
        l2.add(1);
        l2.add(2);
        l2.add(3);
        l2.add(4);

        // zapis l2 do pliku

        // utworzenie obiektów strumieni potrzebnych do zapisu do pliku
        FileOutputStream fileOut = new FileOutputStream("list.ser");
        ObjectOutputStream out = new ObjectOutputStream(fileOut);
        // zapisanie obiektu do pliku
        out.writeObject(l2);
        // zamknięcie strumieni
        out.close();
        fileOut.close();


        // wczytywanie l2 z pliku do obiektu l3

        // zadeklarowanie obiektu l3, do którego będziemy wczytywać obiekt l2,
        // zapisany w pliku
        List<Integer> l3;
        // utworzenie obiektów strumieni potrzebnych do zapisu do pliku
        FileInputStream fileIn = new FileInputStream("list.ser");
        ObjectInputStream in = new ObjectInputStream(fileIn);
        // wczytanie obiektu z pliku do obiektu l3
        l3 = (List<Integer>) in.readObject();
        // zamknięcie strumieni
        in.close();
        fileIn.close();

        // wypisanie zawartości wczytanej listy
        System.out.print("Wartości l3 wczytane z pliku: ");
        for (int i = 0; i < 4; i++) {
            System.out.print(l3.pop() + " ");
        }
        System.out.println();


    }
}