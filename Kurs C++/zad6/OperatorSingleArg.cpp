#include "OperatorSingleArg.h"
#include <cmath>
#include <stdexcept>

void OperatorSingleArg::setArg1(Expression* expression) {
    arg1 = expression;
}

Expression* OperatorSingleArg::getArg1() const {
    return arg1;
}

OperatorSingleArg::OperatorSingleArg(Expression* expression) : arg1((Expression* ) expression), operatorSymbol("") {
    setPriority(6);
}

void OperatorSingleArg::setOperatorSymbol(std::string symbol) {
    operatorSymbol = symbol;
}

std::string OperatorSingleArg::getOperatorSymbol() const {
    return operatorSymbol;
}

std::string OperatorSingleArg::toString() const {
    return getOperatorSymbol() + "(" + arg1->toString() + ")";
}

double Sin::eval() const {
    return std::sin(getArg1()->eval());
}

Sin::Sin(Expression* expression) : OperatorSingleArg(expression) {
    setOperatorSymbol("sin");
}

double Cos::eval() const {
    return std::cos(getArg1()->eval());
}

Cos::Cos(Expression* expression) : OperatorSingleArg(expression) {
    setOperatorSymbol("cos");
}

double Exp::eval() const {
    return std::exp(getArg1()->eval());
}

Exp::Exp(Expression* expression) : OperatorSingleArg(expression) {
    setOperatorSymbol("exp");
}

Ln::Ln(Expression* expression) : OperatorSingleArg(expression) {
    setOperatorSymbol("ln");
    if (expression->eval() <= 0) {
        throw std::invalid_argument("Liczba logarytmowana musi byc dodatnia");
    }
    OperatorSingleArg::setArg1(expression);
}

double Ln::eval() const {
    return std::log(getArg1()->eval());
}

double Abs::eval() const {
    return std::abs(getArg1()->eval());
}

Abs::Abs(Expression* expression) : OperatorSingleArg(expression) {
    setOperatorSymbol("abs");
}

double Opp::eval() const {
    return -1 * getArg1()->eval();
}

Opp::Opp(Expression* expression) : OperatorSingleArg(expression) {
    setOperatorSymbol("opp");
}

double Inv::eval() const {
    return 1 / getArg1()->eval();
}

Inv::Inv(Expression* expression) : OperatorSingleArg(expression) {
    setOperatorSymbol("inv");
    if (expression->eval() == 0) {
        throw std::invalid_argument("Zero nie ma liczby odwrotnej");
    }
    OperatorSingleArg::setArg1(expression);
}
