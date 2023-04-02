#pragma once

#include "Color.h"
#include <iostream>

class ColorAlpha : public virtual Color {
public:
    ColorAlpha();

    ColorAlpha(int r, int g, int b, int a);

    void setA(int value);

    int getA() const;

    void brighten(int value);

    void darken(int value);

    friend std::ostream &operator<<(std::ostream &out, const ColorAlpha &color);

private:
    int a;
};
