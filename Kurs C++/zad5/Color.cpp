#include "Color.h"
#include <stdexcept>
#include <iostream>

Color::Color() {
    r = 0;
    g = 0;
    b = 0;
}

Color::Color(int r, int g, int b) : Color() {
    setR(r);
    setG(g);
    setB(b);
}

int Color::getR() const {
    return r;
}

int Color::getG() const {
    return g;
}

int Color::getB() const {
    return b;
}

void Color::setR(int value) {
    if (value > 255 || value < 0)
        throw std::invalid_argument("Wartosc musi byc z przedzialu 0 do 255");
    r = value;
}

void Color::setG(int value) {
    if (value > 255 || value < 0)
        throw std::invalid_argument("Wartosc musi byc z przedzialu 0 do 255");
    g = value;
}

void Color::setB(int value) {
    if (value > 255 || value < 0)
        throw std::invalid_argument("Wartosc musi byc z przedzialu 0 do 255");
    b = value;
}

void Color::brighten(int value) {
    if (r + value <= 255)
        r += value;
    else
        r = 255;
    if (g + value <= 255)
        g += value;
    else
        g = 255;
    if (b + value <= 255)
        b += value;
    else
        b = 255;
}

void Color::darken(int value) {
    if (r - value >= 0)
        r -= value;
    else
        r = 0;
    if (g - value >= 0)
        g -= value;
    else
        g = 0;
    if (b - value >= 0)
        b -= value;
    else
        b = 0;
}

Color Color::mixColor(const Color &color1, const Color &color2) {
    int red = (color1.getR() + color2.getR()) / 2;
    int green = (color1.getG() + color2.getG()) / 2;
    int blue = (color1.getB() + color2.getB()) / 2;
    return {red, green, blue};
}

std::ostream &operator<<(std::ostream &out, const Color &color) {
    out << "(r: " << color.getR() << ", g: " << color.getG() << ", b: " << color.getB() << ")";
    return out;
}
