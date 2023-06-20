// Bartosz Kruszewski
// PO lista 5 zadanie 2 Listy
// 26.03.2023 Wersja 1.
// Klasa Const, która dziedziczy z Expression,
// jest to implementacja stałej

package zadanie2;

public class Const extends Expression {

    //stała wartość wyrażenia
    private final int value;

    public Const(int value) {
        //wyrażenie musi być "liściem"
        isLeaf = true;
        this.value = value;
    }

    @Override
    public int evaluate() {
        return value;
    }

    @Override
    public String toString() {
        return Integer.toString(value);
    }
}
