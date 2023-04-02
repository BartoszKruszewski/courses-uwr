#pragma once

#include "ColorAlpha.h"
#include "ColorNamed.h"
#include <string>
#include <iostream>

class ColorAlphaNamed : public ColorAlpha, public ColorNamed {
public:
    ColorAlphaNamed();

    ColorAlphaNamed(int r, int g, int b, int a, const std::string &name);

    friend std::ostream &operator<<(std::ostream &out, const ColorAlphaNamed &color);
};
