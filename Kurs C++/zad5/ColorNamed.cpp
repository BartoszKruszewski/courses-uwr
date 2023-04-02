#include <stdexcept>
#include "ColorNamed.h"

ColorNamed::ColorNamed() {
    setR(0);
    setG(0);
    setB(0);
    name = "";
}

ColorNamed::ColorNamed(int r, int g, int b, std::string &name) {
    setR(r);
    setG(g);
    setB(b);
    this->name = name;
}

std::string ColorNamed::getName() const {
    return name;
}

void ColorNamed::setName(std::string name) {
    for (char c : name)
        if (!islower(c))
            throw std::invalid_argument("Nazwa musi skladac sie wylacznie z malych liter");
    this->name = name;
}
