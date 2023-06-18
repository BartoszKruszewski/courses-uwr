#include <iostream>

int main() {
    auto collatz = [](int n, int len, const auto& f) {
        std::cout << n << " ";
        if (n == 1) return 1;
        return ((n % 2 == 0) ? f(n / 2, len, f) : f(3 * n + 1, len, f)) + 1;
    };
    int len = collatz(10, 0, collatz);
    std::cout << std::endl << "Collatz sequence len: " << len << std::endl;

    return 0;
}
