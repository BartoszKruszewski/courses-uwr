#pragma once

#include "Expression.hpp"
#include <string>

namespace calc {
    class Function : public Symbol {
    public:
        explicit Function(const std::string &t);
        [[nodiscard]] double eval(double number1, double number2) const override;
        [[nodiscard]] double eval(double number) const override;
        [[nodiscard]] double eval() const override { return 0; };
    private:
        std::string type;
    };
}

