// Bartosz Kruszewski
// PO lista 7 zadanie 1
// Implementacja edytora obiektów
// 14.04.2023 Wersja 1.
// Klasa Circle, będąca podklasą Figure

package zadanie1;

public class Circle extends Figure {

    // promień koła
    private double r;

    public Circle(double x, double y, double r) throws Exception {
        setX(x);
        setY(y);
        setR(r);
    }

    @Override
    public String toString() {
        return "Okrąg, współrzędne: (" + getX() + ", " + getY() +
                ") Długość promienia: " + getR();
    }

    public double getR() {
        return r;
    }

    public void setR(double value) throws Exception {
        if (value <= 0) {
            throw new Exception("Długość promienia musi być dodatnia!");
        }
        r = value;
    }

}
