#ifndef TRIANGLE_H
#define TRIANGLE_H
#include "point.h"
#include "line_segment.h"

class Triangle {
public:
    Triangle(const Point &, const Point &, const Point &);

    Point getA() const;

    Point getB() const;

    Point getC() const;

    LineSegment getASide() const;

    LineSegment getBSide() const;

    LineSegment getCSide() const;

    double area() const;

    double perimeter() const;

    void vectorOffset(const Vector2 &);

    void rotate(const Point &, double angle);

    void xAxisSymetry();

    void yAxisSymetry();

    void pointSymetry(const Point &);

    bool containsPoint(const Point &) const;

    bool containsTriangle(const Triangle &) const;

    bool isDisjoint(const Triangle &) const;


private:
    Point a = Point(0,0);
    Point b = Point(0,0);
    Point c = Point(0,0);
    LineSegment aSide = LineSegment(Point(0,0), Point(0,1));
    LineSegment bSide = LineSegment(Point(0,0), Point(0,1));
    LineSegment cSide = LineSegment(Point(0,0), Point(0,1));
};

#endif