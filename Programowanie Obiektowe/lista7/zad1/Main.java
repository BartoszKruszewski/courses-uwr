// Bartosz Kruszewski
// PO lista 7 zadanie 1
// Implementacja edytora obiektów
// 14.04.2023 Wersja 1.

// javac Main.java <- kompilacja
// java Main <nazwa_pliku> <nazwa_klasy> <- uruchomienie programu

// Przykładowe polecenia uruchomienia:
// java Main test1 Circle
// java Main test2 Rectangle

// Pliki Figure.java, Rectangle.java, Circle.java, CircleSwing.java,
// RectangleSwing.java muszą znajdować się w folderze zadanie2,
// który musi znajdować się w folderze z plikiem Main.java



import zadanie1.*;
import javax.swing.*;
import java.io.*;

public class Main {
    public static void main(String[] args) {
        // sprawdzanie, czy zostały podane prawidłowe argumenty wywołania
        if (args.length != 2) {
            System.out.println("Prawidłowy sposób użycia: " +
                    "java Main <nazwa_pliku> <nazwa_klasy>");
            System.exit(1);
        }

        // przepisanie nazwy pliku oraz nazwy klasy do osobnych zmiennych
        String filename = args[0];
        String classname = args[1];

        try {
            // utworzenie obiektu, który będziemy edytować
            Object obj = null;
            // utworzenie obiektu obsługi pliku
            File file = new File(filename);

            // jeżeli plik o podanej przez użytkownika nazwie istnieje
            // to wczytujemy z niego dane do obiektu obj
            if (file.exists()) {
                FileInputStream fis = new FileInputStream(file);
                ObjectInputStream ois = new ObjectInputStream(fis);
                obj = ois.readObject();
                ois.close();
            } else {

                // w przeciwnym przypadku tworzymy obiekt takiego typu,
                // jakiego została podana przez użytkownika nazwa
                if (classname.equals("Circle")){
                    obj = new Circle(0,0,1);
                }
                else if (classname.equals("Rectangle")){
                    obj = new Rectangle(0,0,1,1);
                }
                
            }

            // w zależności od typu obiektu wywołujemy odpowiednie okienko
            // do edycji
            if (obj instanceof Rectangle) {
                // utworzenie obiektu z poleceniami dla swinga
                RectangleSwing swing = new RectangleSwing((Rectangle) obj);
                // wywołanie okienka swinga
                int result = JOptionPane.showConfirmDialog(null, swing, "Edycja prostokąta", JOptionPane.OK_CANCEL_OPTION);
                // jeżeli okienko zostanie zamknięte przy użyciu przycisku OK
                // to zapisujemy dane
                if (result == JOptionPane.OK_OPTION) {
                    Rectangle rectangle = swing.getRectangle();
                    FileOutputStream fos = new FileOutputStream(file);
                    ObjectOutputStream oos = new ObjectOutputStream(fos);
                    oos.writeObject(rectangle);
                    oos.close();
                    System.out.println("Prawidłowo zapisano obiekt: " + rectangle.toString());
                }
            } else if (obj instanceof Circle) {
                // analogicznie jak dla obiektów klasy Rectangle
                CircleSwing swing = new CircleSwing((Circle) obj);
                int result = JOptionPane.showConfirmDialog(null, swing, "Edycja okręgu", JOptionPane.OK_CANCEL_OPTION);
                if (result == JOptionPane.OK_OPTION) {
                    Circle circle = swing.getCircle();
                    FileOutputStream fos = new FileOutputStream(file);
                    ObjectOutputStream oos = new ObjectOutputStream(fos);
                    oos.writeObject(circle);
                    oos.close();
                    System.out.println("Prawidłowo zapisano obiekt: " + circle.toString());
                }
            } else {
                // Jeżeli podano błędną nazwę klasy to informujemy
                // o tym użytkownika
                System.out.println("Nie znaleziono klasy: " + classname);
                System.exit(1);
            }
        } catch (Exception e) {
            // wyłapywanie pozostałych wyjątków
            e.printStackTrace();
            System.exit(1);
        }
    }
}
