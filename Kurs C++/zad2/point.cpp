#include "point.h"
#include <cmath>

Point::Point(double x, double y) {
    this->x = x;
    this->y = y;
}

double Point::getX() const{
    return x;
}

double Point::getY() const{
    return y;
}

double Point::distanceTo(const Point &other) const {
    double dx = x - other.getX();
    double dy = y - other.getY();
    return std::sqrt(dx * dx + dy * dy);
}

void Point::vectorOffset(const Vector2 &v) {
    this->x += v.getX();
    this->y += v.getY();
}

void Point::rotate(const Point &p, double angle) {
    double rad = angle * M_PI / 180;
    double xp = p.getX() + (x - p.getX()) * cos(rad) - (y - p.getY()) * sin(rad);
    double yp = p.getY() + (x - p.getX()) * sin(rad) + (y - p.getY()) * cos(rad);
    this->x = xp;
    this->y = yp;
}

void Point::xAxisSymetry() {
    this->y *= -1;
}

void Point::yAxisSymetry() {
    this->x *= -1;
}

void Point::pointSymetry(const Point &p) {
    this->x = 2 * p.getX() - this->x;
    this->y = 2 * p.getY() - this->y;
}
