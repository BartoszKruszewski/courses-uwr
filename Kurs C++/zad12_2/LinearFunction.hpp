#pragma once
#include <iostream>
#include <functional>
#include <complex>

template<typename T>
class LinearFunction {
private:
    T a;
    T b;

public:
    LinearFunction(T a, T b) : a(a), b(b) {}

    T operator()(const T& x) {
        std::multiplies<T> multiply;
        std::plus<T> add;
        return add(multiply(a, x), b);
    }
};

