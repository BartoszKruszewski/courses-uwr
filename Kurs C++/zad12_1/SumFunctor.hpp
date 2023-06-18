#pragma once
#include <iostream>

template<typename T>
class SumFunctor {
public:
    SumFunctor() : sum(0), count(0) {}

    void operator()(const T &value) {
        sum += value;
        count++;
        double average = static_cast<double>(sum) / count;
        std::cout << "Sum: " << sum << ", Count: " << count << ", Average: " << average << std::endl;
    }
private:
    T sum;
    int count;
};
