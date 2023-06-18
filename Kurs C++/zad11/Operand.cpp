#include "Operand.hpp"
#include <stdexcept>

namespace calc {
    double Operand::eval() const {
        return value;
    }
    void Operand::setValue(double v) {
        value = v;
    }
    Variable::Variable(const std::string &n) : Operand() {
        name = n;
    }

    std::map<std::string, double> Variable::valuations;

    void Variable::setVariable(const std::string &n, double value) {
        if (Variable::valuations.count(n) > 0) {
            Variable::valuations.erase(n);
        }
        Variable::valuations[n] = value;
    }
    void Variable::clearVariables() {
        Variable::valuations.clear();
    }
    double Variable::eval() const {
        if (Variable::valuations.count(name) > 0)
            return Variable::valuations[name];
        else
            throw std::out_of_range("Nie zdefiniowano wartosci dla podanej nazwy zmiennej!");
    }
    Number::Number(double v) : Operand() {
        setValue(v);
    }
    Const::Const(const std::string &type) : Operand() {
        if (type == "pi")
            setValue(3.141592653589);
        else if (type == "e")
            setValue(2.718281828459);
        else if (type == "fi")
            setValue(1.618033988750);
        else
            throw std::invalid_argument("Nie rozpoznano nazwy stalej!");
    }


}
