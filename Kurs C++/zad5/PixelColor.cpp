#include "PixelColor.h"

PixelColor::PixelColor() {
    setX(0);
    setY(0);
    color = ColorAlpha();
}

PixelColor::PixelColor(int x, int y, const ColorAlpha &color) : PixelColor() {
    setX(x);
    setY(y);
    setColor(color);
}

void PixelColor::setColor(ColorAlpha color) {
    this->color = color;
}

ColorAlpha PixelColor::getColor() const {
    return color;
}

void PixelColor::moveVector(int x, int y) {
    setX(getX() + x);
    setY(getY() + y);
}

std::ostream &operator<<(std::ostream &out, const PixelColor &pixel) {
    out << "(x: " << pixel.getX() << ", y: " << pixel.getY() << ", kolor: " << pixel.getColor() << ")";
    return out;
}
