#ifndef POINT_H
#define POINT_H
#include "vector2.h"

class Point {
public:
    Point(double x, double y);

    double getX() const;

    double getY() const;

    double distanceTo(const Point &) const;

    void vectorOffset(const Vector2 &);

    void rotate(const Point &, double angle);

    void xAxisSymetry();

    void yAxisSymetry();

    void pointSymetry(const Point &);

private:
    double x;
    double y;
};

#endif
