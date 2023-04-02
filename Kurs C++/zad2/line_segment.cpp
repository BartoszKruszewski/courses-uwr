#include "line_segment.h"
#include <cmath>
#include <stdexcept>
#include <iostream>
#include "point.h"
#include "line.h"

LineSegment::LineSegment(const Point &a, const Point &b) {
    if (a.getX() == b.getX() && a.getY() == b.getY()) {
        throw std::invalid_argument("Odcinek nie moze miec 0 dlugosci!");
    }
    this->a = a;
    this->b = b;
}

Point LineSegment::getA() const{
    return a;
}

Point LineSegment::getB() const{
    return b;
}

double LineSegment::length() const{
    double dx = this->a.getX() - this->b.getX();
    double dy = this->a.getY() - this->b.getY();
    return std::sqrt(dx * dx + dy * dy);
}

void LineSegment::vectorOffset(const Vector2 &v) {
    this->a.vectorOffset(v);
    this->b.vectorOffset(v);
}

void LineSegment::rotate(const Point &p, double angle) {
    this->a.rotate(p, angle);
    this->b.rotate(p, angle);
}

void LineSegment::xAxisSymetry() {
    this->a.xAxisSymetry();
    this->b.xAxisSymetry();
}

void LineSegment::yAxisSymetry() {
    this->a.yAxisSymetry();
    this->b.yAxisSymetry();
}

void LineSegment::pointSymetry(const Point &p) {
    this->a.pointSymetry(p);
    this->b.pointSymetry(p);
}

Line LineSegment::getLine() const {
    Line l(this->getA(), this->getB());
    return l;
}

bool LineSegment::containsPoint(const Point &p) const {
    return this->getLine().containsPoint(p) &&
           p.getX() <= std::fmax(this->a.getX(), this->b.getX()) &&
           p.getX() >= std::fmin(this->a.getX(), this->b.getX());
}

bool LineSegment::isParallel(const LineSegment &l) const {
    return this->getLine().isParallel(l.getLine());
}

bool LineSegment::isPerpendicular(const LineSegment &l) const{
    return this->getLine().isPerpendicular(l.getLine());
}

bool LineSegment::intersectsLine(const Line &l) const {

    return this->getLine().intersects(l) && this->containsPoint(this->getLine().intersectionPoint(l));
}

bool LineSegment::intersectsLineSegment(const LineSegment &l) const {
    return this->intersectsLine(l.getLine()) && l.intersectsLine(this->getLine());
}