#include "Expression.hpp"
#include "Function.hpp"
#include "Operand.hpp"
#include <stack>
#include <stdexcept>

calc::Expression::Expression(const std::string &s) {
    std::string actualName;
    for (char c: s + " ") {
        if (c == ' ') {
            if (actualName == "modulo" || actualName == "min" || actualName == "max" || actualName == "log" ||
                actualName == "pow" || actualName == "abs" || actualName == "sgn" || actualName == "floor" ||
                actualName == "ceil" || actualName == "frac" || actualName == "sin" || actualName == "cos" ||
                actualName == "atan" || actualName == "acot" || actualName == "ln" || actualName == "exp" ||
                actualName == "+" || actualName == "-" || actualName == "*" || actualName == "/")
                symbols.push(new Function(actualName));
            else if (actualName == "pi" || actualName == "fi" || actualName == "e")
                symbols.push(new Const(actualName));
            else {
                char *end;
                std::strtod(actualName.c_str(), &end);
                if (*end == '\0')
                    symbols.push(new Number(std::stod(actualName)));
                else if (actualName.length() <= 7 && actualName != "print" && actualName != "set" &&
                         actualName != "to" && actualName != "clear" && actualName != "exit")
                    symbols.push(new Variable(actualName));
                else
                    throw std::invalid_argument("Nieprawidlowa nazwa zmiennej!");
            }
            actualName = "";
        } else
            actualName += c;
    }
}
double calc::Expression::eval() {
    std::stack<double> s;
    Symbol *symbol;
    while (!symbols.empty()) {
        symbol = symbols.front();
        symbols.pop();
        if (symbol->getArgsAmount() == 0)
            s.push(symbol->eval());
        else {
            double number1 = s.top();
            s.pop();
            if (symbol->getArgsAmount() == 1)
                s.push(symbol->eval(number1));
            else {
                double number2 = s.top();
                s.pop();
                s.push(symbol->eval(number2, number1));
            }
        }
    }
    return s.top();
}
