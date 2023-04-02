#ifndef LINE_SEGMENT_H
#define LINE_SEGMENT_H

#include "point.h"
#include "line.h"

class LineSegment {
public:
    LineSegment(const Point &, const Point &);

    Point getA() const;

    Point getB() const;

    double length() const;

    void vectorOffset(const Vector2 &);

    void rotate(const Point &, double angle);

    void xAxisSymetry();

    void yAxisSymetry();

    void pointSymetry(const Point &);

    bool containsPoint(const Point &) const;

    bool isParallel(const LineSegment &) const;

    bool isPerpendicular(const LineSegment &) const;

    bool intersectsLine(const Line &) const;

    bool intersectsLineSegment(const LineSegment &) const;

    Line getLine() const;


private:
    Point a = Point(0, 0);
    Point b = Point(0, 0);
};

#endif