// Bartosz Kruszewski
// PO lista 7 zadanie 1
// Implementacja edytora obiektów
// 14.04.2023 Wersja 1.
// Klasa Rectangle, będąca podklasą Figure

package zadanie1;

public class Rectangle extends Figure {

    //długości boków prostokąta

    private double a, b;

    public Rectangle(double x, double y, double a, double b) throws Exception {
        setX(x);
        setY(y);
        setA(a);
        setB(b);
    }

    @Override
    public String toString() {
        return "Prostokąt, współrzędne: (" + getX() + ", " + getY() +
                ") Długości boków: " + getA() + " i " + getB();
    }

    public double getA() {

        return a;
    }

    public void setA(double value) throws Exception {
        if (value <= 0) {
            throw new Exception("Długość boku musi być dodatnia!");
        }
        a = value;
    }

    public double getB() {
        return b;
    }

    public void setB(double value) throws Exception {
        if (value <= 0) {
            throw new Exception("Długość boku musi być dodatnia!");
        }
        b = value;
    }
}
