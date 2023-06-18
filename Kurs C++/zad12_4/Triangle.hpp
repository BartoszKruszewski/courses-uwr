#pragma once

#include <iostream>
#include <string>
#include <cmath>
#include <algorithm>

class Triangle {
public:
    Triangle();
    Triangle(double a, double b, double c, std::string name);

    [[nodiscard]] double getA() const;
    [[nodiscard]] double getB() const;
    [[nodiscard]] double getC() const;
    [[nodiscard]] double perimeter() const;
    [[nodiscard]] double area() const;
    [[nodiscard]] bool  isAcuteTriangle() const;

        friend std::ostream &operator<<(std::ostream &os, const Triangle &triangle);
private:
    [[nodiscard]] static bool isTriangle(double a, double b, double c) ;
private:
    double a;
    double b;
    double c;
    std::string name;
};

