// Bartosz Kruszewski
// PO lista 5 zadanie 2 Listy
// 26.03.2023 Wersja 1.
// Klasa Variable, która dziedziczy z Expression,
// jest to implementacja zmiennej

package zadanie2;

public class Variable extends Expression {
    //nazwa zmiennej
    private final String name;

    //wartość zmiennej
    private int value;

    public Variable(String name) {
        //wyrażenie musi być "liściem"
        isLeaf = true;
        this.name = name;

        //domyślna wartość zmiennej to 0
        value = 0;
    }

    @Override
    public int evaluate() {
        return value;
    }

    @Override
    public String toString() {
        //nawiasy klamrowe są dodane dodatkowo,
        //żeby było widać jaką wartość aktualnie przyjmuje zmienna
        return name + "{" + value + "}";
    }

    public void setValue(int value) {
        this.value = value;
    }

}
