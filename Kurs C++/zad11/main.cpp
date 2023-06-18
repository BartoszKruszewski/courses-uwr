#include <iostream>
#include "Expression.hpp"
#include "Operand.hpp"

int main() {
    std::string input;
    std::string instruction;
    std::string exp;
    std::string variableName;
    do {
        std::getline(std::cin, input);
        int i = 0;
        instruction = "";
        while (i < input.length() && input[i] != ' ')
            instruction += input[i++];
        try {
            if (instruction == "print") {
                exp = "";
                i++;
                while (i < input.length()) {
                    exp += input[i++];
                }
                std::cout << calc::Expression(exp).eval() << std::endl;
            } else if (instruction == "set") {
                variableName = "";
                i++;
                while (i < input.length() && input[i] != ' ')
                    variableName += input[i++];
                exp = "";
                i += 4;
                while (i < input.length()) {
                    exp += input[i++];
                }
                calc::Variable::setVariable(variableName, calc::Expression(exp).eval());
                std::cout << calc::Expression(exp).eval() << std::endl;
            } else if (instruction == "clear") {
                calc::Variable::clearVariables();
            } else if (instruction != "exit")
                std::clog << "Nie rozpoznano polecenia!" << std::endl;
        }
        catch (const std::exception &exception) {
            std::clog << exception.what() << std::endl;
        }

    } while (instruction != "exit");
    return 0;
}
