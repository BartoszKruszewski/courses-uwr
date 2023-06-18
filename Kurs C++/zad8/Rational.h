#pragma once

#include <iostream>

namespace calculations {
    class Rational {
    public:
        Rational();

        explicit Rational(int n, int dn = 1);

        [[nodiscard]] int getNominator() const;

        [[nodiscard]] int getDenominator() const;

        Rational operator+(const Rational &other) const;

        Rational operator-(const Rational &other) const;

        Rational operator*(const Rational &other) const;

        Rational operator/(const Rational &other) const;

        Rational operator-() const;

        Rational operator!() const;

        explicit operator double() const;

        explicit operator int() const;

        friend std::ostream &operator<<(std::ostream &output, const Rational &number);

    private:
        int nominator;
        int denominator;

        [[nodiscard]] static bool inRange(long long number);
        [[nodiscard]] static int GCD(int number1, int number2);
    };
}


