#include "Expression.h"
#include <string>
#include <vector>
#include <stdexcept>
#include <cmath>


Number::Number(double value) {
    this->value = value;
}

double Number::eval() const {
    return value;
}

std::string Number::toString() const {
    std::string str = std::to_string(value);
    size_t dotPos = str.find('.');
    if (dotPos != std::string::npos) {
        size_t lastNonZero = str.find_last_not_of('0');
        if (lastNonZero == dotPos) {
            lastNonZero--;
        }
        str = str.substr(0, lastNonZero + 1);
    }
    return str;
}

Var::Var(std::string name) {
    this->name = name;
}

double Var::eval() const {
    for (const std::pair<std::string, double> valuation: valuations) {
        if (valuation.first == name) {
            return valuation.second;
        }
    }
    throw std::invalid_argument("Zmienna nie ma określonej wartości");
}

std::string Var::toString() const {
    return name;
}

void Var::addValuation(std::string name, double value) {
    Var::valuations.push_back(std::pair<std::string, double>(name,value));
}

void Var::removeValuation(std::string name) {
    int i = 0;
    for (std::pair<std::string, double> valuation: Var::valuations) {
        if (valuation.first == name) {
            valuations.erase(valuations.begin() + i);
            break;
        }
        i++;
    }
}

void Var::modifyValuation(std::string name, double value) {
    removeValuation(name);
    addValuation(name, value);
}

double Pi::eval() const {
    return 3.14159265359;
}

std::string Pi::toString() const {
    return "pi";
}

double E::eval() const {
    return 2.71828182846 ;
}

std::string E::toString() const {
    return "e";
}

double Fi::eval() const {
    return 1.618033988;
}

std::string Fi::toString() const {
    return "fi";
}

std::vector<std::pair<std::string, double>> Var::valuations;

void Expression::setPriority(uint8_t value) {
    priority = value;
}

uint8_t Expression::getPriority() const {
    return priority;
}

void Expression::setCombined(uint8_t value) {
    combined = value;
}

uint8_t Expression::getCombined() const {
    return combined;
}
