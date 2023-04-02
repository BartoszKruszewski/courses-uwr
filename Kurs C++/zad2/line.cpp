#include <stdexcept>
#include "line.h"
#include "point.h"

Line::Line(const Point &a, const Point &b) {

    if (a.getX() == b.getX() && a.getY() == b.getY()) {
        throw std::invalid_argument("Do definicji prostej potrzebne sa dwa rozne punkty!");
    }
    this->a = (a.getY() - b.getY()) / (a.getX() - b.getX());
    this->b = (a.getY() - this->a * a.getX());
}

double Line::getA() const {
    return a;
}

double Line::getB() const {
    return b;
}

bool Line::intersects(const Line &l) const {
    return this->a != l.getA() || (this->a == l.getA() && this->b == l.getB());
}

bool Line::isParallel(const Line &l) const {
    return this->a == l.getA();
}

bool Line::isPerpendicular(const Line &l) const {
    return this->a * l.getA() == -1;
}

bool Line::containsPoint(const Point &p) const {
    return this->a * p.getX() + this->b == p.getY();
}

Point Line::intersectionPoint(const Line &l) const {
    if (this->a == l.getA()) {
        throw std::invalid_argument("Proste rownolegle nie maja punktu przeciecia!");
    }
    double x = (l.getB() - this->b) / (this->a - l.getA());
    double y = this->a * x + this->b;
    return Point(x, y);
}

