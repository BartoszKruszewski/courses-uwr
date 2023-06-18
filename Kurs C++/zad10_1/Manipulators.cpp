#include "Manipulators.h"

IndexManipulator index(int x, int w)
{
    return {x, w};
}

IndexIgnore ignore(int x)
{
    return {x};
}

std::ostream& comma(std::ostream& os)
{
    os << ", ";
    return os;
}

std::ostream& colon(std::ostream& os)
{
    os << ": ";
    return os;
}

std::istream& clearLine(std::istream& is)
{
    char c;
    while (is.get(c) && c != '\n') {}
    return is;
}