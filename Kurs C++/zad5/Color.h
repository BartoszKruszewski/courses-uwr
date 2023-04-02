#pragma once

#include <iostream>

class Color {
public:
    Color();

    Color(int r, int g, int b);

    int getR() const;

    int getG() const;

    int getB() const;

    void setR(int value);

    void setG(int value);

    void setB(int value);

    virtual void brighten(int value);

    virtual void darken(int value);

    static Color mixColor(const Color &color1, const Color &color2);

    friend std::ostream &operator<<(std::ostream &out, const Color &color);

private:
    int r;
    int g;
    int b;

};
