// Bartosz Kruszewski
// PO lista 5 zadanie 2 Listy
// 26.03.2023 Wersja 1.
// Program prezentujący klasę Expression

// javac Main.java <- kompilacja
// java Main <- uruchomienie programu

// Pliki Expression.java, Const.java, Variable.java, Sum.java
// i Product.java muszą znajdować się w folderze zadanie2,
// który musi znajdować się w folderze z plikiem Main.java


import zadanie2.Expression;
import zadanie2.Const;
import zadanie2.Variable;
import zadanie2.Sum;
import zadanie2.Product;

public class Main {
    public static void main(String[] args) throws Exception {
        //testy
        Expression simpleSum = new Sum(new Const(4), new Variable("x"));
        printExpression(simpleSum);
        Expression simpleProduct = new Product(new Variable("zmienna"), new Const(7));
        printExpression(simpleProduct);
        Variable v = new Variable("nowa_zmienna");
        v.setValue(15);
        simpleProduct.setRight(v);
        Expression exp1 = new Sum(simpleProduct, simpleSum);
        printExpression(exp1);
        Expression exp2 = new Product(new Const(8), exp1);
        printExpression(exp2);

    }

    public static void printExpression(Expression exp) {
        //funkcja wypisująca zapis wyrażenia nawiasami oraz jego wartość
        System.out.println("Wyrażenie: " + exp + " Wartość: " + exp.evaluate());
    }
}