#include "Function.hpp"
#include <cmath>
#include <stdexcept>

calc::Function::Function(const std::string &t) {
    if (t == "modulo" || t == "min" || t == "max" || t == "log" || t == "pow" || t == "+" || t == "-" || t == "*" ||
        t == "/")
        argsAmount = 2;
    else if (t == "abs" || t == "sgn" || t == "floor" || t == "ceil" || t == "frac" || t == "sin" || t == "cos" ||
             t == "atan" || t == "acot" || t == "ln" || t == "exp")
        argsAmount = 1;
    else
        throw std::invalid_argument("Nie rozpoznano nazwy funkcji!");
    type = t;
}

double calc::Function::eval(double number1, double number2) const {
    if (type == "modulo")
        return number1 - std::floor(number1 / number2) * number2;
    else if (type == "+")
        return number1 + number2;
    else if (type == "-")
        return number1 - number2;
    else if (type == "*")
        return number1 * number2;
    else if (type == "/") {
        if (number2 == 0.0)
            throw std::invalid_argument("Dzielenie przez zero!");
        return number1 / number2;
    }
    else if (type == "min")
        return std::min(number1, number2);
    else if (type == "max")
        return std::max(number1, number2);
    else if (type == "log") {
        if (number2 <= 0 || number2 == 1) {
            throw std::invalid_argument("Bledna podstawa logarytmu!");
        }
        else if (number1 <= 0) {
            throw std::invalid_argument("Liczba logarytmowana musi byc dodatnia!");
        }
        return std::log(number2) / std::log(number1);
    }
    else if (type == "pow")
        return std::pow(number1, number2);
    else
        throw std::invalid_argument("Nie rozpoznano nazwy funkcji!");
}

double calc::Function::eval(double number) const {
    if (type == "abs")
        return std::abs(number);
    else if (type == "sgn")
        return number > 0 ? 1 : (number == 0 ? 0 : -1);
    else if (type == "floor")
        return std::floor(number);
    else if (type == "ceil")
        return std::ceil(number);
    else if (type == "frac")
        return std::fmod(number, 1.0);
    else if (type == "sin")
        return std::sin(number);
    else if (type == "cos")
        return std::cos(number);
    else if (type == "atan")
        return std::atan(number);
    else if (type == "acot")
        return std::atan(1 / number);
    else if (type == "ln")
        return std::log(number);
    else if (type == "exp")
        return std::exp(number);
    else
        throw std::invalid_argument("Nie rozpoznano nazwy funkcji!");
}
