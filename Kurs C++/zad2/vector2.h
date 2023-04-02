#ifndef VECTOR2_H
#define VECTOR2_H

class Vector2 {
public:
    Vector2(double x, double y);

    double getX() const;

    double getY() const;

private:
    double x;
    double y;
};

#endif