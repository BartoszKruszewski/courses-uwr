#include <iostream>
#include "ColorAlphaNamed.h"
#include "PixelColor.h"

int main() {
    ColorAlphaNamed c1(215, 12, 1, 5, "czerwony");
    ColorAlphaNamed c2(15, 178, 14, 92, "zielony");
    PixelColor p1(15, 18, c1);
    PixelColor p2(78, 1045, c2);
    PixelColor *pointer1 = &p1;
    PixelColor *pointer2 = &p2;
    std::cout << p1 << std::endl;
    std::cout << p2 << std::endl;
    std::cout << c1 << std::endl;
    std::cout << c2 << std::endl;

    std::cout << "Odleglosc p1 do p2: " << distance(p1, p2) << std::endl;
    std::cout << "Odleglosc p1 do p2 (wskazniki): " << distance(pointer1, pointer2) << std::endl;
    std::cout << "Odleglosc p1 do gornej krawedzi ekranu: " << p1.distanceTop() << std::endl;
    std::cout << "Odleglosc p1 do dolnej krawedzi ekranu: " << p1.distanceBottom() << std::endl;
    std::cout << "Odleglosc p1 do lewej krawedzi ekranu: " << p1.distanceLeft() << std::endl;
    std::cout << "Odleglosc p1 do prawej krawedzi ekranu: " << p1.distanceRight() << std::endl;
    p1.moveVector(5, 7);
    std::cout << "Przesuniecie p1 o wektor [5,7]: " << p1 << std::endl;
    c1.brighten(15);
    std::cout << "Rozjasnienie c1 o 15: " << c1 << std::endl;
    c1.darken(32);
    std::cout << "Przyciemnienie c1 o 32: " << c1 << std::endl;
    std::cout << "Miks kolorow c1 i c2: " << Color::mixColor(c1, c2) << std::endl;


    return 0;
}
