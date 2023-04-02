#include "vector2.h"

Vector2::Vector2(double x, double y) {
    this->x = x;
    this->y = y;
}

double Vector2::getX() const{
    return x;
}

double Vector2::getY() const{
    return y;
}

