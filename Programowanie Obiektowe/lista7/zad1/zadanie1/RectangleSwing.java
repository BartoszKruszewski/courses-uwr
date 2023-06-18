// Bartosz Kruszewski
// PO lista 7 zadanie 1
// Implementacja edytora obiektów
// 14.04.2023 Wersja 1.
// Klasa RectangleSwing, posiadająca polecenia
// dla Swinga związane z edycją klasy Rectangle

package zadanie1;

import javax.swing.*;

public class RectangleSwing extends JComponent {

    // pola do wpisywania wartości
    private final JTextField xField;
    private final JTextField yField;
    private final JSpinner aSpinner;
    private final JSpinner bSpinner;

    public RectangleSwing(Rectangle rectangle) {
        // ustawiane rozłożenia kontrolek
        setLayout(new BoxLayout(this, BoxLayout.PAGE_AXIS));
        // utworzenie obiektów pól do wpisywania
        xField = new JTextField(String.valueOf(rectangle.getX()));
        yField = new JTextField(String.valueOf(rectangle.getY()));
        aSpinner = new JSpinner(new SpinnerNumberModel(rectangle.getA(), 1, 9999, 1));
        bSpinner = new JSpinner(new SpinnerNumberModel(rectangle.getB(), 1, 9999, 1));

        // dodanie pól z opisami
        add(new JLabel("X:"));
        add(xField);
        add(new JLabel("Y:"));
        add(yField);
        add(new JLabel("A:"));
        add(aSpinner);
        add(new JLabel("B:"));
        add(bSpinner);
    }

    public Rectangle getRectangle() throws Exception {
        // "wyciąganie" z kontrolek danych wpisanych przez użytkownika
        double x = Double.parseDouble(xField.getText());
        double y = Double.parseDouble(yField.getText());
        double a = (double) aSpinner.getValue();
        double b = (double) bSpinner.getValue();
        return new Rectangle(x, y, a, b);
    }
}