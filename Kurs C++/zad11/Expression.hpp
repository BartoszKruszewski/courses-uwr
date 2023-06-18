#pragma once

#include <string>
#include <queue>
#include "Symbol.hpp"

namespace calc {
    class Expression {
    public:
        explicit Expression(const std::string &s);
        double eval();
    private:
        std::queue<Symbol *> symbols;
    };

}

