#ifndef LINE_H
#define LINE_H

#include "point.h"

class Line {
public:
    Line(const Point &, const Point &);

    double getA() const;

    double getB() const;

    bool intersects(const Line &) const;

    bool isParallel(const Line &) const;

    bool isPerpendicular(const Line &) const;

    bool containsPoint(const Point &) const;

    Point intersectionPoint(const Line &) const;


private:
    double a;
    double b;
};

#endif