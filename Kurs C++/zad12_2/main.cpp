#include <iostream>
#include "LinearFunction.hpp"

int main() {
    LinearFunction<int> intLinearFunc(2, 3);
    std::cout << "int: " << intLinearFunc(5) << std::endl;

    LinearFunction<float> floatLinearFunc(1.5, 2.0);
    std::cout << "float: " << floatLinearFunc(3.5) << std::endl;

    LinearFunction<double> doubleLinearFunc(0.5, 1.0);
    std::cout << "double: " << doubleLinearFunc(2.5) << std::endl;

    std::complex<double> a(2.0, 1.0);
    std::complex<double> b(1.0, 3.0);
    LinearFunction<std::complex<double>> complexLinearFunc(a, b);
    std::cout << "complex: " << complexLinearFunc(std::complex<double>(1.0, 2.0)) << std::endl;

    return 0;
}

