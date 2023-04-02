#include <stdexcept>
#include <cmath>
#include "Pixel.h"

Pixel::Pixel() {
    x = 0;
    y = 0;
}

Pixel::Pixel(int x, int y) : Pixel() {
    setX(x);
    setY(y);
}

void Pixel::setX(int value) {
    if (x < 0 || x > screenX)
        throw std::invalid_argument("Punkt musi znajdowac sie na ekranie");
    x = value;
}

void Pixel::setY(int value) {
    if (y < 0 || y > screenY)
        throw std::invalid_argument("Punkt musi znajdowac sie na ekranie");
    y = value;
}

int Pixel::getX() const {
    return x;
}

int Pixel::getY() const {
    return y;
}

int Pixel::distanceRight() const {
    return screenX - x;
}

int Pixel::distanceLeft() const {
    return x;
}

int Pixel::distanceTop() const {
    return screenY - y;
}

int Pixel::distanceBottom() const {
    return y;
}


int distance(const Pixel &pixel1, const Pixel &pixel2) {
    return int(round(sqrt(pow(pixel1.getX() - pixel2.getX(), 2) + pow(pixel1.getY() - pixel2.getY(), 2))));
}

int distance(const Pixel *pixel1, const Pixel *pixel2) {
    return int(round(sqrt(pow(pixel1->getX() - pixel2->getX(), 2) + pow(pixel1->getY() - pixel2->getY(), 2))));
}
