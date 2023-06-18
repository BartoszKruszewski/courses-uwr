#include <iostream>
#include "Expression.h"
#include "OperatorSingleArg.h"
#include "OperatorDualArg.h"

int main() {
    Var::addValuation("x", 1);
    Var::addValuation("y", 1);

    Number* number = new Number(2);
    Pi* pi = new Pi();
    E* e = new E();
    Fi* fi = new Fi();
    Sin* sin = new Sin(number);
    Cos* cos = new Cos(number);
    Ln* ln = new Ln(number);
    Exp* exp = new Exp(number);
    Abs* abs = new Abs(number);
    Opp* opp = new Opp(number);
    Inv* inv = new Inv(number);
    Sum* sum = new Sum(number, number);
    Diff* diff = new Diff(number, number);
    Prod* prod = new Prod(number, number);
    Div* div = new Div(number, number);
    Log* log = new Log(number, number);
    Mod* mod = new Mod(number, number);
    Pow* pow = new Pow(number, number);
    std::cout << number->toString() << " : " << number->eval() << std::endl;
    std::cout << pi->toString() << " : " << pi->eval() << std::endl;
    std::cout << e->toString() << " : " << e->eval() << std::endl;
    std::cout << fi->toString() << " : " << fi->eval() << std::endl;
    std::cout << sin->toString() << " : " << sin->eval() << std::endl;
    std::cout << cos->toString() << " : " << cos->eval() << std::endl;
    std::cout << ln->toString() << " : " << ln->eval() << std::endl;
    std::cout << exp->toString() << " : " << exp->eval() << std::endl;
    std::cout << abs->toString() << " : " << abs->eval() << std::endl;
    std::cout << opp->toString() << " : " << opp->eval() << std::endl;
    std::cout << inv->toString() << " : " << inv->eval() << std::endl;
    std::cout << sum->toString() << " : " << sum->eval() << std::endl;
    std::cout << diff->toString() << " : " << diff->eval() << std::endl;
    std::cout << prod->toString() << " : " << prod->eval() << std::endl;
    std::cout << div->toString() << " : " << div->eval() << std::endl;
    std::cout << log->toString() << " : " << log->eval() << std::endl;
    std::cout << mod->toString() << " : " << mod->eval() << std::endl;
    std::cout << pow->toString() << " : " << pow->eval() << std::endl;

    std::cout << std::endl;

    //((x-1)*x)/2
    Expression* a = new Div(new Prod(new Diff(new Var("x"), new Number(1)), new Var("x")), new Number(2));
    std::cout << a->toString() << std::endl;

    //(3+5)/(2+x*7)
    Expression* b = new Div(new Sum(new Number(3), new Number(5)),
                            new Sum(new Number(2), new Prod(new Var("x"), new Number(7))));
    std::cout << b->toString() << std::endl;

    //2+x*7-(y*3+5)
    Expression* c = new Diff(new Sum(new Number(2), new Prod(new Var("x"), new Number(7))),
                             new Sum(new Prod(new Var("y"), new Number(3)), new Number(5)));
    std::cout << c->toString() << std::endl;

    //cos((x+1)*pi)/e^x^2
    Expression* d = new Div(new Cos(new Prod(new Sum(new Var("x"), new Number(1)), new Pi()))
            , new Pow(new E(), new Pow(new Var("x"), new Number(2))));
    std::cout << d->toString() << std::endl;
    std::cout << d->eval() << std::endl;

    //pi-(2+x*7)
    Expression *z = new Diff(new Pi(),new Sum(new Number(2),new Prod(new Var("x"),new Number(7))));
    std::cout << z->toString() << std::endl;

    std::cout << std::endl;

    Var::addValuation("x", 0);
    Var::addValuation("y", 0);

    std::pair<double, double> values[5] = {
            std::make_pair(0,0),
            std::make_pair(0,0.5),
            std::make_pair(0.5,0),
            std::make_pair(0.5,0.5),
            std::make_pair(1,1)
    };

    Var::removeValuation("x");
    Var::removeValuation("y");

    for (int i = 0; i < 5; i += 1) {
        std::cout << "\n x = " << values[i].first << " ";
        Var::modifyValuation("x", values[i].first);
        std::cout << "\n y = " << values[i].second << "\n";
        Var::modifyValuation("y", values[i].second);
        std::cout << a->toString() << " = " << a->eval() << std::endl;
        std::cout << b->toString() << " = " << b->eval() << std::endl;
        std::cout << c->toString() << " = " << c->eval() << std::endl;
        std::cout << d->toString() << " = " << d->eval() << std::endl;
        std::cout << z->toString() << " = " << z->eval() << std::endl;
    }


    return 0;
}
