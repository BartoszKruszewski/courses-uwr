#include "Triangle.hpp"

#include <utility>

Triangle::Triangle() : a(1.0), b(1.0), c(1.0), name("Triangle") {}

Triangle::Triangle(double a, double b, double c, std::string name) : a(a), b(b), c(c), name(std::move(name)) {
    if (!isTriangle(a, b, c)) {
        throw std::invalid_argument("Triangle inequality not satisfied!");
    }
}
double Triangle::getA() const {
    return a;
}
double Triangle::getB() const {
    return b;
}
double Triangle::getC() const {
    return c;
}
double Triangle::perimeter() const {
    return a + b + c;
}
double Triangle::area() const {
    double p = perimeter() / 2.0;
    return std::sqrt(p * (p - a) * (p - b) * (p - c));
}
std::ostream &operator<<(std::ostream &os, const Triangle &triangle) {
    os << "Name: " << triangle.name << ", Side A: " << triangle.a << ", Side B: " << triangle.b << ", Side C: "
       << triangle.c << ", Is Actue?: " << triangle.isAcuteTriangle();
    return os;
}
bool Triangle::isTriangle(double a, double b, double c) {
    return (a + b > c) && (b + c > a) && (c + a > b);
}
bool Triangle::isAcuteTriangle() const {
    bool isGoodA = (b * b) + (c * c) > (a * a);
    bool isGoodB = (a * a) + (c * c) > (b * b);
    bool isGoodC = (a * a) + (b * b) > (c * c);
    return isGoodA && isGoodB && isGoodC;
}
