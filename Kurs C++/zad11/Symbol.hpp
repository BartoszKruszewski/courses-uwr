#pragma once

#include <string>

class Symbol {
public:
    [[nodiscard]] virtual double eval(double number1, double number2) const = 0;
    [[nodiscard]] virtual double eval(double number) const = 0;
    [[nodiscard]] virtual double eval() const = 0;
    [[nodiscard]] int getArgsAmount() const;
protected:
    int argsAmount = 0;
};
