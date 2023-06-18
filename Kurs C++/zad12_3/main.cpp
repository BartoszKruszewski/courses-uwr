#include <iostream>
#include <array>
#include <vector>
#include <algorithm>
#include "GenerateRandom.hpp"

int main() {
    auto randomIntGenerator = generateRandom<1, 100>();

    int arrayInts[10];
    std::generate(std::begin(arrayInts), std::end(arrayInts), randomIntGenerator);

    std::cout << "Array: ";
    std::for_each(std::begin(arrayInts), std::end(arrayInts), [](int x) {
        std::cout << x << " ";
    });
    std::cout << std::endl;

    std::array<int, 10> stdArrayInts{};
    std::generate(std::begin(stdArrayInts), std::end(stdArrayInts), randomIntGenerator);

    std::cout << "std::array: ";
    std::for_each(std::begin(stdArrayInts), std::end(stdArrayInts), [](int x) {
        std::cout << x << " ";
    });
    std::cout << std::endl;

    std::vector<int> vectorInts(10);
    std::generate(std::begin(vectorInts), std::end(vectorInts), randomIntGenerator);

    std::cout << "std::vector: ";
    std::for_each(std::begin(vectorInts), std::end(vectorInts), [](int x) {
        std::cout << x << " ";
    });
    std::cout << std::endl;

    auto isPrime = [](int number) {
        if (number < 2)
            return false;
        for (int i = 2; i * i <= number; ++i) {
            if (number % i == 0)
                return false;
        }
        return true;
    };

    int primes[10];
    auto primesEnd = std::copy_if(std::begin(arrayInts),std::end(arrayInts), std::begin(primes), isPrime);
    primesEnd = std::copy_if(std::begin(stdArrayInts),std::end(stdArrayInts), primesEnd, isPrime);
    primesEnd = std::copy_if(std::begin(vectorInts),std::end(vectorInts), primesEnd, isPrime);
    int primeCount = std::distance(std::begin(primes), primesEnd);

    std::cout << "Prime numbers: ";
    std::for_each(std::begin(primes), primesEnd, [](int x) {
        std::cout << x << " ";
    });
    std::cout << std::endl;

    std::cout << "Prime count: " << primeCount << std::endl;

    return 0;
}
