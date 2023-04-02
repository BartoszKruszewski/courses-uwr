#include "ColorAlpha.h"
#include <stdexcept>

ColorAlpha::ColorAlpha() {
    setR(0);
    setG(0);
    setB(0);
    a = 0;
}

ColorAlpha::ColorAlpha(int r, int g, int b, int a) : ColorAlpha(){
    setR(r);
    setG(g);
    setB(b);
    setA(a);
}

void ColorAlpha::setA(int value) {
    if (value > 255 || value < 0)
        throw std::invalid_argument("Wartosc musi byc z przedzialu 0 do 255");
    a = value;
}

int ColorAlpha::getA() const {
    return a;
}

void ColorAlpha::brighten(int value) {
    Color::brighten(value);
    if (a + value <= 255)
        a += value;
    else
        a = 255;
}

void ColorAlpha::darken(int value) {
    Color::brighten(value);
    if (a - value >= 0)
        a -= value;
    else
        a = 0;
}

std::ostream &operator<<(std::ostream &out, const ColorAlpha &color) {
    out << "(r: " << color.getR() << ", g: " << color.getG() << ", b: " << color.getB() << ", a: " << color.getA()
        << ")";
    return out;
}
