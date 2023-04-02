# pragma once

# include "Pixel.h"
# include "ColorAlpha.h"
# include <iostream>

class PixelColor : public Pixel {
public:
    PixelColor();

    PixelColor(int x, int y, const ColorAlpha &color);

    void setColor(ColorAlpha color);

    ColorAlpha getColor() const;

    void moveVector(int x, int y);

    friend std::ostream &operator<<(std::ostream &out, const PixelColor &pixel);

private:
    ColorAlpha color;
};