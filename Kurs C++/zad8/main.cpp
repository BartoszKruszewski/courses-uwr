#include <iostream>
#include "Rational.h"
#include "RationalException.h"


int main() {
    calculations::Rational a;
    calculations::Rational b(2);
    calculations::Rational c(1, 3);
    calculations::Rational d(2147483647);
    calculations::Rational e = d;
    calculations::Rational f(d);

    std::cout << "a: " << a << std::endl;
    std::cout << "b: " << b << std::endl;
    std::cout << "c: " << c << std::endl;
    std::cout << "d: " << d << std::endl;
    std::cout << "e: " << e << std::endl;
    std::cout << "f: " << f << std::endl;

    std::cout << "b + c: " << b + c << std::endl;
    std::cout << "b - c: " << b - c << std::endl;
    std::cout << "b * c: " << b * c << std::endl;
    std::cout << "b / c: " << b / c << std::endl;
    std::cout << "-c : " << -c << std::endl;
    std::cout << "!c: " << !c << std::endl;
    std::cout << "(double)c : " << (double) c << std::endl;
    std::cout << "(int)c: " << (int) c << std::endl;

    try {
        std::cout << d + d << std::endl;
    }
    catch (OutOfRangeException &e) {
        std::cout << e.what() << std::endl;
    }
    catch (...) {}

    try {
        std::cout << d / a << std::endl;
    }
    catch (DivisionByZeroException &e) {
        std::cout << e.what() << std::endl;
    }
    catch (...) {}

    return 0;
}
