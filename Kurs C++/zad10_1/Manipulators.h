#pragma once
#include <iostream>
#include <iomanip>

struct IndexManipulator
{
    IndexManipulator(int x, int w) : x(x), w(w) {}
    int x;
    int w;

};

struct IndexIgnore
{
    IndexIgnore(int x) : x(x) {}
    int x;
};

IndexManipulator index(int x, int w);
IndexIgnore ignore(int x);
std::ostream& comma(std::ostream& os);
std::ostream& colon(std::ostream& os);
std::istream& clearLine(std::istream& is);
