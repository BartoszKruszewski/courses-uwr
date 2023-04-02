#include "ColorAlphaNamed.h"


ColorAlphaNamed::ColorAlphaNamed() {
    setR(0);
    setG(0);
    setB(0);
    setA(0);
    setName("");

}

ColorAlphaNamed::ColorAlphaNamed(int r, int g, int b, int a, const std::string &name) {
    setR(r);
    setG(g);
    setB(b);
    setA(a);
    setName(name);
}

std::ostream &operator<<(std::ostream &out, const ColorAlphaNamed &color) {
    out << "(nazwa: " << color.getName() << ", r: " << color.getR() << ", g: " << color.getG() << ", b: " << color.getB() << ", a: " << color.getA() << ")";

    return out;
}
