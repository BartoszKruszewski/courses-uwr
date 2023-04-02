#include "triangle.h"
#include <cmath>
#include <stdexcept>
#include "point.h"
#include "line_segment.h"

Triangle::Triangle(const Point &a, const Point &b, const Point &c) {
    if ((a.getX() == b.getX() && a.getY() == b.getY()) ||
        (a.getX() == c.getX() && a.getY() == c.getY()) ||
        (b.getX() == c.getX() && b.getY() == c.getY())) {
        throw std::invalid_argument("Trojkat nie moze miec dwoch takich samych wierzcholkow!");
    }
    if (Line(a, b).containsPoint(c)) {
        throw std::invalid_argument("Wierzcholki trojkata nie moga byc wspolliniowe!");
    }
    this->a = a;
    this->b = b;
    this->c = c;
    this->aSide = LineSegment(a, b);
    this->bSide = LineSegment(b, c);
    this->cSide = LineSegment(a, c);
}

Point Triangle::getA() const {
    return a;
}

Point Triangle::getB() const {
    return b;
}

Point Triangle::getC() const {
    return c;
}

LineSegment Triangle::getASide() const {
    return aSide;
}

LineSegment Triangle::getBSide() const {
    return bSide;
}

LineSegment Triangle::getCSide() const {
    return cSide;
}

double Triangle::area() const {
    return std::abs(
            (this->b.getX() - this->a.getX()) * (this->c.getY() - this->a.getY()) -
            (this->b.getY() - this->a.getY()) * (this->c.getX() - this->a.getX())) / 2;
}

double Triangle::perimeter() const {
    return this->aSide.length() + this->bSide.length() + this->cSide.length();
}

void Triangle::vectorOffset(const Vector2 &v) {
    this->a.vectorOffset(v);
    this->b.vectorOffset(v);
    this->c.vectorOffset(v);
}

void Triangle::rotate(const Point &p, double angle) {
    this->a.rotate(p, angle);
    this->b.rotate(p, angle);
    this->c.rotate(p, angle);
}

void Triangle::xAxisSymetry() {
    this->a.xAxisSymetry();
    this->b.xAxisSymetry();
    this->c.xAxisSymetry();
}

void Triangle::yAxisSymetry() {
    this->a.yAxisSymetry();
    this->b.yAxisSymetry();
    this->c.yAxisSymetry();
}

void Triangle::pointSymetry(const Point &p) {
    this->a.pointSymetry(p);
    this->b.pointSymetry(p);
    this->c.pointSymetry(p);

}

bool Triangle::containsPoint(const Point &p) const {
    double pacArea = 0;
    double pabArea = 0;
    double pbcArea = 0;
    try {
        pacArea = Triangle(this->a, this->c, p).area();
    }
    catch (...) {}
    try {
        pabArea = Triangle(this->a, this->b, p).area();
    }
    catch (...) {}
    try {
        pbcArea = Triangle(p, this->b, this->c).area();
    }
    catch (...) {}
    return pabArea + pacArea + pbcArea == this->area();
}

bool Triangle::containsTriangle(const Triangle &t) const {
    return this->containsPoint(t.getA()) && this->containsPoint(t.getB()) && this->containsPoint(t.getC());
}

bool Triangle::isDisjoint(const Triangle &t) const {
    return !(this->aSide.intersectsLineSegment(t.getASide()) ||
             this->aSide.intersectsLineSegment(t.getBSide()) ||
             this->aSide.intersectsLineSegment(t.getCSide()) ||
             this->bSide.intersectsLineSegment(t.getASide()) ||
             this->bSide.intersectsLineSegment(t.getBSide()) ||
             this->bSide.intersectsLineSegment(t.getCSide()) ||
             this->cSide.intersectsLineSegment(t.getASide()) ||
             this->cSide.intersectsLineSegment(t.getBSide()) ||
             this->cSide.intersectsLineSegment(t.getCSide()));
}