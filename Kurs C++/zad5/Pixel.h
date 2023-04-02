# pragma once

class Pixel {
public:
    Pixel();

    Pixel(int x, int y);

    void setX(int value);

    void setY(int value);

    int getX() const;

    int getY() const;

    int distanceRight() const;

    int distanceLeft() const;

    int distanceTop() const;

    int distanceBottom() const;


private:
    int x;
    int y;
    const static int screenX = 1920;
    const static int screenY = 1080;
};

int distance(const Pixel &pixel1, const Pixel &pixel2);

int distance(const Pixel *pixel1, const Pixel *pixel2);
