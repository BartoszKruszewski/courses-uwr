// Bartosz Kruszewski
// PO lista 5 zadanie 2 Listy
// 26.03.2023 Wersja 1.
// Klasa Product, która dziedziczy z Expression
// jest to implementacja iloczynu

package zadanie2;

public class Product extends Expression {
    public Product(Expression left, Expression right) throws Exception {
        //wyrażenie nigdy nie jest "liściem"
        isLeaf = false;
        setLeft(left);
        setRight(right);
    }

    @Override
    public int evaluate() {
        return left.evaluate() * right.evaluate();
    }

    @Override
    public String toString() {
        //dodanie nawiasów, żeby zachować konwencję stosowaną w matematyce,
        //ponieważ drzewo zachowuje kolejność działań
        return "(" + left.toString() + " * " + right.toString() + ")";
    }
}
