// Bartosz Kruszewski
// PO lista 5 zadanie 2 Listy
// 26.03.2023 Wersja 1.
// Klasa Expression

package zadanie2;

public abstract class Expression {
    //lewy potomek
    protected Expression left = null;

    //prawy potomek
    protected Expression right = null;

    //czy wyrażenie jest "liściem" drzewa
    protected boolean isLeaf;

    //zwracanie wartości całego drzewa
    public abstract int evaluate();

    //zwracanie napisu przedstawiającego wyrażenie zapisane w drzewie
    public abstract String toString();

    //ustawianie lewego elementu
    public void setLeft(Expression expression) throws Exception {
        if (isLeaf) {
            throw new Exception("Wyrażenia będące liśćmi nie mają potomków!");
        } else {
            left = expression;
        }
    }

    //ustawianie prawego elementu
    public void setRight(Expression expression) throws Exception {
        if (isLeaf) {
            throw new Exception("Wyrażenia będące liśćmi nie mają potomków!");
        } else {
            right = expression;
        }
    }
}
