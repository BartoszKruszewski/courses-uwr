#include <iostream>
#include <set>
#include <list>
#include <vector>
#include <algorithm>
#include "SumFunctor.hpp"

int main() {
    std::set<int> intSet = { 1, 2, 3, 4, 5 };
    std::list<float> floatList = { 1.5, 2.5, 3.5, 4.5, 5.5 };
    std::vector<double> doubleVector = { 1.2, 2.3, 3.4, 4.5, 5.6 };

    SumFunctor<int> sumInt;
    std::cout << "Summing integers:" << std::endl;
    std::for_each(intSet.begin(), intSet.end(), sumInt);

    SumFunctor<float> sumFloat;
    std::cout << "Summing floats:" << std::endl;
    std::for_each(floatList.begin(), floatList.end(), sumFloat);

    SumFunctor<double> sumDouble;
    std::cout << "Summing doubles:" << std::endl;
    std::for_each(doubleVector.begin(), doubleVector.end(), sumDouble);

    return 0;
}

