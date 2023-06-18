// Bartosz Kruszewski
// PO lista 7 zadanie 1
// Implementacja edytora obiektów
// 14.04.2023 Wersja 1.
// Klasa CircleSwing, posiadająca polecenia
// dla Swinga związane z edycją klasy Circle

package zadanie1;

import javax.swing.*;

public class CircleSwing extends JComponent {

    // pola do wpisywania wartości
    private final JTextField xField;
    private final JTextField yField;
    private final JSpinner rSpinner;

    public CircleSwing(Circle circle) {
        // ustawiane rozłożenia kontrolek
        setLayout(new BoxLayout(this, BoxLayout.PAGE_AXIS));
        // utworzenie obiektów pól do wpisywania
        xField = new JTextField(String.valueOf(circle.getX()));
        yField = new JTextField(String.valueOf(circle.getY()));
        rSpinner = new JSpinner(new SpinnerNumberModel(circle.getR(), 1, 9999, 1));

        // dodanie pól z opisami
        add(new JLabel("X:"));
        add(xField);
        add(new JLabel("Y:"));
        add(yField);
        add(new JLabel("R:"));
        add(rSpinner);
    }

    public Circle getCircle() throws Exception {
        // "wyciąganie" z kontrolek danych wpisanych przez użytkownika
        double x = Double.parseDouble(xField.getText());
        double y = Double.parseDouble(yField.getText());
        double r = (double) rSpinner.getValue();
        return new Circle(x, y, r);
    }
}