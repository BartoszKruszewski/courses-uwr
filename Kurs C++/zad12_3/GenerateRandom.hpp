#pragma once

#include <iostream>
#include <random>

template<int a, int b>
auto generateRandom() {
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<> dis(a, b);

    return [&dis, &gen]() {
        return dis(gen);
    };
}
