// Bartosz Kruszewski
// PO lista 7 zadanie 1
// Implementacja edytora obiektów
// 14.04.2023 Wersja 1.
// Abstrakcyjna klasa Figure

package zadanie1;

import java.io.Serializable;

public abstract class Figure implements Serializable {

    // współrzędne figury
    private double x, y;

    abstract public String toString();

    public void setX(double value) {
        x = value;
    }

    public double getX() {
        return x;
    }

    public void setY(double value) {
        y = value;
    }

    public double getY() {
        return y;
    }


}
