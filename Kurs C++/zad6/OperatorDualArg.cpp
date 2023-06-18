#include "OperatorDualArg.h"
#include <cmath>
#include <stdexcept>
#include <iostream>

void OperatorDualArg::setArg2(Expression* expression) {
    arg2 = expression;
}

Expression* OperatorDualArg::getArg2() const {
    return arg2;
}

OperatorDualArg::OperatorDualArg(Expression* expression1, Expression* expression2) :
        OperatorSingleArg(expression1), arg2(expression2) {
}

std::string OperatorDualArg::toString() const {
    std::string expression1 = getArg1()->toString();
    std::string expression2 = getArg2()->toString();
    if (getArg1()->getPriority() < getPriority() || (getArg1()->getPriority() == getPriority() && (getCombined() == 2 || getCombined() == 0))) {
        expression1 = "(" + expression1 + ")";
    }
    if (getArg2()->getPriority() < getPriority() || (getArg2()->getPriority() == getPriority() && (getCombined() == 1 || getCombined() == 0))) {
        expression2 = "(" + expression2 + ")";
    }
    return expression1 + getOperatorSymbol() + expression2;
}

double Sum::eval() const {
    return getArg1()->eval() + getArg2()->eval();
}

Sum::Sum(Expression* expression1, Expression* expression2) :
        OperatorDualArg(expression1, expression2) {
    setOperatorSymbol("+");
    setPriority(2);
    setCombined(3);
}


double Diff::eval() const {
    return getArg1()->eval() - getArg2()->eval();;
}

Diff::Diff(Expression* expression1, Expression* expression2) :
        OperatorDualArg(expression1, expression2) {
    setOperatorSymbol("-");
    setPriority(2);
    setCombined(1);
}


double Prod::eval() const {
    return getArg1()->eval() * getArg2()->eval();;
}

Prod::Prod(Expression* expression1, Expression* expression2) :
        OperatorDualArg(expression1, expression2) {
    setOperatorSymbol("*");
    setPriority(3);
    setCombined(3);
}

double Div::eval() const {
    return getArg1()->eval() / getArg2()->eval();;
}

Div::Div(Expression* expression1, Expression* expression2) :
        OperatorDualArg(expression1, expression2) {
    setOperatorSymbol("/");
    setPriority(3);
    setCombined(2);
}


double Log::eval() const {
    return std::log(getArg1()->eval()) / std::log(getArg2()->eval());
}

std::string Log::toString() const {
    return "log(" + getArg1()->toString() + ", " + getArg2()->toString() + ")";
}

Log::Log(Expression* expression1, Expression* expression2) :
    OperatorDualArg(expression1, expression2) {
    if (expression2->eval() <= 0 || expression2->eval() == 1) {
        throw std::invalid_argument("Bledna podstawa logarytmu!");
    }
    else if (expression1->eval() <= 0) {
        throw std::invalid_argument("Liczba logarytmowana musi byc dodatnia!");
    }
    setArg1(expression1);
    setArg2(expression2);
    setPriority(5);
}

Mod::Mod(Expression* expression1, Expression* expression2) :
        OperatorDualArg(expression1, expression2) {
    setOperatorSymbol("%");
    double intPart;
    if (std::modf(expression1->eval(), &intPart) != 0.0 ||
        std::modf(expression2->eval(), &intPart) != 0.0) {
        throw std::invalid_argument("Modulo przyjmuje liczby całkowite!");
    }
    setArg1(expression1);
    setArg2(expression2);
    setPriority(1);
}

double Mod::eval() const {
    return (int)getArg1()->eval() % (int)getArg2()->eval();
}

double Pow::eval() const {
    return std::pow(getArg1()->eval(), getArg2()->eval());
}

Pow::Pow(Expression* expression1, Expression* expression2) :
        OperatorDualArg(expression1, expression2) {
    setOperatorSymbol("^");
    setPriority(4);
    setCombined(1);
}
