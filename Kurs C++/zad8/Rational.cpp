#include <cmath>
#include <vector>
#include "Rational.h"
#include "RationalException.h"

calculations::Rational::Rational() {
    nominator = 0;
    denominator = 1;
}

calculations::Rational::Rational(int n, int dn) {

    if (dn == 0)
        throw DivisionByZeroException("Mianownik nie może byc rowny zero!");

    nominator = n;
    denominator = dn;

    if (denominator < 0) {
        nominator *= -1;
        denominator *= -1;
    }
    bool isNegative = nominator < 0;
    if (isNegative)
        nominator *= -1;

    int gcd = GCD(nominator, denominator);
    nominator /= gcd;
    denominator /= gcd;

    if (isNegative)
        nominator *= -1;
}

int calculations::Rational::getNominator() const {
    return nominator;
}

int calculations::Rational::getDenominator() const {
    return denominator;
}

calculations::Rational calculations::Rational::operator+(const calculations::Rational &other) const {
    long long newNominator = (long long) nominator * (long long) other.getDenominator() +
                             (long long) other.getNominator() * (long long) denominator;
    long long newDenominator = (long long) denominator * (long long) other.denominator;
    if (!inRange(newNominator)) {
        throw OutOfRangeException("Licznik nie miesci sie w zakresie!");
    }

    if (!inRange(newDenominator))
        throw OutOfRangeException("Mianownik nie miesci sie w zakresie!");
    return calculations::Rational((int) newNominator, (int) newDenominator);
}

calculations::Rational calculations::Rational::operator-(const calculations::Rational &other) const {
    long long newNominator = (long long) nominator * (long long) other.getDenominator() -
                             (long long) other.getNominator() * (long long) denominator;
    long long newDenominator = (long long) denominator * (long long) other.denominator;
    if (!inRange(newNominator))
        throw OutOfRangeException("Licznik nie miesci sie w zakresie!");
    if (!inRange(newDenominator))
        throw OutOfRangeException("Mianownik nie miesci sie w zakresie!");
    return calculations::Rational((int) newNominator, (int) newDenominator);
}

calculations::Rational calculations::Rational::operator*(const calculations::Rational &other) const {
    long long newNominator = (long long) nominator * (long long) other.getNominator();
    long long newDenominator = (long long) denominator * (long long) other.getDenominator();
    if (!inRange(newNominator))
        throw OutOfRangeException("Licznik nie miesci sie w zakresie!");
    if (!inRange(newDenominator))
        throw OutOfRangeException("Mianownik nie miesci sie w zakresie!");
    return calculations::Rational((int) newNominator, (int) newDenominator);
}

calculations::Rational calculations::Rational::operator/(const calculations::Rational &other) const {
    if (other.nominator == 0)
        throw DivisionByZeroException("Nie mozna dzielic przez zero!");
    long long newNominator = (long long) nominator * (long long) other.getDenominator();
    long long newDenominator = (long long) denominator * (long long) other.getNominator();
    if (!inRange(newNominator))
        throw OutOfRangeException("Licznik nie miesci sie w zakresie!");
    if (!inRange(newDenominator))
        throw OutOfRangeException("Mianownik nie miesci sie w zakresie!");
    return calculations::Rational((int) newNominator, (int) newDenominator);
}

calculations::Rational calculations::Rational::operator-() const {
    return calculations::Rational(-nominator, denominator);
}

calculations::Rational calculations::Rational::operator!() const {
    if (nominator == 0)
        throw DivisionByZeroException("Mianownik nie może byc rowny zero!");
    if (nominator > 0)
        return calculations::Rational(denominator, nominator);
    return calculations::Rational(-denominator, -nominator);
}

calculations::Rational::operator double() const {
    return (double) nominator / denominator;
}

calculations::Rational::operator int() const {
    return (int) round((double) nominator / denominator);
}

std::ostream &calculations::operator<<(std::ostream &output, const calculations::Rational &number) {
    bool isNegative = number.nominator < 0;
    int nominator = number.nominator;
    int denominator = number.denominator;
    if (isNegative)
        nominator *= -1;


    std::string integer = std::to_string(nominator / denominator);
    int rest = nominator % denominator;

    if (rest == 0) {
        if (isNegative)
            output << "-";
        output << integer;
        return output;
    }

    std::string result = integer + ".";
    std::vector<int> positions;

    while (rest > 0) {
        rest *= 10;
        for (int i = 0; i < positions.size(); i++) {
            if (positions[i] == rest / denominator) {
                result.insert(integer.length() + i + 1, "(");
                result += ")";
                rest = 0;
                break;
            }
        }
        if (rest != 0)
            result += std::to_string(rest / denominator);
        positions.push_back(rest / denominator);
        rest %= denominator;
    }

    if (isNegative)
        output << "-";
    output << result;
    return output;
}

bool calculations::Rational::inRange(long long number) {
    return number <= std::numeric_limits<int>::max() && number >= std::numeric_limits<int>::min();
}

int calculations::Rational::GCD(int number1, int number2) {
    if (number2 == 0) return number1;
    return GCD(number2, number1 % number2);
}
